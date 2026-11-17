"""
Classe : Rayon
Module : enseigne.rayon
Description : Rayon d'un secteur d'activité, tenu par un vendeur et proposant des produits.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enseigne.produit import Produit
    from enseigne.vendeur import Vendeur


class Rayon:
    """Rayon d'un secteur d'activité.

    Attributes:
        compteur: Nombre de rayons existants (attribut de classe).
        code_rayon: Code du rayon, tiré du compteur (``RAY-001``, ``RAY-002``…).
        nom: Nom du rayon.
        produits: Produits proposés dans le rayon.
        vendeur: Vendeur qui tient le rayon, ``None`` tant qu'il n'est pas affecté.
    """

    compteur: int = 0

    def __init__(self, nom: str) -> None:
        """Construit le rayon, incrémente le compteur et en tire le code du rayon.

        Args:
            nom: Nom du rayon (Football, Natation…).
        """
        Rayon.compteur += 1
        self.code_rayon : str = f"RAY-{Rayon.compteur:03d}"
        self.nom = nom
        self.produits: list[Produit] = []      # rempli par Produit.__init__
        self.vendeur: Vendeur | None = None    # rempli par Vendeur.__init__


    def __del__(self) -> None:
        """Décrémente le compteur de rayons à la destruction du rayon.

        En Python, ``__del__`` n'est pas appelé à un moment garanti : il l'est quand
        l'objet est libéré, ce qui peut être différé (cycles de références, autre
        implémentation que CPython) ou ne jamais arriver avant la fin du programme.
        On passe par ``type(self)`` et non par le nom global ``Rayon``, qui peut déjà
        être effacé à la fin du programme.
        """
        type(self).compteur -= 1

    def ajouter_produit(self, produit: Produit) -> None:
        """Ajoute un produit au rayon.

        Args:
            produit: Produit proposé dans le rayon.
        """
        if produit.rayon is not self:
               raise ValueError(f"{produit.code} appartient au rayon {produit.rayon.nom}")
        if produit not in self.produits:
            self.produits.append(produit)

    def montant_total(self) -> float:
        """Calcule le montant total des ventes du rayon.

        Returns:
            Le montant total des ventes du rayon.
        """
        if self.vendeur:
            return self.vendeur.montant_total()
        else:
            return 0.0

    def __str__(self) -> str:
        """Renvoie le code, le nom et le vendeur du rayon.

        Returns:
            Une description courte du rayon.
        """
        vendeur_str = (
            f"{self.vendeur.prenom} {self.vendeur.nom}" if self.vendeur else "aucun"
        )
        return (
            f"Rayon {self.code_rayon} {self.nom} "
            f"({len(self.produits)} produit(s), vendeur : {vendeur_str})"
        )


if __name__ == "__main__":
    from enseigne.produit import Produit

    rayon_tennis = Rayon("Tennis")

    raquette = Produit("P001", "Raquette Pro Carbon", 120.00, rayon_tennis)
    tubes_balles = Produit("P002", "Tube de 4 balles de tennis", 15.50, rayon_tennis)

    print(rayon_tennis)
    print(f"Compteur : {Rayon.compteur}")
    del rayon_tennis
    print(f"Compteur après suppression d'un rayon : {Rayon.compteur}")
