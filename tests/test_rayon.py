"""Tests du compteur de rayons (incrémenté au constructeur, décrémenté par __del__)."""

from __future__ import annotations

import gc
from datetime import date

import pytest

from enseigne.produit import Produit
from enseigne.rayon import Rayon
from enseigne.vendeur import Vendeur


def test_compteur_et_destructeur():
    # Les rayons des graphes d'autres tests sont dans des cycles de références :
    # on les libère d'abord, puis on bloque le ramasse-miettes pendant le test.
    gc.collect()
    gc.disable()
    depart = Rayon.compteur
    try:
        rayon_vtt = Rayon("VTT")
        rayon_route = Rayon("Route")
        assert Rayon.compteur == depart + 2
        assert rayon_vtt.code_rayon != rayon_route.code_rayon
        del rayon_route  # CPython : libération immédiate, donc appel de __del__
        assert Rayon.compteur == depart + 1
    finally:
        Rayon.compteur = depart
        gc.enable()


def test_montant_total_sans_vendeur():
    rayon_tennis = Rayon("Tennis")
    Produit("P001", "Raquette Pro Carbon", 120.00, rayon_tennis)
    assert rayon_tennis.montant_total() == 0.0


def test_montant_total_avec_vendeur(monkeypatch):
    # Vendeur.montant_total n'est pas encore écrite : on la remplace pour ce test.
    monkeypatch.setattr(Vendeur, "montant_total", lambda self: self.montant_ventes)

    rayon_tennis = Rayon("Tennis")
    jean = Vendeur(
        "Benguigui",
        "Jean",
        "0624567267",
        "jean.benguigui@exemple.fr",
        date(2024, 9, 1),
        3,
        rayon_tennis,
    )
    jean.montant_ventes = 120.00 + 2 * 15.50  # 1 raquette + 2 tubes de balles

    assert rayon_tennis.montant_total() == pytest.approx(151.00)
