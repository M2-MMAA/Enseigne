class SiteInternet:
    """Classe représentant le site internet d'un magasin."""

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return "Site internet : " + self.url


if __name__ == "__main__":
    site = SiteInternet("https://www.monmagasin.fr")
    print(site)
