# nonogram.py - Sofiane DJERBI & Salem HAFTARI
""" CONVENTIONS
 | Les nonogrammes donnent les informations en partant du haut et de la gauche.
 | row[x], col[y] : infos de la case en position x,y (Coordonnées matricielles)
"""
import pickle
from util.logic import NNGFormula
from util.graphics import Graphics

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
                 name="", colors=False, formula=NNGFormula()):
        """ INITIALISATION
        Paramètres:
            - size: Taile du nonogramme
            - name: Nom du nonogramme
            - row: Informations des lignes du nonogramme
            - col: Informations des colonnes du nonogramme
            - colors: Le nonogramme est-il en couleur (Booléen)
            - formula: Formule logique associée au nonogramme
        """
        self.x, self.y = size
        self.name = name
        self.row = row
        self.col = col
        self.colors = colors
        self.formula = formula

    def _to_formula(self):
        """ CONVERTIS LE NONOGRAMME EN FORMULE """
        pass


    def save(self, path):
        """ SAUVEGARDE
        Sauvegarde le nonogramme dans un dossier, nom donné automatiquement
        Variables :
            - path: Chemin du dossier
        """
        print("Saving nonogram...")
        if path[-1] == "/": # Petite correction de syntaxe..
            path = path[:-1]
        path = f"{path}/{self.name.lower()}.nng" # nng = NoNoGram
        # Ci dessous: Dictionnaire qui regroupe les variables du nonogramme
        d = {"x": self.x, "y": self.y, "name": self.name, "row": self.row,
             "col": self.col, "colors": self.colors, "formula": self.formula}
        with open(path, 'wb+') as file: # On ouvre en write + binary + créer
            pickle.dump(d, file)
        print(f"NNG {self.name} sucessfully saved.")

    def load(self, path):
        """ CHARGER
        Charge le fichier .nng d'un nonogramme
        Variables :
            - path: Chemin du fichier (et non du dossier cette fois-ci !)
        """
        print("Loading nonogram...")
        with open(path, 'rb') as file: # On ouvre en read + binary
            d = pickle.load(file) # nng = NoNoGram
        self.name = d["name"]
        self.x = d["x"]
        self.y = d["y"]
        self.row = d["row"]
        self.col = d["col"]
        self.colors = d["colors"]
        self.formula = d["formula"]
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
