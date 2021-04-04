# nonogram.py - Sofiane DJERBI & Salem HAFTARI
""" CONVENTIONS
 | Les nonogram donnent les informations en partant du haut et de la gauche.
 | row[x], col[y] donne les données de la case en position x,y (Coordonnées matricielles)
"""
import pickle
from pathlib import Path

class Nonogram:
    """ NONOGRAMME
    Cet objet représente un nonogramme.
    Variables :
        - x, y : Taille du nonogramme
        - name : Nom du nonogramme
        - row : Informations des lignes du nonogramme
        - col : Informations des colonnes du nonogramme
        - colors : Le nonogramme est-il en couleur (Booléen)

    """
    def __init__(self, size=(0,0), row=[], col=[], name="", colors=False):
        """ INITIALISATION
        Paramètres :
            - size: Taile du nonogramme
            - name : Nom du nonogramme
            - row : Informations des lignes du nonogramme
            - col : Informations des colonnes du nonogramme
            - colors : Le nonogramme est-il en couleur (Booléen)
        """
        self.x, self.y = size
        self.name = name
        self.row = row
        self.col = col
        self.colors = colors

    def save(self, path):
        """ SAUVEGARDE
        Sauvegarde le nonogramme dans un dossier, le nom est donné automatiquement
        Variables :
            - path : Chemin du dossier
        """
        print("Saving nonogram...")
        if path[-1] == "/": # Petite correction de syntaxe..
            path = path[:-1]
        path = f"{path}/{self.name.lower()}.nng"
        path = Path(__file__).parent / path # Chemin complet
        # Ci dessous : Dictionnaire qui regroupe les variables du nonogramme
        d = {"x": self.x, "y": self.y, "name": self.name, "row": self.row, "col": self.col, "colors": self.colors}
        with open(path.resolve(), 'wb+') as file: # On ouvre en write + binary + créer si n'existe pas
            pickle.dump(d, file) # nng = NoNoGram
        print(f"Nonogram {self.name} sucessfully saved.")


    def load(self, path):
        """ SAUVEGARDE
        Sauvegarde le nonogramme dans un dossier, le nom est donné automatiquement
        Variables :
            - path : Chemin du fichier (et non du dossier cette fois-ci !)
        """
        print("Loading nonogram...")
        path = Path(__file__).parent / path # Chemin complet
        with open(path.resolve(), 'rb') as file: # On ouvre en write + binary
            d = pickle.load(file) # nng = NoNoGram
        self.name = d["name"]
        self.x = d["x"]
        self.y = d["y"]
        self.row = d["row"]
        self.col = d["col"]
        self.colors = d["colors"]
        print(f"Nonogram {self.name} sucessfully loaded.")
