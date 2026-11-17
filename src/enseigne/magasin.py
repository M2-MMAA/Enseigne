"""
Classe : Magasin
Module : enseigne.magasin
Description : Magasin de l'enseigne, structuré en secteurs d'activité et doté d'un site Internet.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from enseigne.secteur_activite import SecteurActivite
    from enseigne.site_internet import SiteInternet


class Magasin:
    """Magasin de l'enseigne.

    Attributes:
        nom: Nom du magasin.
        ville: Ville du magasin.
        site_internet: Site Internet du magasin.
        secteurs: Secteurs d'activité du magasin.
    """

    def __init__(self, nom: str, ville: str, site_internet: SiteInternet) -> None:
        """Construit le magasin, sans secteur d'activité.

        Args:
            nom: Nom du magasin.
            ville: Ville du magasin.
            site_internet: Site Internet du magasin.
        """
        self.nom = nom
        self.ville = ville
        self.site_internet = site_internet
        self.secteurs: List[SecteurActivite] = []

    def ajouter_secteur(self, secteur: SecteurActivite) -> None:
        """Ajoute un secteur d'activité au magasin.

        Args:
            secteur: Secteur d'activité du magasin.
        """
        self.secteurs.append(secteur)

    def __str__(self) -> str:
        """Renvoie le nom, la ville, le site et les secteurs du magasin.

        Returns:
            Une description du magasin sur plusieurs lignes.
        """
        lignes = [f"Magasin {self.nom} ({self.ville})", f"  {self.site_internet}"]
        lignes += [f"  - {secteur}" for secteur in self.secteurs]
        return "\n".join(lignes)


if __name__ == "__main__":
    from enseigne.secteur_activite import SecteurActivite
    from enseigne.site_internet import SiteInternet

    magasin = Magasin("Sport Lyon", "Lyon", SiteInternet("https://www.sport-lyon.fr"))
    magasin.ajouter_secteur(SecteurActivite("Running"))
    magasin.ajouter_secteur(SecteurActivite("Randonnée"))
    print(magasin)
