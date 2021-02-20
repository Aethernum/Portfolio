import pygame

from src import constant
from src import windowstate
from src.utils import addBouton


class Menu:
    def __init__(self):
        self.bg = pygame.image.load('assets/Background/background_menu.png').convert()
        self.bg = pygame.transform.scale(self.bg, constant.SCREEN_SIZE)
        self.rect = self.bg.get_rect()

    def startMenu(self, screen):
        screen.blit(self.bg, self.rect)

       #titre du menu
        font = pygame.font.SysFont('Helvetic', 80)

        name = pygame.image.load("assets/name/name.png")
        screen.blit(name, (constant.WIDTH // 2 - name.get_rect().width // 2, 100 - name.get_rect().height // 2))

        play = addBouton(screen, "Jouer", None, constant.WIDTH // 2 - 200, 200, 400, 50)
        instruction = addBouton(screen, "Comment jouer ?", None, constant.WIDTH // 2 - 200, 275, 400, 50)
        high = addBouton(screen, "High-Score", None, constant.WIDTH // 2 - 200, 350, 400, 50)
        settings = addBouton(screen, "Paramètres", None, constant.WIDTH // 2 - 200, 425, 400, 50)
        credits = addBouton(screen, "Crédits", None, constant.WIDTH // 2 - 200, 500, 400, 50)
        close = addBouton(screen, "Fermer", None, constant.WIDTH // 2 - 200, 575, 400, 50)

        pygame.display.flip()

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.menu = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if play.collidepoint(pos):
                        windowstate.playerName = True
                        windowstate.menu = False
                        running = False

                    elif instruction.collidepoint(pos):
                        windowstate.notice = True
                        windowstate.menu = False
                        running = False

                    elif high.collidepoint(pos):
                        windowstate.highscore = True
                        windowstate.menu = False
                        running = False

                    elif settings.collidepoint(pos):
                        windowstate.settings = True
                        windowstate.menu = False
                        running = False

                    elif credits.collidepoint(pos):
                        windowstate.credits = True
                        windowstate.menu = False
                        running = False

                    elif close.collidepoint(pos):
                        windowstate.menu = False
                        running = False