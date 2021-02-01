# Graphics.py - Sofiane DJERBI
""" CONVENTIONS
 | Chaque case fait 8*8 pixels.
 | La taille de la fenêtre dépend de la taille du nonogram.
 | Un pixel pour séparer chaque case
 |
 |
 |
"""
import pygame

class Graphics:
    """ GESTIONNAIRE DE GRAPHISMES
    Gestionnaire de fenêtre, d'affichage, API pour manipuler l'affichage facilement.
    Variables:
        - x : Nombre de cases en x
        - y : Nombre de cases en y
        - screen : Objet surface de pygame, contient le contenu de la fenêtre
    """
    def __init__(self, title, x, y, icon=None, background=(255, 255, 255)):
        """ INITIALISATION
        Parametres :
            - title : Titre de la fenêtre
            - x : Nombre de cases en x
            - y : Nombre de cases en y
            - background : Couleur de fond
            - icon : Icone de la fenêtre
        """
        pygame.init() # Initialisation de pygame
        self.screen = pygame.display.set_mode((x*11-1, y*11-1)) # *11 - 1 = UN pixel entre caque case
        pygame.display.set_caption(title) # Titre
        self.x = x
        self.y = y
        # Ci-dessous : Charger l'image et la désigner comme icone du programme.
        if icon is not None:
            image = pygame.image.load(icon)
            pygame.display.set_icon(image)
        self.screen.fill(background) # Couleur de fond

    def tick(self):
        """ Affiche le contenu graphique chargé dans les surfaces temporaies de pygame
        """
        pygame.display.flip()

    def draw_grid(self, grid_color=(0,0,0)):
        """ Dessine la grille de jeu
        Parametres :
            - grid_color : Couleur des bords de la grille
        """
        for x in range(self.x):
            for y in range(self.y):
                rect = pygame.Rect((x*11, y*11), (11, 11)) # Objet rectangle pygame
                pygame.draw.rect(self.screen, grid_color, rect,  1) # Dessinons l'objet sur la surface principale

    def color_box(self, x, y, color=(0,0,0)):
        """ Dessine la grille de jeu
        Parametres :
            - x, y : Position de la case
        """
        rect = pygame.Rect((x*11, y*11), (11, 11)) # Objet rectangle pygame
        pygame.draw.rect(self.screen, color, rect) # Dessinons l'objet sur la surface principale


if __name__ == "__main__": # DEBUG!
    graphics = Graphics("Nonogram", 32, 32, icon="resources/icon.png")
    graphics.draw_grid()
    for i in range(10):
        graphics.color_box(i, i)
    while True:
        for event in pygame.event.get(): # Gerer les events
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        graphics.tick()
