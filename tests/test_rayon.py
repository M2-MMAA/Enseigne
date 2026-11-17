"""Tests du compteur de rayons (incrémenté au constructeur, décrémenté par __del__)."""

from __future__ import annotations

import gc

from enseigne.rayon import Rayon


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
