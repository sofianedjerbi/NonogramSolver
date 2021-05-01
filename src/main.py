""" MENU, INTERFACE UTILISATEUR CLI """
from pysat.solvers import *
from util.nonogram import *
from util.graphics import *
import time
import os

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
    num = input("Your choice: ")
    if not num.isnumeric() or int(num) > max or int(num) < 1: # Si le choix est invalide
        print("Incorrect choice.")
        return choice(max) # Pour éviter un faux do..while
    return int(num) - 1

def solve(nonogram):
    pass


class Menu():
    def main(self):
        print("\n- MAIN MENU -")
        print("1) Browse available nonograms")
        print("2) Download a nonogram online (requests-html needed)")
        print("3) Exit")
        next = [self.nonogram, self.download, self.stop] # Index = Choix du joueur
        c = choice(3)
        return next[c]()

    def stop(self):
        return

    def download(self):
        print("\n- DOWNLOADING -")
        if SCRAPER:
            url = input("Nonogram.org URL: ")
            scraper = Scraper()
            try:
                nonogram = scraper.get(url)
                nonogram.save("resources/nonograms/")
            except Exception as e:
                print(e) # On laisse requests_html gerer les erreurs
        else:
            print("Module requests-html non installé.")
            time.sleep(2)
        print("Back to the main menu...")
        self.main()

    def nonogram(self):
        print("\n- CHOOSE A NONOGRAM -")
        dir = os.listdir("resources/nonograms") # Liste des nonogrammes
        for i, n in enumerate(dir):
            print(f"{i+1}) \"{n[:-4]}\"")
        c = choice(len(dir))
        nonogram = Nonogram()
        nonogram.load(f"resources/nonograms/{dir[c]}")
        self.solve(nonogram)

    def solve(self, nng):
        # SAT_LIST = [Glucose4, MinisatGH, Minisat22, Lingeling, Cadical]
        print("\n- CHOOSE ENGINE -")
        print("1) Glucose 4")
        print("2) Minisat (Github Version)")
        print("3) Minisat 2.2")
        print("4) Lingeling")
        print("5) Cadical")
        c = choice(len(SAT_LIST)+1)
        engine = SAT_LIST[c]

        print("\nGenerating ODIMACS...")
        a = time.time()
        nng.to_formula()
        t = time.time() - a
        print("ODIMACS generated in {:.2f} seconds!".format(t))

        vars = nng.solve(engine)
        self.show(nng, vars)

    def show(self, nng, vars):
        print("\nDraw grid ? 1 = No, 2 = Yes")
        c = choice(2)
        graphics = Graphics("Nonogram Solver", nng.y, nng.x, "resources/icon.png")
        if c:
            graphics.draw_grid()
        for x in vars:
            x = x-1 # On refais le décalage inverse du format DIMACS
            if x >= 0 and x < nng.x * nng.y: # x activé et pas une configuration
                graphics.color_box(x%nng.y, x//nng.y)
        GUI = True
        while GUI:
            graphics.tick()
            for event in pygame.event.get(): # Gerer les events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    GUI = False
        self.main()



if __name__ == "__main__": # Programme principal
    sat = DEFAULT_SAT
    print(LOGO) # Logo
    menu = Menu()
    menu.main()
