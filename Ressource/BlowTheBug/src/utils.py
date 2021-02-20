import json

import pygame

from src import constant


def addBouton(screen, text, icon, x, y, width, height):
    font = pygame.font.SysFont('Helvetic', 50)
    if icon:
        image = pygame.image.load("assets/" + icon + ".png")
        image = pygame.transform.scale(image, (width, height))
        rect = image.get_rect()
        rect.x = x
        rect.y = y

        text_1 = font.render(text, 1, constant.WHITE)
        rect_text = text_1.get_rect()

        rect_text.center = rect.center
        rect_text.y = rect.y + rect.height + 10

    else:
        image = pygame.image.load('assets/Sign/bouton.png')
        image = pygame.transform.scale(image, (width, height))
        text_1 = font.render(text, 1, constant.BLACK)
        rect_text = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y + 10)
        rect = image.get_rect()
        rect.x = x
        rect.y = y

    screen.blit(image, rect)
    screen.blit(text_1, rect_text)
    return rect

def getBestPlayer():
    with open('jsonFile/score.json') as json_file:
        data = json.load(json_file)
        toReturn = sorted(data['score'], key=lambda player: player['highscore'], reverse=True)
        return toReturn[0:4]

def toggleMusic():
    with open('jsonFile/config.json') as json_file:
        data = json.load(json_file)
    active = data['music'][0]['active']

    if active:
        data['music'][0]['active'] = 0
        pygame.mixer.music.stop()
    else:
        data['music'][0]['active'] = 1
        pygame.mixer.music.play()

    with open('jsonFile/config.json', "w") as jsonFile:
        json.dump(data, jsonFile)

def toggleSound():
    with open('jsonFile/config.json') as json_file:
        data = json.load(json_file)
    active = data['sound'][0]['active']

    if active:
        data['sound'][0]['active'] = 0
    else:
        data['sound'][0]['active'] = 1

    with open('jsonFile/config.json', "w") as jsonFile:
        json.dump(data, jsonFile)

def isSoundOn():
    with open('jsonFile/config.json') as json_file:
        data = json.load(json_file)
    return data['sound'][0]['active']

def isMusicOn():
    with open('jsonFile/config.json') as json_file:
        data = json.load(json_file)
    return data['music'][0]['active']

def registerNewScore(name, score):
    with open('jsonFile/score.json') as json_file:
        data = json.load(json_file)
    players = data['score']

    playerFind = False
    for player in players:
        if player['name'] == name:
            if player['highscore'] < score:
                player['highscore'] = score
                playerFind = True

    if not playerFind:
        players.append({'name': name, 'highscore': score})

    with open('jsonFile/score.json', "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

def getSpriteWindLeft():
    toReturn = []
    for i in range(1, 15):
        path = "assets/wind/Wind" + str(i) + ".png"
        tempImage = pygame.image.load(path).convert_alpha()
        tempImage = pygame.transform.flip(tempImage, True, False)
        tempImage = pygame.transform.scale(tempImage, (400, 50))
        toReturn.append(tempImage)
    return toReturn

def getSpriteWindRight():
    toReturn = []
    for i in range(1, 15):
        path = "assets/wind/Wind" + str(i) + ".png"
        tempImage = pygame.image.load(path).convert_alpha()
        tempImage = pygame.transform.scale(tempImage, (400, 50))
        toReturn.append(tempImage)
    return toReturn
