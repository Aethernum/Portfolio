import pygame

from src import constant


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bigBug.png')
        self.image = pygame.transform.scale(self.image, (65, 44))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 110
        self.velocity = 40

    def moveRight(self):
        self.rect.x += self.velocity

    def moveLeft(self):
        self.rect.x -= self.velocity