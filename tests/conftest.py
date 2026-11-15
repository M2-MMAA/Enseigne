"""Fixtures partagées par les tests : un petit graphe complet du modèle."""

from __future__ import annotations

from datetime import date, datetime
from types import SimpleNamespace

import pytest

from enseigne.achat import Achat
from enseigne.client import Client
from enseigne.enseigne import Enseigne
from enseigne.magasin import Magasin
from enseigne.produit import Produit
from enseigne.rayon import Rayon
from enseigne.secteur_activite import SecteurActivite
from enseigne.site_internet import SiteInternet
from enseigne.vendeur import Vendeur


@pytest.fixture
def graphe() -> SimpleNamespace:
    """Construit une enseigne, un magasin et son site, un secteur, deux rayons, deux vendeurs
    dont un responsable, deux produits et un client avec un achat.

    Returns:
        Les objets du graphe, accessibles par leur nom.
    """
    enseigne = Enseigne("Sport+")
    site = SiteInternet("https://www.sport-lyon.fr")
    magasin = Magasin("Sport Lyon", "Lyon", site)
    enseigne.ajouter_magasin(magasin)
    secteur = SecteurActivite("Raquettes")
    magasin.ajouter_secteur(secteur)
    rayon_tennis = Rayon("Tennis")
    rayon_badminton = Rayon("Badminton")
    secteur.ajouter_rayon(rayon_tennis)
    secteur.ajouter_rayon(rayon_badminton)
    jean = Vendeur("Benguigui", "Jean", "0624567267", "jean.benguigui@exemple.fr",
                   date(2024, 9, 1), 3, rayon_tennis)
    paul = Vendeur("Durand", "Paul", "0611223344", "paul.durand@exemple.fr",
                   date(2025, 1, 6), 2, rayon_badminton)
    secteur.ajouter_vendeur(jean)
    secteur.ajouter_vendeur(paul)
    secteur.responsable = jean
    raquette = Produit("P001", "Raquette", 89.90, rayon_tennis)
    volant = Produit("P002", "Volant", 12.50, rayon_badminton)
    lea = Client("Martin", "Léa", "0600000000", "lea.martin@exemple.fr")
    achat = Achat(raquette, 2, datetime(2026, 11, 15, 10, 30))
    lea.ajouter_achat(achat)
    enseigne.ajouter_client(lea)
    return SimpleNamespace(
        enseigne=enseigne, site=site, magasin=magasin, secteur=secteur,
        rayon_tennis=rayon_tennis, rayon_badminton=rayon_badminton,
        jean=jean, paul=paul, raquette=raquette, volant=volant, lea=lea, achat=achat,
    )
