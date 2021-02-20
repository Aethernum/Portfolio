import json

import pygame

from src import constant, windowstate
from src.Menu import Menu
from src.Credit import Credit
from src.Settings import Settings
from src.Notice import Notice
from src.HighScore import HighScore
from src.Game import Game
from src.NamePlayer import NamePlayer

pygame.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('assets/logo.png').convert_alpha()

pygame.display.set_caption("Blow the Bug")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()

namePlayer = NamePlayer()
menu = Menu()
notice = Notice()
highscore = HighScore()
settings = Settings()
credit = Credit()

with open('jsonFile/config.json') as json_file:
    data = json.load(json_file)

pygame.mixer.music.load('assets/sound/music.ogg')
pygame.mixer.music.set_volume(0.03)

if data['music'][0]['active']:
    pygame.mixer.music.play(loops=-1)

running = True

while windowstate.credits or windowstate.highscore or windowstate.menu or windowstate.notice or windowstate.play or windowstate.settings or windowstate.playerName:
    if windowstate.menu:
        menu.startMenu(screen)
    elif windowstate.play:
        game = Game()
        game.startGame(screen)
    elif windowstate.notice:
        notice.startNotice(screen)
    elif windowstate.highscore:
        highscore.startHighScore(screen)
    elif windowstate.settings:
        settings.startSettings(screen)
    elif windowstate.credits:
        credit.startCredits(screen)
    elif windowstate.playerName:
        namePlayer.startNamePlayer(screen)

