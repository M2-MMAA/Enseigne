"""
Classe : Vendeur
Module : enseigne.vendeur
Description : Vendeur de l'enseigne, qui tient un rayon.
"""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from enseigne.personne import Personne

if TYPE_CHECKING:
    from enseigne.rayon import Rayon


class Vendeur(Personne):
    """Vendeur de l'enseigne, affecté à un seul rayon.

    Attributes:
        date_prise_fonction: Date de prise de fonction.
        indice_salaire: Indice dans la grille des salaires.
        montant_ventes: Montant cumulé des ventes, en euros.
        rayon: Rayon tenu par le vendeur.
    """

    def __init__(
        self,
        nom: str,
        prenom: str,
        tel: str,
        mail: str,
        date_prise_fonction: date,
        indice_salaire: int,
        rayon: Rayon,
    ) -> None:
        """Construit le vendeur et l'enregistre comme vendeur de son rayon.

        Args:
            nom: Nom du vendeur.
            prenom: Prénom du vendeur.
            tel: Numéro de téléphone.
            mail: Adresse électronique.
            date_prise_fonction: Date de prise de fonction.
            indice_salaire: Indice dans la grille des salaires.
            rayon: Rayon tenu par le vendeur.

        Raises:
            ValueError: Si le rayon a déjà un vendeur.
        """
        if rayon.vendeur is not None:
            raise ValueError(f"Le rayon {rayon.code_rayon} a déjà un vendeur")
        super().__init__(nom, prenom, tel, mail)
        self.date_prise_fonction = date_prise_fonction
        self.indice_salaire = indice_salaire
        self.montant_ventes: float = 0.0
        self.rayon = rayon
        rayon.vendeur = self

    def ajouter_vente(self, montant: float) -> None:
        """Ajoute le montant d'une vente au cumul des ventes du vendeur.

        Args:
            montant: Montant de la vente, en euros.

        Raises:
            NotImplementedError: Méthode pas encore écrite.
        """
        raise NotImplementedError("code en cours")

    def montant_total(self) -> float:
        """Renvoie le montant total des ventes du vendeur.

        Returns:
            Le montant total des ventes, en euros.

        Raises:
            NotImplementedError: Méthode pas encore écrite.
        """
        raise NotImplementedError("code en cours")

    def fiche_signaletique(self) -> str:
        """Construit la fiche signalétique du vendeur.

        Returns:
            Le texte de la fiche : nom, prénom, téléphone, mail et montant des ventes.
        """
        return (
            f"Vendeur : {self.prenom} {self.nom}\n"
            f"  - Tél : {self.tel}\n"
            f"  - Mail : {self.mail}\n"
            f"  - Montant des ventes : {self.montant_ventes:.2f} €"
        )

    def imprimer_fiche(self) -> None:
        """Affiche la fiche signalétique du vendeur."""
        print(self.fiche_signaletique())

    def __str__(self) -> str:
        """Renvoie le nom du vendeur et le rayon qu'il tient.

        Returns:
            Une description courte du vendeur.
        """
        return f"Vendeur {self.prenom} {self.nom} (rayon {self.rayon.code_rayon} {self.rayon.nom})"


if __name__ == "__main__":
    from enseigne.rayon import Rayon

    rayon_vtt = Rayon("VTT")
    vendeur = Vendeur(
        "Benguigui", "Jean", "0624567267", "jean.benguigui@exemple.fr", date(2024, 9, 1), 3, rayon_vtt
    )
    print(vendeur)
    print(rayon_vtt)
    vendeur.imprimer_fiche()
