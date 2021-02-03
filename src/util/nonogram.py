# nonogram.py - Sofiane DJERBI
""" CONVENTIONS
 | Les nonogram donnent les informations en partant du haut et de la gauche.
"""

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
    def __init__(self, size, row, col, name="", colors=False):
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
