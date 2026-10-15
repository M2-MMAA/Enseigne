from abc import ABC


class Personne(ABC):
    """Classe abstraite : regroupe ce que Vendeur et Client ont en commun."""

    def __init__(self, nom, prenom, tel, mail):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail

    def afficher(self):
        """Affiche les informations de la personne."""
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Téléphone : {self.tel}")
        print(f"Mail : {self.mail}")

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# Exemple d'utilisation par les autres classes :
#
# from personne import Personne
#
# class Vendeur(Personne):
#     def __init__(self, nom, prenom, tel, mail, date_prise_fonction, indice_grille_salaire):
#         super().__init__(nom, prenom, tel, mail)
#         self.date_prise_fonction = date_prise_fonction
#         self.indice_grille_salaire = indice_grille_salaire
#         self.montant_ventes = 0
