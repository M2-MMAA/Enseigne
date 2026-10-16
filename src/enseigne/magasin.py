"""
Classe : Magasin
Module : magasin
Description : Magasin de l'enseigne, structuré en secteurs d'activités et possédant un site Internet
"""

class Magasin:

  def __init__(self, aNom, aSiteInternet):
    self.nom = aNom
    self.siteInternet = aSiteInternet
    self.activites = []

  def __str__(self):
    chaine = "Magasin : " + str(self.nom)
    chaine += "\n  Site Internet : " + str(self.siteInternet)
    chaine += "\n  Secteurs d'activités :"
    for activite in self.activites:
      chaine += "\n    - " + str(activite)
    return chaine

  def getNom(self):
    return self.nom

  def getSiteInternet(self):
    return self.siteInternet

  def getActivites(self):
    return self.activites

  def ajouterActivite(self, aActivite):
    self.activites.append(aActivite)


if __name__ == '__main__':
  m = Magasin("Sport Lyon", "www.sportlyon.fr")
  m.ajouterActivite("Running")
  m.ajouterActivite("Randonnée")
  print(m)
  print(len(m.getActivites()), "secteurs")
