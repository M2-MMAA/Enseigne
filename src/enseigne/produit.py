"""
Classe : Produit
Module : enseigne.produit
Description : Produit proposé dans un rayon.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enseigne.rayon import Rayon


class Produit:
    """Produit proposé dans un rayon.

    Attributes:
        code: Code du produit.
        libelle: Libellé du produit.
        prix: Prix unitaire en euros.
        rayon: Rayon qui propose le produit.
    """

    def __init__(self, code: str, libelle: str, prix: float, rayon: Rayon) -> None:
        """Construit le produit et l'ajoute aux produits de son rayon.

        Args:
            code: Code du produit.
            libelle: Libellé du produit.
            prix: Prix unitaire en euros.
            rayon: Rayon qui propose le produit.
        """
        self.code = code
        self.libelle = libelle
        self.prix = prix
        self.rayon = rayon
        rayon.ajouter_produit(self)

    def __str__(self) -> str:
        """Renvoie le code, le libellé, le prix et le rayon du produit.

        Returns:
            Une description courte du produit.
        """
        return f"Produit {self.code} {self.libelle} : {self.prix:.2f} € (rayon {self.rayon.nom})"


if __name__ == "__main__":
    from enseigne.rayon import Rayon

    rayon_tennis = Rayon("Tennis")
    raquette = Produit("P001", "Raquette", 89.90, rayon_tennis)
    print(raquette)
    print(rayon_tennis)
