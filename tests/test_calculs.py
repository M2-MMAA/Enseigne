"""Tests des méthodes de calcul déjà écrites par le groupe (D6 bis)."""

from __future__ import annotations

from datetime import date

import pytest

from enseigne.achat import Achat
from enseigne.client import Client
from enseigne.produit import Produit
from enseigne.rayon import Rayon
from enseigne.vendeur import Vendeur


@pytest.fixture
def rayon() -> Rayon:
    """Un rayon vide, sans vendeur.

    Returns:
        Le rayon.
    """
    return Rayon("Tennis")


def test_montant_achat(rayon):
    raquette = Produit("P001", "Raquette", 89.90, rayon)
    assert Achat(raquette, 2).montant() == pytest.approx(179.80)


def test_montant_moyen_achat(rayon):
    raquette = Produit("P001", "Raquette", 89.90, rayon)
    balles = Produit("P002", "Balles", 12.25, rayon)
    client = Client("Martin", "Léa", "0600000000", "lea.martin@exemple.fr")
    client.ajouter_achat(Achat(raquette, 2))
    client.ajouter_achat(Achat(balles, 2))
    assert client.montant_moyen_achat() == pytest.approx(102.15)


def test_montant_moyen_achat_sans_achat():
    client = Client("Martin", "Léa", "0600000000", "lea.martin@exemple.fr")
    assert client.montant_moyen_achat() == 0.0


def test_fiche_signaletique(rayon):
    vendeur = Vendeur("Benguigui", "Jean", "0624567267", "jean.benguigui@exemple.fr",
                      date(2024, 9, 1), 3, rayon)
    vendeur.montant_ventes = 150.0
    fiche = vendeur.fiche_signaletique()
    for champ in ("Benguigui", "Jean", "0624567267", "jean.benguigui@exemple.fr", "150.00"):
        assert champ in fiche


def test_afficher(capsys):
    client = Client("Martin", "Léa", "0600000000", "lea.martin@exemple.fr")
    client.afficher()
    sortie = capsys.readouterr().out
    for champ in ("Martin", "Léa", "0600000000", "lea.martin@exemple.fr"):
        assert champ in sortie
