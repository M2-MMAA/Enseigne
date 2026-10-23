"""
Classe : Client
Module : client.py
Description : Un client et ses achats
"""
class Client():
  """ Un client fait un ou plusieurs achats """
  def __init__(self, aNom, aPrenom):
    """Constructeur avec passage des valeurs pour les attributs"""
    self.nom = aNom
    self.prenom = aPrenom
    self.achats = []

  def __str__(self):
    """ Methode pour l'affichage de la classe """
    chaine = "Client" + "\n"
    chaine = chaine + "nom=" + str(self.nom) + "\n"
    chaine = chaine + "prenom=" + str(self.prenom) + "\n"
    chaine = chaine + "nombre d'achats=" + str(len(self.achats)) + "\n"
    return chaine

  def ajouterAchat(self, aAchat):
    """ Ajoute un achat au client """
    self.achats.append(aAchat)

  def montantMoyen(self):
    """ Calcule le montant moyen d'achat du client """
    if len(self.achats) == 0:
      return 0
    total = 0
    for achat in self.achats:
      total = total + achat.getMontant()
    return total / len(self.achats)

if __name__ == '__main__':
  """ Permet d'executer le code localement """
  monClient = Client("Martin", "Lea")
  print(monClient)
  print(monClient.montantMoyen())
