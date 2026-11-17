"""
Classe : Personne
Module : enseigne.personne
Description : Classe abstraite regroupant ce que Vendeur et Client ont en commun.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Personne(ABC):
    """Personne de l'enseigne (classe abstraite) : un vendeur ou un client.

    Attributes:
        nom: Nom de la personne.
        prenom: Prénom de la personne.
        tel: Numéro de téléphone.
        mail: Adresse électronique.
    """

    @abstractmethod
    def __init__(self, nom: str, prenom: str, tel: str, mail: str) -> None:
        """Initialise les attributs communs à toutes les personnes.

        Ce constructeur est abstrait : ``Personne(...)`` lève ``TypeError``. Chaque
        sous-classe définit son propre ``__init__`` et appelle ``super().__init__``.

        Args:
            nom: Nom de la personne.
            prenom: Prénom de la personne.
            tel: Numéro de téléphone.
            mail: Adresse électronique.
        """
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail

    def afficher(self) -> None:
        """Affiche les informations de la personne, une par ligne."""
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Téléphone : {self.tel}")
        print(f"Mail : {self.mail}")

    def __str__(self) -> str:
        """Renvoie le prénom et le nom de la personne.

        Returns:
            Le texte « prénom nom ».
        """
        return f"{self.prenom} {self.nom}"


if __name__ == "__main__":
    from enseigne.client import Client

    try:
        Personne("Martin", "Léa", "0600000000", "lea.martin@exemple.fr")  # type: ignore[abstract]
    except TypeError as erreur:
        print(f"Personne n'est pas instanciable : {erreur}")
    client = Client("Martin", "Léa", "0600000000", "lea.martin@exemple.fr")
    print(f"Une personne concrète (Client) : {client}")
    client.afficher()
