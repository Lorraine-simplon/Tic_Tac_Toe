import pygame
import sys


class Grille:
    def __init__(self, ecran):
        self.ecran = ecran
        self.lignes = [((200, 0), (200, 600)),
                       ((400, 0), (400, 600)),
                       ((0, 200), (600, 200)),
                       ((0, 400), (600, 400)), ]
        """initier la grille"""
        self.grille = [[None for x in range(0, 3)] for y in range(0, 3)]

    def afficher(self):
        for ligne in self.lignes:
            pygame.draw.line(self.ecran, (0, 0, 0), ligne[0], ligne[1], 2)

            """afficher les X et les O"""

        for y in range(0, len(self.grille)):
            for x in range(0, len(self.grille)):
                if self.grille[y][x] == 'X':
                    """0,0,0 = couleur noire"""
                    pygame.draw.line(
                        self.ecran, (0, 0, 0), (x * 200, y * 200), (200 + (x * 200), 200 + (y * 200)), 3)
                    pygame.draw.line(self.ecran, (0, 0, 0), ((
                        x * 200), 200 + (y * 200)), (200 + (x * 200), (y * 200)), 3)

                elif self.grille[y][x] == 'O':
                    pygame.draw.circle(
                        self.ecran, (0, 0, 0), (100 + (x * 200), 100 + (y * 200)), 100, 3)

    def print_grille(self):
        print(self.grille)

        """fixer les valeurs"""

    def fixer_la_valeur(self, x, y, valeur):
        self.grille[y][x] = valeur


class Jeu:
    def __init__(self):
        self.ecran = pygame.display.set_mode(size=(600, 600))
        pygame.display.set_caption("Tic Tac Toe")
        self.jeu_encours = True
        self.grille = Grille(self.ecran)
        """fixer les variables X et O"""
        self.player_X = 'X'
        self.player_O = 'O'
        """fixer le compteur"""
        self.compteur = 0

    def fonction_principale(self):
        while self.jeu_encours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    """ permet de sortir du jeu avec la croix rouge """
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    """obtenir la position de la souris"""
                    position = pygame.mouse.get_pos()
                    position_x, position_y = position[0]//200, position[1]//200
                    print(position)
                    print(position_x, position_y)

                    self.grille.fixer_la_valeur(position_x, position_y, 'X')
                    """condition si le compteur est pair ou impair"""
                    if self.compteur % 2 == 0:
                        self.grille.fixer_la_valeur(
                            position_x, position_y, self.player_X)
                    else:
                        self.grille.fixer_la_valeur(
                            position_x, position_y, self.player_O)

                    self.compteur += 1

                self.grille.print_grille()

            self.ecran.fill((240, 240, 240))
            self.grille.afficher()
            pygame.display.flip()
            """ permet de mettre à jour l'écran """


if __name__ == "__main__":
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
