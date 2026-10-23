"""
Classe : Produit
Module : produit.py
Description : Un produit vendu dans un rayon
"""
class Produit():
  """ Un produit avec son prix, il se trouve dans un rayon """
  def __init__(self, aNom, aPrix, aRayon):
    """Constructeur avec passage des valeurs pour les attributs"""
    self.nom = aNom
    self.prix = aPrix
    self.rayon = aRayon

  def __str__(self):
    """ Methode pour l'affichage de la classe """
    chaine = "Produit" + "\n"
    chaine = chaine + "nom=" + str(self.nom) + "\n"
    chaine = chaine + "prix=" + str(self.prix) + "\n"
    chaine = chaine + "rayon=" + str(self.rayon) + "\n"
    return chaine

  def getPrix(self):
    """ Renvoie le prix du produit """
    return self.prix

  def getRayon(self):
    """ Renvoie le rayon du produit """
    return self.rayon

if __name__ == '__main__':
  """ Permet d'executer le code localement """
  monProduit = Produit("Raquette", 89.90, "Tennis")
  print(monProduit)
  print(monProduit.getPrix())
