import pygame

from src import constant
from src.Ball import Ball


class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/pipe.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (630, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 205
        self.rect.y = 340
        self.ball = Ball()
        self.ball.rect.center = self.rect.center

    def moveRight(self):
        self.ball.moveRight()

    def moveLeft(self):
        self.ball.moveLeft()

    def collide(self):
        if not self.rect.contains(self.ball.rect):
            if self.ball.rect.x < self.rect.x:
                loser = 'left'
            else:
                loser = 'right'
            return True, loser
        else:
            return False, None