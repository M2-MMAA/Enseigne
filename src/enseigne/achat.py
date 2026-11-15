"""
Classe : Achat
Module : enseigne.achat
Description : Achat d'un produit par un client, en une certaine quantité.
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from enseigne.produit import Produit


class Achat:
    """Achat d'un produit, en une certaine quantité, à une date donnée.

    Attributes:
        quantite: Nombre d'exemplaires achetés.
        date: Date et heure de l'achat.
        produit: Produit acheté.
    """

    def __init__(self, produit: Produit, quantite: int, date: Optional[datetime] = None) -> None:
        """Construit l'achat.

        Args:
            produit: Produit acheté.
            quantite: Nombre d'exemplaires achetés.
            date: Date et heure de l'achat ; maintenant si elle n'est pas donnée.
        """
        self.produit = produit
        self.quantite = quantite
        self.date = date if date is not None else datetime.now()

    def montant(self) -> float:
        """Calcule le montant de l'achat.

        Returns:
            Le montant de l'achat (prix du produit × quantité), en euros.
        """
        return self.produit.prix * self.quantite

    def __str__(self) -> str:
        """Renvoie le produit, la quantité, la date et le montant de l'achat.

        Returns:
            Une description courte de l'achat.
        """
        return (
            f"Achat de {self.quantite} × {self.produit.libelle} le {self.date:%d/%m/%Y %H:%M} "
            f"(montant : {self.montant():.2f} €)"
        )


if __name__ == "__main__":
    from enseigne.produit import Produit
    from enseigne.rayon import Rayon

    rayon_tennis = Rayon("Tennis")
    raquette = Produit("P001", "Raquette", 89.90, rayon_tennis)
    achat = Achat(raquette, 2, datetime(2026, 11, 15, 10, 30))
    print(achat)
