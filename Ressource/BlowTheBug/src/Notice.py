import pygame

from src import constant
from src import windowstate
from src.utils import addBouton


class Notice:
    def __init__(self):
        self.bg = pygame.image.load('assets/Background/background.png').convert()
        self.bg = pygame.transform.scale(self.bg, constant.SCREEN_SIZE)
        self.page = 1

    def addText(self, screen, font, texte, y):
        text_1 = font.render(texte, 1, constant.WHITE)
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

    def startNotice(self, screen):
        clock = pygame.time.Clock()

        running = True
        while running:

            screen.blit(self.bg, (0, 0))

            if self.page == 1:
                font = pygame.font.SysFont('Helvetic', 80)
                self.addText(screen, font, "Notice 1/3", 100)

                font = pygame.font.SysFont('Helvetic', 40)
                self.addText(screen, font, "Le principe est simple :", 200)
                self.addText(screen, font, "faire manger le cafard à son adversaire", 250)
                self.addText(screen, font, "Pour ça, il faut enchainer une combinaison de touches", 320)
                self.addText(screen, font, "Le joueur de gauche : Z, Q, S et D", 370)
                self.addText(screen, font, "Le joueur de droite : flèches haut, bas, droite et gauche", 420)

                self.addText(screen, font, "Celui qui réussi à souffler dans le tuyau pour ", 500)
                self.addText(screen, font, "faire gober le cafard à l'autre l'emporte", 550)
                suivant = addBouton(screen, None, 'Sign/Right1', constant.WIDTH - 250, constant.HEIGHT - 100, 50, 50)

            elif self.page == 2:
                font = pygame.font.SysFont('Helvetic', 80)
                self.addText(screen, font, "Notice 2/3", 100)
                font = pygame.font.SysFont('Helvetic', 40)
                self.addText(screen, font, "Comment sont calculés les points :", 250)
                self.addText(screen, font, "Votre score augmente si vous réussissez une combinaison", 300)
                self.addText(screen, font, "et diminue en cas d'échec", 350)
                self.addText(screen, font, "Comment lancer un malus :", 450)
                self.addText(screen, font, "Enchainer 3 bonnes combinaisons", 500)
                self.addText(screen, font, "Comment se libérer :", 550)
                self.addText(screen, font, "réussir une combinaison", 600)
                precedent = addBouton(screen, None, 'Sign/Left1', 200, constant.HEIGHT - 100, 50, 50)
                suivant = addBouton(screen, None, 'Sign/Right1', constant.WIDTH - 250, constant.HEIGHT - 100, 50, 50)

            else:
                font = pygame.font.SysFont('Helvetic', 80)
                self.addText(screen, font, "Notice 3/3", 100)
                font = pygame.font.SysFont('Helvetic', 40)

                self.addText(screen, font, "Malus invasion : ", 180)
                self.addText(screen, font, "Des cafards vous masquent la vue", 230)

                self.addText(screen, font, "Malus inversion : ", 300)
                self.addText(screen, font, "Les touches haut et bas ainsi que droite et gauche sont inversées", 350)

                self.addText(screen, font, "Malus temps : ", 420)
                self.addText(screen, font, "Un temps limité pour réussir une combinaison", 470)

                self.addText(screen, font, "Malus miroir : ", 540)
                self.addText(screen, font, "La combinaison est affichée de droite à gauche", 590)

                precedent = addBouton(screen, None, 'Sign/Left1', 200, constant.HEIGHT - 100, 50, 50)

            menu = addBouton(screen, 'Menu', None, constant.WIDTH // 2 - 200, constant.HEIGHT - 100, 400, 50)
            close = addBouton(screen, None, 'back', 15, 15, 30, 30)

            bug1 = pygame.image.load("assets/bigBug.png")
            bug1 = pygame.transform.rotate(bug1, -90)

            screen.blit(bug1, (80, 50))
            screen.blit(bug1, ((constant.WIDTH - 213), 50))
            screen.blit(bug1, (80, (constant.HEIGHT - 245)))
            screen.blit(bug1, ((constant.WIDTH - 213), (constant.HEIGHT - 245)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.notice = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if menu.collidepoint(pos) or close.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.notice = False
                        running = False
                    if self.page == 1 and suivant.collidepoint(pos):
                        self.page = 2
                    elif self.page == 2:
                        if precedent.collidepoint(pos):
                            self.page = 1
                        elif suivant.collidepoint(pos):
                            self.page = 3
                    elif self.page == 3 and precedent.collidepoint(pos):
                        self.page = 2
            clock.tick(constant.FPS)
