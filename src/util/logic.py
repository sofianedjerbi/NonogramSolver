# Logic.py - Sofiane DJERBI & Salem HAFTARI
# DEPRECATED
# FICHIER INUTILE !
# DEPRECATED
""" CONVENTIONS
 | Notations :
 | a + b + (-cd) := NNGFormula([[1], [2], [-3, 4]])
 | En théorie nous manipulons des listes, c'est donc plus pratique et simple
 | qu'utiliser *args. Même si cela ne rend pas très "simple" en exemple.
 |
 | /!\ Cette implémentation n'est pas une implémentation complète de la logique
 | Nous traitons uniquement des FND / FNC
 |
 | Le format de données choisi est le "ODIMACS", notre version "Optimisée" du
 | format DIMACS:
 |
 | - Données stockées en "wb" ascii
 | - Retour "\n" au lieu de " 0\n"
 | - Pas de ligne de "présentation" (p cnf ..) (Pour éviter le parcours)
"""
import pickle
import os
import time
import numba
import threading

from itertools import product


class NNGFormula:
    """ OBJET FORMULE LOGIQUE (adapté pour les nonogrammes)
    Variables:
        - list: Liste des sous formules, conjonctions ou disjonctions.
    """
    def __init__(self, l=[]):
        """ INITIALISATION
        Paramètres:
            - l: Liste des sous termes.
        """
        self.clauses = []

    #def __str__(self): # !!! DEPRECATED !!!
    #    """ AFFICHAGE DIMACS """
    #    return " 0\n".join(" ".join(str(e) for e in x) for x in self.file) + " 0"

    def append(self, l):
        """ AJOUTE DES ELEMENTS DANS LA LISTE
        Paramètres:
            - l: Sous liste (FNC)
        """
        self.clauses.append(l)

    def solve(self, engine):
        """ RESOUDRE UNE FORMULE
        Paramètres:
            - engine: Classe Algorithme/Solveur SAT (Classe et non objet!)
        Retourne:
            - None si la formule n'admet pas de modèle
            - Une liste si la formule admet un modèle
        """
        instance = engine() # Une instance de l'engine pour pas le modifier

        print("\nLoading ODIMACS...")
        a = time.time()
        for clause in file:
            instance.add_clause([int(i) for i in clause[:-1].split(' ')]) # On enlève le \n
        file.close()
        t = time.time() - a
        print("Loaded in {:.2f} seconds!".format(t))

        print("\nSolving...")
        a = time.time()
        solvable = instance.solve()
        t = time.time() - a
        print("Solved in {:.2f} seconds!".format(t))

        threading.Thread(target=os.remove, args=[self.name]).start() # Supression dans un thread différent

        if solvable:
            return instance.get_model()
        return None # "Sinon" pas obligatoire car le if retourne


if __name__ == "__main__": # DEBUG !
    from pysat.solvers import Glucose4
    a = NNGFormula([[1,2,3,10], [4,5], [6,7,8]])
    #print(a) # FND
    #a.linearize() # FND -> FNC
    #print(a) # FNC
    # CryptoMiniSat: "v 1 2 3 -4 -5 -6 -7 -8 -9 -10 -11 0"
    #a.save("test", "./")
    #b = NNGFormula()
    #b.load("test.ngf")
    #print(b) # Fonctionnel
    # Maintenant on va solver a
    a = NNGFormula([[1,2,3,10], [4,5], [6,7,8]])
    print(a.solve(Glucose4)) #Fonctionnel!
