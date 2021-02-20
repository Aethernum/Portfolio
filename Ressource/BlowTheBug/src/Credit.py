import pygame

from src import constant
from src import windowstate
from src.utils import addBouton


class Credit:
    def __init__(self):
        self.bg = pygame.image.load('assets/Background/background.png').convert()
        self.bg = pygame.transform.scale(self.bg, constant.SCREEN_SIZE)
        self.rect = self.bg.get_rect()

    def addText(self, screen, font, texte, y):
        text_1 = font.render(texte, 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

    def startCredits(self, screen):
        clock = pygame.time.Clock()

        running = True

        screen.blit(self.bg, (0, 0))

        font = pygame.font.SysFont('Helvetic', 80)
        self.addText(screen, font, "Crédits", 80)

        font = pygame.font.SysFont('Helvetic', 40)
        self.addText(screen, font, "L'équipe Semi :", 150)
        self.addText(screen, font, "- Martin, game designer - testeur", 200)
        self.addText(screen, font, "- Fanny, développeuse", 250)
        self.addText(screen, font, "- Marine, développeuse", 300)
        self.addText(screen, font, "- Julien, développeur - intégrateur", 350)
        self.addText(screen, font, "- Joris, développeur - graphiste", 400)

        self.addText(screen, font, "Son : Universal-soundbank    buzzer 6", 480)
        self.addText(screen, font, "Son : Freesound : xtrsounder    Human blowing", 530)
        self.addText(screen, font, "Son : Freesound : Zihris    Applause_encore", 580)
        self.addText(screen, font, "Musique : Kevin MacLeod    Welcome to the Show", 630)

        menu = addBouton(screen, 'Menu', None, constant.WIDTH // 2 - 200, constant.HEIGHT - 100, 400, 50)
        close = addBouton(screen, None, 'back', 15, 15, 30, 30)

        bug1 = pygame.image.load("assets/bigBug.png")
        bug1 = pygame.transform.rotate(bug1, -90)

        screen.blit(bug1, (80, 200))
        screen.blit(bug1, (780, 200))

        pygame.display.flip()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.credits = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if menu.collidepoint(pos) or close.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.credits = False
                        running = False

            clock.tick(constant.FPS)