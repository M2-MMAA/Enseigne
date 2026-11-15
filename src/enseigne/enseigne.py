"""
Classe : Enseigne
Module : enseigne.enseigne
Description : Racine du modèle : l'enseigne, ses magasins et ses clients.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from enseigne.client import Client
    from enseigne.magasin import Magasin
    from enseigne.vendeur import Vendeur


class Enseigne:
    """Enseigne de matériel de sport, racine du modèle.

    Attributes:
        nom: Nom de l'enseigne.
        magasins: Magasins de l'enseigne.
        clients: Clients de l'enseigne.
    """

    def __init__(self, nom: str) -> None:
        """Construit l'enseigne, sans magasin ni client.

        Args:
            nom: Nom de l'enseigne.
        """
        self.nom = nom
        self.magasins: List[Magasin] = []
        self.clients: List[Client] = []

    def ajouter_magasin(self, magasin: Magasin) -> None:
        """Ajoute un magasin à l'enseigne.

        Args:
            magasin: Magasin de l'enseigne.
        """
        self.magasins.append(magasin)

    def ajouter_client(self, client: Client) -> None:
        """Ajoute un client à l'enseigne.

        Args:
            client: Client de l'enseigne.
        """
        self.clients.append(client)

    def liste_vendeurs(self) -> List[Vendeur]:
        """Liste les vendeurs de tous les magasins de l'enseigne.

        Returns:
            La liste des vendeurs.

        Raises:
            NotImplementedError: Méthode pas encore écrite.
        """
        raise NotImplementedError("code en cours")

    def montant_moyen_par_client(self) -> float:
        """Calcule le montant moyen des achats par client.

        Returns:
            Le montant moyen des achats par client, en euros.

        Raises:
            NotImplementedError: Méthode pas encore écrite.
        """
        raise NotImplementedError("code en cours")

    def __str__(self) -> str:
        """Renvoie le nom de l'enseigne et ses effectifs.

        Returns:
            Une description courte de l'enseigne.
        """
        return f"Enseigne {self.nom} ({len(self.magasins)} magasin(s), {len(self.clients)} client(s))"


if __name__ == "__main__":
    from datetime import date

    from enseigne.achat import Achat
    from enseigne.client import Client
    from enseigne.magasin import Magasin
    from enseigne.produit import Produit
    from enseigne.rayon import Rayon
    from enseigne.secteur_activite import SecteurActivite
    from enseigne.site_internet import SiteInternet
    from enseigne.vendeur import Vendeur

    enseigne = Enseigne("Sport+")
    magasin = Magasin("Sport Lyon", "Lyon", SiteInternet("https://www.sport-lyon.fr"))
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
    Produit("P002", "Volant", 12.50, rayon_badminton)
    lea = Client("Martin", "Léa", "0600000000", "lea.martin@exemple.fr")
    lea.ajouter_achat(Achat(raquette, 2))
    enseigne.ajouter_client(lea)
    print(enseigne)
    print(magasin)
    for rayon in secteur.rayons:
        print(f"  {rayon}")
    print(lea)
    print(f"  {lea.achats[0]}")
    jean.imprimer_fiche()
