# solver.py - Sofiane DJERBI & Salem HAFTARI
import threading
import random
import os

P = 0.5
MAX = 10000000

class RandomWalk:
    """ RANDOMWALK
    Cet objet représente le solveur WalkSat
    Variables:
        - clauses: Liste des clauses
        - variables: Dictionnaire des variables {abs(v): v}
    """
    def __init__(self):
        """ INITIALISATION """
        self.clauses = []
        self.variables = {}

    def add_clause(self, l):
        """ AJOUTE UNE CLAUSE
        Paramètres:
            - l: Sous liste (FNC)
        """
        self.clauses.append(l)

    def solve(self):
        """ RESOLUTION DES CLAUSES
            (Algorithme du sujet)
            Retourne True si un modèle est trouvé, False sinon.
        """
        for i in range(MAX):
            for clause in self.clauses: # On parcours les clauses
                for v in clause: # On parcours les variables
                    if abs(v) not in self.variables.keys(): # Si variable inconnue
                        self.variables[abs(v)] = v # La variable est celle donnée (en faveur du "ou")
                bools = [self.variables[abs(i)] == i for i in clause] # Les valeurs des clause
                bools = sum(bools) > 0 # Si au moins une est vraie
                if not bools: # Si la clause est fausse
                    if random.random() <= P:
                        v = random.choice(clause) # On prend une variable aléatoire
                    else:
                        v = clause[-1] # On prend la dernière variable
                    self.variables[abs(v)] *= -1 # On inverse la valeur
            if self.is_model():
                return True
            else:
                continue
        return False

    def is_model(self):
        """ EST MODELE
            Retourne True si les variables sont un modèle, False sinon.
        """
        for clause in self.clauses: # Parcours des clauses
            bools = [self.variables[abs(i)] == i for i in clause] # Les valeurs des clause
            bools = sum(bools) > 0 # Si au moins une est vraie
            if not bools:
                return False
        return True

    def get_model(self):
        """ RETOURNE LE MODELE """
        return list(self.variables.values())


if __name__ == '__main__':
    sat = RandomWalk()
    sat.add_clause([-6, 1])
    sat.add_clause([-6, 2])
    sat.add_clause([-6, -3])
    sat.add_clause([-6, 4])
    sat.add_clause([-6, -5])
    sat.add_clause([-7, 1])
    sat.add_clause([-7, 2])
    sat.add_clause([-7, -3])
    sat.add_clause([-7, -4])
    sat.add_clause([-7, 5])
    sat.add_clause([-8, -1])
    sat.add_clause([-8, 2])
    sat.add_clause([-8, 3])
    sat.add_clause([-8, -4])
    sat.add_clause([-8, 5])
    sat.add_clause([6, 7, 8])
    sat.add_clause([-9, -1])
    sat.add_clause([9])
    sat.add_clause([-10, 2])
    sat.add_clause([10])
    sat.add_clause([-11, 3])
    sat.add_clause([11])
    sat.add_clause([-12, -4])
    sat.add_clause([12])
    sat.add_clause([-13, 5])
    sat.add_clause([13])
    print(sat.solve())
    print(sat.get_model())
"""
    sat.add_clause([-6, 1])
    sat.add_clause([-6, 2])
    sat.add_clause([-6, -3])
    sat.add_clause([-6, 4])
    sat.add_clause([-6, -5])

    sat.add_clause([-7, 1])
    sat.add_clause([-7, 2])
    sat.add_clause([-7, -3])
    sat.add_clause([-7, -4])
    sat.add_clause([-7, 5])

    sat.add_clause([-8, -1])
    sat.add_clause([-8, 2])
    sat.add_clause([-8, 3])
    sat.add_clause([-8, -4])
    sat.add_clause([-8, 5])

    sat.add_clause([6,7,8])

    sat.add_clause([-9, 1])
    sat.add_clause([9])

    sat.add_clause([-10, 2])
    sat.add_clause([10])

    sat.add_clause([-11, 5])
    sat.add_clause([11])

    sat.add_clause([-12, -3])
    sat.add_clause([12])

    sat.add_clause([-13, -4])
    sat.add_clause([13])
"""
