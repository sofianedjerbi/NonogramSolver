# Logic.py - Sofiane DJERBI & Salem HAFTARI
""" CONVENTIONS
 | Notations :
 | a + b + (-cd) := NNGFormula([[1], [2], [-3, 4]])
 | En théorie nous manipulons des listes, c'est donc plus pratique et simple
 | qu'utiliser *args. Même si cela ne rend pas très "simple" en exemple.
"""
import pickle
from itertools import product


class NNGFormula:
    """ OBJET FORMULE LOGIQUE (adapté pour les nonogrammes)
    Variables:
        - list: Liste des sous formules, conjonctions ou disjonctions.
    """
    def __init__(self, l=None):
        """ INITIALISATION
        Paramètres:
            - l: Liste des sous termes.
        """
        self.list = l

    def __str__(self):
        """ AFFICHAGE DIMACS """
        return " 0\n".join(" ".join(str(e) for e in x) for x in self.list) + " 0"

    def _linearize(self):
        """ LINEARISATION
        Distribue tous les termes des listes.
        Permet une conversion FND <-> FNC.
        """
        self.list = list(product(*self.list))

    def solve(self, engine):
        """ RESOUDRE UNE FORMULE
        Paramètres:
            - engine: Classe Algorithme/Solveur SAT (Classe et non objet!)
        Retourne:
            - None si la formule n'admet pas de modèle
            - Une liste si la formule admet un modèle
        """
        self._linearize() # On met c sous FNC (on ne veux PAS convertir en dehors)
        instance = engine() # Une instance de l'engine pour pas le modifier
        for clause in self.list:
            instance.add_clause(clause)
        if instance.solve():
            return instance.get_model()
        return None # Sinon pas obligatoire car le if retourne


if __name__ == "__main__": # DEBUG !
    from pysat.solvers import Glucose4
    a = NNGFormula([[1,2,3,10], [4,5], [6,7,8]])
    #print(a) # FND
    #a._linearize() # FND -> FNC
    #print(a) # FNC
    # CryptoMiniSat: "v 1 2 3 -4 -5 -6 -7 -8 -9 -10 -11 0"
    #a.save("test", "./")
    #b = NNGFormula()
    #b.load("test.ngf")
    #print(b) # Fonctionnel
    # Maintenant on va solver a
    a = NNGFormula([[1,2,3,10], [4,5], [6,7,8]])
    print(a.solve(Glucose4)) #Fonctionnel!
