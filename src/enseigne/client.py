"""
Classe : Client
Module : enseigne.client
Description : Client de l'enseigne et ses achats.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from enseigne.personne import Personne

if TYPE_CHECKING:
    from enseigne.achat import Achat
    from enseigne.produit import Produit


class Client(Personne):
    """Client de l'enseigne.

    Attributes:
        achats: Achats faits par le client.
    """

    def __init__(self, nom: str, prenom: str, tel: str, mail: str) -> None:
        """Construit le client, sans achat.

        Args:
            nom: Nom du client.
            prenom: Prénom du client.
            tel: Numéro de téléphone.
            mail: Adresse électronique.
        """
        super().__init__(nom, prenom, tel, mail)
        self.achats: List[Achat] = []

    def ajouter_achat(self, achat: Achat) -> None:
        """Ajoute un achat aux achats du client.

        Args:
            achat: Achat fait par le client.
        """
        self.achats.append(achat)

    def acheter(self, produit: Produit, quantite: int) -> Achat:
        """Fait acheter un produit au client.

        Args:
            produit: Produit acheté.
            quantite: Nombre d'exemplaires achetés.

        Returns:
            L'achat créé.

        Raises:
            NotImplementedError: Méthode pas encore écrite.
        """
        raise NotImplementedError("code en cours")

    def montant_moyen_achat(self) -> float:
        """Calcule le montant moyen des achats du client.

        Returns:
            Le montant moyen d'un achat, en euros ; ``0.0`` si le client n'a rien acheté.
        """
        if not self.achats:
            return 0.0
        total = sum(achat.montant() for achat in self.achats)
        return total / len(self.achats)

    def __str__(self) -> str:
        """Renvoie le nom du client et son nombre d'achats.

        Returns:
            Une description courte du client.
        """
        return f"Client {self.prenom} {self.nom} ({len(self.achats)} achat(s))"


if __name__ == "__main__":
    from enseigne.achat import Achat
    from enseigne.produit import Produit
    from enseigne.rayon import Rayon

    rayon_tennis = Rayon("Tennis")
    raquette = Produit("P001", "Raquette", 89.90, rayon_tennis)
    client = Client("Martin", "Léa", "0600000000", "lea.martin@exemple.fr")
    client.ajouter_achat(Achat(raquette, 1))
    client.ajouter_achat(Achat(raquette, 2))
    print(client)
    print(f"Montant moyen d'un achat : {client.montant_moyen_achat():.2f} €")
