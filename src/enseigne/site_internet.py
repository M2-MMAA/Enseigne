"""
Classe : SiteInternet
Module : enseigne.site_internet
Description : Site Internet d'un magasin, dont l'URL est validée à la construction.
"""

from __future__ import annotations

from urllib.parse import urlparse


class SiteInternet:
    """Site Internet d'un magasin.

    Attributes:
        url: Adresse du site, de schéma ``http`` ou ``https``.
    """

    def __init__(self, url: str) -> None:
        """Construit le site après avoir validé son URL.

        Args:
            url: Adresse du site, par exemple ``https://www.exemple.fr``.

        Raises:
            ValueError: Si l'URL n'est pas une chaîne de schéma ``http`` ou ``https``
                avec un nom d'hôte non vide.
        """
        if not isinstance(url, str):
            raise ValueError(f"URL invalide : {url!r} n'est pas une chaîne")
        decoupage = urlparse(url)
        if decoupage.scheme not in ("http", "https"):
            raise ValueError(f"URL invalide : {url!r} (schéma http ou https attendu)")
        if not decoupage.hostname:
            raise ValueError(f"URL invalide : {url!r} (nom d'hôte manquant)")
        self.url = url

    def __str__(self) -> str:
        """Renvoie l'URL du site.

        Returns:
            Le texte « Site Internet : url ».
        """
        return f"Site Internet : {self.url}"


if __name__ == "__main__":
    site = SiteInternet("https://www.sport-lyon.fr")
    print(site)
    try:
        SiteInternet("sport-lyon.fr")
    except ValueError as erreur:
        print(erreur)
