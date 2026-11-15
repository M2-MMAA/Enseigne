"""Les méthodes de calcul restent des bouchons : chacune lève NotImplementedError.

Chaque cas sera remplacé par de vrais tests quand la méthode sera écrite.
"""

from __future__ import annotations

import pytest

BOUCHONS = {
    "Client.acheter": lambda g: g.lea.acheter(g.volant, 1),
    "Vendeur.ajouter_vente": lambda g: g.jean.ajouter_vente(10.0),
    "Vendeur.montant_total": lambda g: g.jean.montant_total(),
    "Rayon.montant_total": lambda g: g.rayon_tennis.montant_total(),
    "SecteurActivite.montant_total": lambda g: g.secteur.montant_total(),
    "Enseigne.liste_vendeurs": lambda g: g.enseigne.liste_vendeurs(),
    "Enseigne.montant_moyen_par_client": lambda g: g.enseigne.montant_moyen_par_client(),
}


@pytest.mark.parametrize("appel", BOUCHONS.values(), ids=BOUCHONS.keys())
def test_bouchon(graphe, appel):
    with pytest.raises(NotImplementedError):
        appel(graphe)
