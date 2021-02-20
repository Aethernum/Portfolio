import pygame

from src import constant
from src import windowstate
from src.utils import getBestPlayer, addBouton


class HighScore:
    def __init__(self):
        self.bg = pygame.image.load('assets/Background/background.png').convert()
        self.bg = pygame.transform.scale(self.bg, constant.SCREEN_SIZE)

        # Création d'une liste, il faut recuperer les high score et les ordonner
        self.joueurs = getBestPlayer()

    def startHighScore(self, screen):
        clock = pygame.time.Clock()
        self.joueurs = getBestPlayer()
        screen.blit(self.bg, (0, 0))
        font = pygame.font.Font(None, 80)
        text_1 = font.render("High-Score", 1, constant.WHITE)
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

        menu = addBouton(screen, 'Menu', None, constant.WIDTH // 2 - 200, constant.HEIGHT - 100, 400, 50)
        close = addBouton(screen, None, 'back', 15, 15, 30, 30)

        y = 0
        font = pygame.font.Font(None, 40)
        for joueur in self.joueurs:
            text_nom = font.render(joueur['name'], 1, constant.WHITE)
            rect_nom = text_nom.get_rect()
            rect_nom.x = 300
            rect_nom.y = 200 - text_nom.get_rect().height // 2 + y

            text_score = font.render(str(joueur['highscore']), 1, constant.WHITE)
            rect_score = text_score.get_rect()
            rect_score.x = rect_nom.x + 300
            rect_score.y = rect_nom.y

            y += 100
            screen.blit(text_nom, rect_nom)
            screen.blit(text_score, rect_score)

        bug1 = pygame.image.load("assets/bigBug.png")
        bug1 = pygame.transform.rotate(bug1, -90)

        screen.blit(bug1, (120, 300))
        screen.blit(bug1, (740, 300))

        pygame.display.flip()

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.highscore = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if menu.collidepoint(pos) or close.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.highscore = False
                        running = False

            clock.tick(constant.FPS)