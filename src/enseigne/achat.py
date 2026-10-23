"""
Classe : Achat
Module : achat.py
Description : Un achat d'un produit par un client
"""
from produit import Produit

class Achat():
  """ Un achat concerne un produit, en une certaine quantite """
  def __init__(self, aProduit, aQuantite):
    """Constructeur avec passage des valeurs pour les attributs"""
    self.produit = aProduit
    self.quantite = aQuantite

  def __str__(self):
    """ Methode pour l'affichage de la classe """
    chaine = "Achat" + "\n"
    chaine = chaine + "produit=" + str(self.produit.nom) + "\n"
    chaine = chaine + "quantite=" + str(self.quantite) + "\n"
    chaine = chaine + "montant=" + str(self.getMontant()) + "\n"
    return chaine

  def getMontant(self):
    """ Calcule le montant de l'achat """
    return self.produit.getPrix() * self.quantite

  def getProduit(self):
    """ Renvoie le produit achete """
    return self.produit

if __name__ == '__main__':
  """ Permet d'executer le code localement """
  maRaquette = Produit("Raquette", 89.90, "Tennis")
  monAchat = Achat(maRaquette, 2)
  print(monAchat)
