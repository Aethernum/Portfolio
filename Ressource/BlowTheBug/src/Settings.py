import json
import pygame

from src import constant, windowstate
from src.utils import addBouton, toggleSound, toggleMusic, isSoundOn, isMusicOn


class Settings:
    def __init__(self):
        self.bg = pygame.image.load('assets/Background/background.png').convert()
        self.bg = pygame.transform.scale(self.bg, constant.SCREEN_SIZE)
        self.rect = self.bg.get_rect()

    def startSettings(self, screen):
        clock = pygame.time.Clock()

        running = True
        while running:
            screen.blit(self.bg, self.rect)

            font = pygame.font.SysFont('Helvetic', 80)
            text_1 = font.render("Paramètres", 1, (255, 255, 255))
            text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
            screen.blit(text_1, text_1_pos)

            close = addBouton(screen, None, 'back', 15, 15, 30, 30)
            menu = addBouton(screen, "Menu", None, constant.WIDTH // 2 - 200, 400, 400, 50)

            if isSoundOn():
                sound = addBouton(screen, "SFX", "vol", constant.WIDTH // 2 - 100, 150, 50, 50)
            else:
                sound = addBouton(screen, "SFX", "mute_vol", constant.WIDTH // 2 - 100, 150, 50, 50)

            if isMusicOn():
                music = addBouton(screen, "Musique", "music", constant.WIDTH // 2 + 50, 150, 50, 50)
            else:
                music = addBouton(screen, "Musique", "mute_music", constant.WIDTH // 2 + 50, 150, 50, 50)

            bug1 = pygame.image.load("assets/bigBug.png")
            bug1 = pygame.transform.rotate(bug1, -90)

            screen.blit(bug1, (120, 200))
            screen.blit(bug1, (740, 200))
            screen.blit(bug1, (120, 500))
            screen.blit(bug1, (740, 500))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.settings = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if close.collidepoint(pos) or  menu.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.settings = False
                        running = False

                    elif sound.collidepoint(pos):
                        toggleSound()

                    elif music.collidepoint(pos):
                        toggleMusic()

            clock.tick(constant.FPS)