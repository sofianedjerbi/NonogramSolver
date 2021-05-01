# nonogram.py - Sofiane DJERBI & Salem HAFTARI
""" CONVENTIONS
 | Les nonogrammes donnent les informations en partant du haut et de la gauche.
 | row[x], col[y] : infos de la case en position x,y (Coordonnées matricielles)
"""
import pickle
from util.logic import NNGFormula
from util.graphics import Graphics


def _convert(n, c, d=0, prec=[]): # O(t) avec t la taille de l'arbre construit
    """ CALCULE LES COMBINAISONS POSSIBLES PAR LIGNE
    Paramètres:
        - n: Taille de la ligne/colonne
        - c: Les coefficients
    Retourne:
        - Une liste avec le nombre d'espaces possibles entre chaque coefficient
    """
    l = list(range(d, n - sum(c) - len(c) + 2)) # Case maximale accessible
    if len(c) == 1:
        for i in l:
            yield prec + [i] # On ne s'arrête pas
    else:
        # d = 1 : On est obligé d'avoir au minimum une case d'écart
        # n-i-c[0] : On enlève les cases prises par le premier coef
        # Cette ligne construit les arbres des possibilités
        for i in l:
            yield from _convert(n-i-c[0], c[1:], 1, prec + [i])


def convert(n, c): # O(n^3) + O(t) avec n le nombre de coef par ligne et O(t) la complexité de _convert
    """ WRAPPER POUR CONVERT, RETOURNE DES DONNEES EXPLOITABLES
    Paramètres:
        - n: Taille de la ligne/colonne
        - c: Les coefficients
    Retourne:
        - Une liste comprise dans le produit cartésien {1, -1}^n
    """
    c = [i for i in c if i != 0] # On enleve les 0
    if len(c) == 0: # Si aucun coef, tout est rogné
        yield [-1]*n
        return
    for x in _convert(n, c): # Parcours des configurations
        l = [-1]*n # Tout invalide par défaut, on rend ca valide après
        pos = 0 # pos de départ des 1
        for y, z in zip(c, x): # y = parcours du coefficient, z = espace précédents associés
            l[pos+z:pos+z+y] = [1]*y # On fixe les cases avant et on avance du coefficient
            pos = pos+z+y
        yield l


class Nonogram:
    """ NONOGRAMME
    Cet objet représente un nonogramme.
    Variables:
        - x, y: Taille du nonogramme
        - name: Nom du nonogramme
        - row: Informations des lignes du nonogramme
        - col: Informations des colonnes du nonogramme
        - colors: Le nonogramme est-il en couleur ? (Booléen)
        - formula: Formule logique correspondant au booléen (FND/FNC)
    """
    def __init__(self, size=(0,0), row=[], col=[],
                 name="", colors=False, formula=None): # O(1)
        """ INITIALISATION
        Paramètres:
            - x,y: Taile du nonogramme
            - name: Nom du nonogramme
            - row: Informations des lignes du nonogramme
            - col: Informations des colonnes du nonogramme
            - colors: Le nonogramme est-il en couleur (Booléen)
            - formula: Formule logique associée au nonogramme
            - solution: Solution du nonogramme
        """
        self.y, self.x = size
        self.name = name
        self.row = row
        self.col = col
        self.colors = colors
        self.formula = formula
        self.solution = []

    def __str__(self):
        return f"Size: {self.y}x{self.x}, row:{self.row}, col:{self.col}"

    def to_formula(self):
        """ CONVERTIS LE NONOGRAMME EN FORMULE """
        self.formula = NNGFormula() # Formule principale
        compteur = self.x*self.y + 1 # Pour ne pas interférer avec les cases

        # LIGNES
        for i, c in enumerate(self.row): # i = ligne, c = coefficient
            lines = [] # Liste des configurations par ligne
            for config in convert(self.y, c): # Parcours des config
                x = list(range(i*self.y+1, (i+1)*self.y+1)) # Numéros de la ligne
                for v in [a*b for a,b in zip(x,config)]: # Parcours des variables
                    self.formula.append([-compteur, v]) # LISTE DES IMPLICATIONS
                lines.append(compteur)
                compteur += 1 # On passe a la prochaine config
            self.formula.append(lines)
        # COLONNES
        for i, c in enumerate(self.col): # i = ligne, c = coefficient
            lines = [] # Liste des configurations par ligne
            for config in convert(self.x, c): # Parcours des config
                x = [i%self.y + self.y * j + 1 for j in range(self.y)] # Numéros de la colonne
                for v in [a*b for a,b in zip(x,config)]: # Parcours des variables
                    self.formula.append([-compteur, v]) # LISTE DES IMPLICATIONS
                lines.append(compteur)
                compteur += 1 # On passe a la prochaine config
            self.formula.append(lines)



    def save(self, path="."): # O(1)
        """ SAUVEGARDE
        Sauvegarde le nonogramme dans un dossier, nom donné automatiquement
        Paramètres:
            - path: Chemin du dossier
        """
        print("Saving nonogram...")
        if path[-1] == "/": # Petite correction de syntaxe..
            path = path[:-1]
        path = f"{path}/{self.name.lower()}.nng" # nng = NoNoGram
        # Ci dessous: Dictionnaire qui regroupe les variables du nonogramme
        d = {"x": self.x, "y": self.y, "name": self.name, "row": self.row,
             "col": self.col, "colors": self.colors, "formula": self.formula,
             "solution": self.solution}
        with open(path, 'wb+') as file: # On ouvre en write + binary + créer
            pickle.dump(d, file)
        print(f"NNG {self.name} sucessfully saved.")

    def load(self, path):
        """ CHARGER
        Charge le fichier .nng d'un nonogramme
        Paramètres:
            - path: Chemin du fichier (et non du dossier cette fois-ci !)
        """
        print("Loading nonogram...")
        with open(path, 'rb') as file: # On ouvre en read + binary
            d = pickle.load(file) # Chargement du dictionnaire
        self.name = d["name"]
        self.x = d["x"]
        self.y = d["y"]
        self.row = d["row"]
        self.col = d["col"]
        self.colors = d["colors"]
        self.formula = d["formula"]
        self.solution = d["solution"]
        print(f"NNG {self.name} sucessfully loaded.")

    def solve(self, engine):
        """ RESOUDRE UN NONOGRAMME
        Paramètres:
            - engine: Classe Algorithme/Solveur SAT (Classe et non objet!)
        Retourne:
            - None si le nonogramme n'admet pas de modèle
            - Une liste si le nonogramme admet un modèle
        """
        return self.formula.solve(engine)
