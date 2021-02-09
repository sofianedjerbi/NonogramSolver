# Logic.py - Sofiane DJERBI
""" CONVENTIONS
 | Notations python
 | i.e OU |, ET &, NEG -
 | La négation est "contenue dans la variable" (voir exemple).
 | Deux listes pour une formule : Une liste de sous-formules + une liste d'opérateurs
 | Exemple : Liste d'opérateurs : ["&", "|"], Liste de formules : ["1 | 5", "-2", "3"]
 | Formule logique correspondante : ((1 | 5) & -2 | 3) (NOTE : la longueur de la liste opérateurs est n-1, n=len(liste_formule)
 | Testez la partie debug ci dessous pour plus de précisions
"""
""" Ce code contient beaucoup d'objets (4). Voilà une liste :
    - Objet "Formula", une forme normale
    - Objet "Variable", une variable
    - Objet "CNF", une forme normale conjonctive
    - Objet "DNF", une forme normale disjonctive
"""
import re


class Formula: # On suppose que la formule est en forme normale !
    """ FORMULE (FORME NORMALE)
    Modélisation d'une formule en forme normale
    Variables:
        - formula : Liste des sous formules
        - operator : Liste des opérations dans l'ordre
    """
    def __init__(self, txt="", allowed_operators=["|", "&"]):
        """ INITIALISATION
        Paramètres :
            - txt : Formule sous forme de texte
        """
        self.formula = list()
        self.operator = list()
        self.allowed_operators = allowed_operators
        if txt != "":
            self._unserialize(txt)

    def __str__(self):
        """ AFFICHAGE DE LA LISTE (SERIALISATION) """
        txt = "("
        for i in range(0, len(self.operator)):
            txt += f"{self.formula[i]} {self.operator[i]} "
        return txt + f"{self.formula[-1]})"

    def _unserialize(self, txt): # Le _ devant : Cette fonction n'est pas sensée être utilisée autre part que dans cette classe
        """ DESERIALISATION
        Transforme une formule normale sous forme de texte en objet formule normale
        Paramètres:
            - txt : Texte de la formule normale
        """
        self.operator = list()
        self.formula = list()
        pos = 0 # Profondeur des parenthèses
        handler = ""
        raw = []
        # Ci dessous : A réduire ?
        for c in txt: # On coupe les parenthèses principales
            if c == '(':
                pos += 1
                if pos == 1 and handler != "": # debut parenthèse
                    raw.append(handler)
                    handler = ""
                handler += '('
            elif c == ')':
                pos -= 1
                handler += ')'
                if pos == 0: # fin parenthèse
                    raw.append(handler)
                    handler = ""
            else:
                handler += c
        if handler != "":
            raw.append(handler)
        for f in raw: # On ajoue dans les listes de la formule
            if f[0] == '(':
                self.formula.append(Formula(f[1:-1]))
            else:
                for w in f.split(): # On parcours les variables et signes
                    if w in self.allowed_operators:
                        self.operator.append(w)
                    elif w.replace('-', '').isnumeric():
                        self.formula.append(Variable(int(w)))
                    else:
                        raise ValueError(f"Formula incorrect: {txt}")


class Variable(Formula): # Une variable est une formule, elle hérite donc des propriétés
    """ VARIABLE
    Variables:
        - id : Id de la variable (le nom qu'elle aura dans le fichier DIMACS)
    """
    def __init__(self, id):
        """ INITIALISATION
        Paramètres :
            - id : Nom de la variable
        """
        super().__init__() # On initialise la formule
        self.id = id

    def __str__(self):
        """ AFFICHAGE (SERIALISATION) """
        return str(self.id)


class CNF(Formula): # Une FNC (CNF en anglais) est une formule, elle hérite donc des propriétés
    def __init__(self, txt=""):
        """ INITIALISATION
        Paramètres:
            - formula : Formule sous forme de texte
        """
        super().__init__(txt, "&") # On autorise seulement les conjonctions

    def export(self):
        """ EXPORT EN FORMAT DIMACS COMPATIBLE """
        txt = str(self)
        txt = txt.replace("(", "")
        txt = txt.replace(")", "")
        txt = txt.replace(" ", "")
        txt = txt.replace("|", " ")
        txt = txt.replace("&", " 0\n")
        cnt = txt.count('\n')
        nbl = [e for e in txt.split() if e.isnumeric()]
        nb = max(nbl)
        return f"p cnf {nb} {cnt}\n" + txt + " 0"

class DNF(Formula): # Une FND (DNF en anglais) est une formule, elle hérite donc des propriétés
    def __init__(self, txt=""):
        """ INITIALISATION
        Paramètres:
            - formula : Formule sous forme de texte
        """
        super().__init__(txt, "|") # On autorise seulement les disjonctions

    def to_cnf(self): # On suppose qu'il y a plusieurs objet dans self.formula, sinon c'est inutile..
        """ CONVERSION EN FNC """
        operator = []
        formula = []
        cnf = CNF()
        for i in range(1, len(self.formula)):
            for var0 in self.formula[0].formula: # On distribue le premier terme sur tous les termes sans exception
                for var in self.formula[i].formula:
                    formula.append(Formula(f"{var0} | {var}"))
                    operator.append("&")
        cnf.operator = operator
        cnf.formula = formula
        return cnf



if __name__ == "__main__": # DEBUG !
    f = Formula("(1 | 2 | (3 & 4) | 5) & (6 | 7) & 8 & 9 & 10")
    print(f)
    f2 = DNF("(1 & 2 & 3 & -4 & -5 & -6) | (-1 & 2 & 3 & 4 & -5 & -6) | (-1 & -2 & 3 & 4 & 5 & -6) | (-1 & -2 & -3 & 4 & 5 & 6)")
    cnf = f2.to_cnf()
    print("CNF : ", cnf)
    print("EXPORT : ", cnf.export())
