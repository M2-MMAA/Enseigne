"""
Classe : Vente
Module : Vente
Description : Vente d'un produit à un client par un vendeur
"""

class Vente:

  def __init__(self, aClient, aProduit, aVendeur, aMontant):
    self.client = aClient
    self.produit = aProduit
    self.vendeur = aVendeur
    self.montant = aMontant

  def __str__(self):
    chaine = "Vente :"
    chaine += "\n  Client : " + str(self.client)
    chaine += "\n  Produit : " + str(self.produit)
    chaine += "\n  Vendeur : " + str(self.vendeur)
    chaine += "\n  Montant : " + str(self.montant) + " euros"
    return chaine

  def getClient(self):
    return self.client

  def getProduit(self):
    return self.produit

  def getVendeur(self):
    return self.vendeur

  def getMontant(self):
    return self.montant


if __name__ == '__main__':
  v1 = Vente("Dupont", "Raquette de tennis", "Martin", 89.90)
  v2 = Vente("Durand", "Ballon de foot", "Martin", 24.50)
  print(v1)
  print(v2)
  print("Total Martin :", v1.getMontant() + v2.getMontant())
