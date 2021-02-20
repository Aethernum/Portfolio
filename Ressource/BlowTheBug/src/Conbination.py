import random

import pygame
from pygame.locals import *

class Combination(object):
    def __init__(self, combi):
        self.length = len(combi)
        self.keys = combi
        self.keysValue = []
        for i in self.keys:
            self.keysValue.append(eval("K_" + i))
        self.state = 0 # -1 = raté, 0 = en cours, 1 = réussi
        self.attempt = []
        self.goal = []
        self.tempGoal = []
        self.goalValue = []
        self.score = 0

    def newRandom(self, length):
        i = 0
        self.goal = []
        self.goalValue = []
        self.tempGoal = []
        while i < length:
            self.tempGoal.append(self.keys[random.randrange(0, self.length)])
            i += 1
        for i in self.tempGoal:
            self.goalValue.append(eval("K_" + i))
        i = 0
        self.attempt = []
        for i in self.tempGoal:
            if i == 'q' or i == 'LEFT':
                self.goal.append(pygame.image.load('assets/Sign/Left1.png').convert_alpha())
            elif i == 'd' or i == 'RIGHT':
                self.goal.append(pygame.image.load('assets/Sign/Right1.png').convert_alpha())
            elif i == 'z' or i == 'UP':
                self.goal.append(pygame.image.load('assets/Sign/Up1.png').convert_alpha())
            elif i == 's' or i == 'DOWN':
                self.goal.append(pygame.image.load('assets/Sign/Down1.png').convert_alpha())

    def tried(self, car):
        self.attempt.append(car)
        size = len(self.attempt)
        if self.attempt == self.goalValue [0:size] and size == len(self.goalValue):
            self.state = 1
            self.score += 10
        elif self.attempt == self.goalValue [0:size]:
            if self.tempGoal[size - 1] == 'q' or self.tempGoal[size - 1] == 'LEFT':
                self.goal[size - 1] = pygame.image.load('assets/Sign/Left2.png').convert_alpha()

            elif self.tempGoal[size - 1] == 'd' or self.tempGoal[size - 1] == 'RIGHT':
                self.goal[size - 1] = pygame.image.load('assets/Sign/Right2.png').convert_alpha()

            elif self.tempGoal[size - 1] == 'z' or self.tempGoal[size - 1] == 'UP':
                self.goal[size - 1] = pygame.image.load('assets/Sign/Up2.png').convert_alpha()

            elif self.tempGoal[size - 1] == 's' or self.tempGoal[size - 1] == 'DOWN':
                self.goal[size - 1] = pygame.image.load('assets/Sign/Down2.png').convert_alpha()
            self.state = 0
        else:
            self.state = -1
            self.score -= 10

    def reverse(self, car):
        if car == K_z:
            return K_s
        elif car == K_s:
            return K_z
        elif car == K_q:
            return K_d
        elif car == K_d:
            return K_q
        elif car == K_UP:
            return K_DOWN
        elif car == K_DOWN:
            return K_UP
        elif car == K_LEFT:
            return K_RIGHT
        elif car == K_RIGHT:
            return K_LEFT
