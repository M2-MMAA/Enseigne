"""
Classe : Activités
Module : enseigne.activite
Description : Représente un secteur d'activité spécifique au sein d'une enseigne.
"""

from datetime import datetime, timezone

from enseigne.rayon import Rayon
from enseigne.vendeur import Vendeur


class SecteurActivite:
    def __init__(self, nom: str, rayons: Rayon, listevendeurs: list[Vendeur]) -> None:
        """Constructeur de la classe Activite.
        Args:
            nom: Nom du secteur d'activité
            rayons: Liste des rayons
            listevendeurs: Liste des vendeurs
        """
        self.rayons = rayons
        self.listevendeurs = listevendeurs
        self.nom = nom

    def __str__(self) -> str:
        return (
            f"nom = {self.nom}, rayons = {self.rayons}, vendeurs = {self.listevendeurs}"
        )


if __name__ == "__main__":
    r1 = Rayon(nom="VTT")
    r1 = Rayon("VTT")
    v1 = Vendeur(
        prenom="Jean",
        nom="Benguigui",
        tel="0624567267",
        email="Benguigui@gmail.com",
        prise_fonction=datetime.now(tz=timezone.utc),
        rayon=r1,
        indice_salaire=1,
    )

    a1 = SecteurActivite(nom="Hand", rayons=r1, listevendeurs=[v1])
    print(a1)
