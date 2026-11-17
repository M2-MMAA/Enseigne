# Enseigne
TD0 M2 MMAA INFO901 : Enseigne

## Description
Ce projet consiste à créer une application pour gérer une enseigne de matériel de sport disposant de plusieurs magasins en France. L'application permet de structurer les magasins en secteurs d'activités et en rayons, de gérer les vendeurs (affectation, suivi des ventes, fiches signalétiques) ainsi que les clients.

## Installation à partir d'un terminal

### Sur Linux et macOS
```bash
git clone https://github.com/M2-MMAA/Enseigne.git
cd Enseigne
python3 -m venv .venv          # Évite d'installer dans l'environnement global
source .venv/bin/activate      # Active l'environnement virtuel
pip install -e .               # Installe le projet et ses dépendances
```

### Sur Windows (PowerShell)
```powershell
git clone https://github.com/M2-MMAA/Enseigne.git
cd Enseigne
py -m venv .venv               # Évite d'installer dans l'environnement global (ou : python -m venv .venv)
.\.venv\Scripts\Activate.ps1   # Active l'environnement virtuel
pip install -e .               # Installe le projet et ses dépendances
```

> Si PowerShell refuse d'exécuter `Activate.ps1`, lancez une seule fois `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, puis réessayez.

## Utilisation

Après avoir suivi les étapes ci-dessus (environnement virtuel activé), exécutez la commande suivante :
```console
enseigne
```

## Affichage des diagrammes UML

Les diagrammes UML sont écrits dans le langage [Mermaid](https://mermaid.js.org/intro/).

Pour les visualiser directement dans votre navigateur à l'aide du script de documentation, exécutez les commandes suivantes depuis la racine du projet :

**Sur Linux et macOS :**
```bash
# Afficher le diagramme de classe
python3 ./doc/mermaid.py ./doc/class.mmd

# Afficher le diagramme de cas d'utilisation
python3 ./doc/mermaid.py ./doc/use_case.mmd

# Afficher le diagramme de séquence
python3 ./doc/mermaid.py ./doc/sequence.mmd
```

**Sur Windows (PowerShell) :**
```powershell
# Afficher le diagramme de classe
python ./doc/mermaid.py ./doc/class.mmd

# Afficher le diagramme de cas d'utilisation
python ./doc/mermaid.py ./doc/use_case.mmd

# Afficher le diagramme de séquence
python ./doc/mermaid.py ./doc/sequence.mmd
```

## Structure du projet
```text
Enseigne/
├── .github/
│   └── CODEOWNERS        # Responsables GitHub qui valident les Pull Requests
├── doc/                  # Documentation (Diagrammes UML Mermaid + script d'affichage)
├── src/
│   └── enseigne/
│       ├── __init__.py   # Fichier d'initialisation des modules
│       ├── __main__.py   # Fichier d'entrée de notre programme
│       ├── module1.py    # Classe 1
│       └── module2.py    # Classe 2
├── .gitattributes        # Normalisation des fins de ligne (LF dans le dépôt)
├── .gitignore            # Liste des fichiers et dossiers non suivis par Git
├── CONTRIBUTING.md       # Guide pour contribuer (branches, Pull Requests, problèmes fréquents)
├── LICENSE               # Conditions d'utilisation de votre projet
├── README.md             # Explication du projet
└── pyproject.toml        # Fichier de configuration
```

## Organisation des membres

| Rôle | Personnes |
|----------|-------------|
| GITHUB | Mathis, Josquin, Raoul |
| Dictionnaire | Jodie, Judith, Lilou, Anaïs |
| Diagramme UML (Use Case) | ???? |
| Diagramme UML (Séquence) | ???? |
| Diagramme UML (Classe) | Salihou + Mathis |
| Scrum Master |  Jodie + Séphora |
| Product Owner | Dimitri + Mathis |
| Programme principal | Josquin + Jodie |



| Classe | Personnes |
|----------|-------------|
| Vente | Anaïs |
| Client | Lilou |
| Achat| Séphora |
| Produit | Dimitri |
| ClasseMetier | Mathieu |
| Vendeur |  Assil |
| VendeurResponsable| Josquin |
| Rayon | Mathis |
| Activite | Yoliza |
| Magasin | Jodie |
| SiteInternet | Judith |



## Comment contribuer

> **Règle d'or :** on ne pousse jamais directement sur `main`. Chaque modification passe par une branche personnelle, puis par une Pull Request validée par un responsable GitHub.

Avant votre première contribution, lisez le guide **[CONTRIBUTING.md](CONTRIBUTING.md)** : il explique pas à pas comment préparer son poste, nommer sa branche et sa Pull Request, proposer ses modifications, et quoi faire en cas de problème.

## Livraisons

Chaque livraison est un **tag** posé sur `main` par les responsables GitHub à la date limite (`S42`, `S46`, `S50`…). Le code livré est consultable dans l'onglet **Releases** du dépôt, ou via le menu de sélection des branches et tags.

Une PR fusionnée après la date limite part simplement dans la livraison suivante.

## Conventions d'écriture du code
- Le nom des classes utilise le **PascalCase**.
- Les méthodes, fonctions et variables utilisent le **snake_case**.
- Un seul fichier par classe, et le nom du fichier sera en snake_case (exemple : pour la classe `SecteurActivite`, le fichier s'appellera `secteur_activite.py`).
- Les fonctions et méthodes seront typées et documentées en utilisant le standard PEP 8 de Python.

  Exemple :
  ```python
  """
  Classe : ClassTemplate
  Module : 
  Description : Permet d'avoir une ossature pour toutes mes classes
  """
  class ClassTemplate:
      def __init__(self, aValeurAttribut01: type1, aValeurAttribut02: type2) -> None:
          """Constructeur de la classe ClassTemplate.
              
          Args:
              aValeurAttribut01: Description de aValeurAttribut01.
              aValeurAttribut02: Description de aValeurAttribut02.
          """
          self.attribut01 = aValeurAttribut01
          self.attribut02 = aValeurAttribut02

      def __str__(self) -> str:
          chaine = "Ma manière d'afficher la classe ClassTemplate\n"
          chaine += "attribut01=" + str(self.attribut01) + "\n"
          chaine += "attribut02=" + str(self.attribut02) + "\n"
          return chaine

      def action01(self, aValeurParametrage01: type2, aValeurParametrage02: type3) -> None:
          """Description de l'action01.
              
          Args:
              aValeurParametrage01: Description de aValeurParametrage01.
              aValeurParametrage02: Description de aValeurParametrage02.
          """
          print(str(self.attribut01) + " action01 avec les paramètres " + str(aValeurParametrage01) + ", " + str(aValeurParametrage02))
  ```
