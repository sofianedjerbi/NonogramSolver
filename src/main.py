from pysat.solvers import *
import time
try:
    from util.scraper import Scraper
    SCRAPER=True
except Exception:
    SCRAPER=False


# ENVIRONMENT
SAT_LIST = [Glucose4, MinisatGH, Minisat22, Lingeling, Cadical]
DEFAULT_SAT = 0 # Glucose4, index dans la liste
# Nom de l'objet: <instance>.__name__
# FIN_ENVIRONMENT

LOGO = """
███╗   ██╗ ██████╗ ███╗   ██╗ ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗
████╗  ██║██╔═══██╗████╗  ██║██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
██╔██╗ ██║██║   ██║██╔██╗ ██║██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║
██║╚██╗██║██║   ██║██║╚██╗██║██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
██║ ╚████║╚██████╔╝██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝

            ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗
            ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗
  █████╗    ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝    █████╗
  ╚════╝    ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗    ╚════╝
            ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║
            ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝
                   Sofiane DJERBI & Salem HAFTARI
"""


def choice(max):
    """ CHOIX DU JOUEUR
    Paramètres:
        - max: Numéro max du choix
    Renvoie le choix du joueur
    """
    num = input("Votre choix: ")
    if not num.isnumeric() or int(num) > max: # Si le choix est invalide
        print("Choix incorrect.")
        return choice(max) # Pour éviter un faux do..while
    return int(num)

def solve(nonogram):
    pass


class MenuManager():
    def main(self):
        print("\n\n")
        print("""- MAIN MENU -

        1) Browse available nonograms
        2) Solve nonogram online (requests-html needed)
        3) Exit
        """)
        next = [self.nonogram, self.download, None] # Index = Choix du joueur
        c = choice(3)
        return next[c-1]()

    def download(self):
        print("\n\n")
        print("""- DOWNLOADING -""")
        if SCRAPER:
            url = input("Nonogram.org URL: ")
            scraper = Scraper()
            try:
                nonogram = scraper.get(url)
                
            except Exception as e:
                print(e) # On laisse requests_html gerer les erreurs
        else:
            print("Module requests-html non installé.")
            time.sleep(1)
        print("Retour au menu principal...")
        time.sleep(1)
        self.main()

    def nonogram():
        print("\n\n")
        pass




if __name__ == "__main__": # Programme principal
    sat = DEFAULT_SAT
    print(LOGO) # Logo
    menu = MenuManager()
    menu.main()
