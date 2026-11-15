"""
Classe : SecteurActivite
Module : enseigne.secteur_activite
Description : Secteur d'activité d'un magasin, avec ses rayons, ses vendeurs et son responsable.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from enseigne.rayon import Rayon
    from enseigne.vendeur import Vendeur


class SecteurActivite:
    """Secteur d'activité d'un magasin.

    Attributes:
        nom: Nom du secteur.
        rayons: Rayons du secteur.
        vendeurs: Vendeurs du secteur.
        responsable: Vendeur responsable du secteur, pris parmi ``vendeurs`` ;
            ``None`` tant qu'il n'est pas affecté.
    """

    def __init__(self, nom: str) -> None:
        """Construit le secteur, sans rayon, sans vendeur ni responsable.

        Args:
            nom: Nom du secteur.
        """
        self.nom = nom
        self.rayons: List[Rayon] = []
        self.vendeurs: List[Vendeur] = []
        self._responsable: Optional[Vendeur] = None

    @property
    def responsable(self) -> Optional[Vendeur]:
        """Vendeur responsable du secteur, ``None`` tant qu'il n'est pas affecté.

        Raises:
            ValueError: À l'affectation, si le vendeur ne fait pas partie de
                ``vendeurs``.
        """
        return self._responsable

    @responsable.setter
    def responsable(self, vendeur: Vendeur) -> None:
        if vendeur not in self.vendeurs:
            raise ValueError(f"{vendeur} ne fait pas partie des vendeurs du secteur {self.nom}")
        self._responsable = vendeur

    def ajouter_rayon(self, rayon: Rayon) -> None:
        """Ajoute un rayon au secteur.

        Args:
            rayon: Rayon du secteur.
        """
        self.rayons.append(rayon)

    def ajouter_vendeur(self, vendeur: Vendeur) -> None:
        """Ajoute un vendeur au secteur.

        Args:
            vendeur: Vendeur du secteur.
        """
        self.vendeurs.append(vendeur)

    def montant_total(self) -> float:
        """Calcule le montant total des ventes du secteur.

        Returns:
            Le montant total des ventes du secteur, en euros.

        Raises:
            NotImplementedError: Méthode pas encore écrite.
        """
        raise NotImplementedError("code en cours")

    def __str__(self) -> str:
        """Renvoie le nom du secteur, ses effectifs et son responsable.

        Returns:
            Une description courte du secteur.
        """
        responsable = (
            f"{self.responsable.prenom} {self.responsable.nom}" if self.responsable else "aucun"
        )
        return (
            f"Secteur {self.nom} ({len(self.rayons)} rayon(s), "
            f"{len(self.vendeurs)} vendeur(s), responsable : {responsable})"
        )


if __name__ == "__main__":
    from datetime import date

    from enseigne.rayon import Rayon
    from enseigne.vendeur import Vendeur

    secteur = SecteurActivite("Cyclisme")
    rayon_vtt = Rayon("VTT")
    secteur.ajouter_rayon(rayon_vtt)
    vendeur = Vendeur(
        "Benguigui", "Jean", "0624567267", "jean.benguigui@exemple.fr", date(2024, 9, 1), 3, rayon_vtt
    )
    secteur.ajouter_vendeur(vendeur)
    secteur.responsable = vendeur
    print(secteur)
