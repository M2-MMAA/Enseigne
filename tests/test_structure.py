"""Tests de structure : les classes et leurs associations suivent doc/class.mmd."""

from __future__ import annotations

import importlib
from datetime import date

import pytest

from enseigne.client import Client
from enseigne.personne import Personne
from enseigne.vendeur import Vendeur

MODULES = [
    "enseigne",
    "enseigne.enseigne",
    "enseigne.magasin",
    "enseigne.site_internet",
    "enseigne.secteur_activite",
    "enseigne.rayon",
    "enseigne.produit",
    "enseigne.personne",
    "enseigne.vendeur",
    "enseigne.client",
    "enseigne.achat",
]


@pytest.mark.parametrize("nom_module", MODULES)
def test_module_importable(nom_module):
    importlib.import_module(nom_module)


def test_noms_des_associations(graphe):
    g = graphe
    assert g.enseigne.magasins == [g.magasin]
    assert g.enseigne.clients == [g.lea]
    assert g.magasin.site_internet is g.site
    assert g.magasin.secteurs == [g.secteur]
    assert g.secteur.rayons == [g.rayon_tennis, g.rayon_badminton]
    assert g.secteur.vendeurs == [g.jean, g.paul]
    assert g.secteur.responsable is g.jean
    assert g.rayon_tennis.produits == [g.raquette]
    assert g.rayon_badminton.produits == [g.volant]
    assert g.rayon_tennis.vendeur is g.jean
    assert g.rayon_badminton.vendeur is g.paul
    assert g.jean.rayon is g.rayon_tennis
    assert g.paul.rayon is g.rayon_badminton
    assert g.raquette.rayon is g.rayon_tennis
    assert g.volant.rayon is g.rayon_badminton
    assert g.lea.achats == [g.achat]
    assert g.achat.produit is g.raquette


def test_vendeur_et_client_heritent_de_personne():
    assert issubclass(Vendeur, Personne)
    assert issubclass(Client, Personne)


def test_personne_non_instanciable():
    with pytest.raises(TypeError):
        Personne("Martin", "Léa", "0600000000", "lea.martin@exemple.fr")


def test_deuxieme_vendeur_sur_un_rayon(graphe):
    with pytest.raises(ValueError):
        Vendeur("Petit", "Marc", "0699887766", "marc.petit@exemple.fr",
                date(2025, 3, 3), 1, graphe.rayon_tennis)
    assert graphe.rayon_tennis.vendeur is graphe.jean


def test_responsable_hors_des_vendeurs_du_secteur(graphe):
    secteur = graphe.secteur
    secteur.vendeurs.remove(graphe.paul)
    with pytest.raises(ValueError):
        secteur.responsable = graphe.paul
    assert secteur.responsable is graphe.jean
