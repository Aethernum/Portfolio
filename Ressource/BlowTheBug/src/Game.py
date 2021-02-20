import pygame

from src import constant, windowstate
from src.Pipe import Pipe
from src.Player import Player
from src.utils import addBouton, isSoundOn, registerNewScore, getSpriteWindLeft, getSpriteWindRight


class Game:
    def __init__(self):
        self.all_sprite = pygame.sprite.Group()

        self.player1 = Player(10, 210, 1)
        self.player1.setName('1')

        self.player2 = Player(824, 210, 2)
        self.player2.setName('2')

        self.players = []
        self.players.append(self.player1)
        self.players.append(self.player2)

        self.pipe = Pipe()

        self.all_sprite.add(self.player1)
        self.all_sprite.add(self.player2)

        self.bg = pygame.image.load('assets/Background/gameBG.png').convert()
        self.bg = pygame.transform.scale(self.bg, constant.SCREEN_SIZE)
        self.rect = self.bg.get_rect()

        self.power = []
        for i in range(1,12):
            self.power.append(pygame.image.load('assets/HUD/power' + str(i) + '.png').convert_alpha())
        self.powerRect = self.power[0].get_rect()
        self.powerRect.x = 25
        self.powerRect.y = 600
        self.powerRect2 = self.power[0].get_rect()
        self.powerRect2.x = constant.WIDTH//2 + 25
        self.powerRect2.y = 600

        self.invasion = pygame.image.load('assets/HUD/invasion.png').convert_alpha()
        self.invasionRect = self.invasion.get_rect()
        self.invasionRect.x = 90
        self.invasionRect.y = 610
        self.invasionRect2 = self.invasion.get_rect()
        self.invasionRect2.x = constant.WIDTH // 2 + 90
        self.invasionRect2.y = 610


        self.windLeft = getSpriteWindLeft()
        self.windRight = getSpriteWindRight()

    def startGame(self, screen):
        clock = pygame.time.Clock()

        if windowstate.isBlanchon1:
            self.player1.setBlanchonHead()

        if windowstate.isBlanchon2:
            self.player2.setBlanchonHead()

        for player in self.players:
            player.combi.newRandom(4)
        count = -1
        i = 0
        key = 0
        msg_bonus = ["BONUS : appuye 5 fois sur ESPACE pour l'utiliser !", "BONUS : appuye 5 fois sur ENTREE pour l'utiliser !"]
        msg_malus = "MALUS : inversion des touches !"
        self.player1.name = windowstate.name1
        self.player2.name = windowstate.name2

        isBlow1 = False
        blowCount1 = 0
        isBlow2 = False
        blowCount2 = 0

        isRegister = False

        running = True
        while running:

            result = finish, loser = self.pipe.collide()
            applause = pygame.mixer.Sound('assets/sound/applause.ogg')
            applause.set_volume(0.02)

            # Si fini afficher fin
            if finish:
                isBlow1 = False
                isBlow2 = False
                if isSoundOn():
                    applause.play()
                gameOver = pygame.image.load('assets/Background/background_menu.png').convert()
                gameOver = pygame.transform.scale(gameOver, constant.SCREEN_SIZE)
                gameOverRect = gameOver.get_rect()
                screen.blit(gameOver, gameOverRect)

                text = pygame.image.load('assets/victoire.png')
                textRect = text.get_rect()
                textRect.center = screen.get_rect().center
                textRect.y -= 150
                screen.blit(text, textRect)

                if loser == 'left':
                    winnerName = self.player2.name
                    loserName = self.player1.name
                    winnerScore = self.player2.combi.score
                    loserScore = self.player1.combi.score
                else:
                    winnerName = self.player1.name
                    loserName = self.player2.name
                    winnerScore = self.player1.combi.score
                    loserScore = self.player2.combi.score

                font = pygame.font.Font(None, 40)
                textWinner = font.render("Bravo " + winnerName + " ! Ton score est de : " + str(winnerScore), True, constant.WHITE)
                winnerRect = textWinner.get_rect()
                winnerRect.center = screen.get_rect().center
                winnerRect.y = winnerRect.y + 50
                screen.blit(textWinner, winnerRect)

                textLoser = font.render(loserName + " ton score est de : " + str(loserScore), True, constant.LIGHT_GRAY)
                loserRect = textLoser.get_rect()
                loserRect.center = winnerRect.center
                loserRect.y = loserRect.y + 50
                screen.blit(textLoser, loserRect)
                menu = addBouton(screen, None, 'back', 5, 5, 30, 30)

                if not isRegister:
                    registerNewScore(winnerName, winnerScore)
                    registerNewScore(loserName, loserScore)
                    isRegister = True

            # Si jeu en cours
            else:
                screen.blit(self.bg, self.rect)
                menu = addBouton(screen, None, 'back_black', 5, 5, 30, 30)
                self.all_sprite.draw(screen)
                screen.blit(self.pipe.image, self.pipe.rect)
                screen.blit(self.pipe.ball.image, self.pipe.ball.rect)

                # Affichage de la combinaison et du score actuel
                font = pygame.font.Font(None, 40)
                for pl in self.players:
                    if(pl.malus[3]):
                        number = 3
                    else:
                      number = 0
                    # Affichage de la combinaison
                    for key in pl.combi.goal:
                        pos = pl.pos[0] + number * 80, pl.pos[1]
                        screen.blit(key, pos)
                        if (pl.malus[3]):
                            number -= 1
                        else:
                            number += 1
                    # affichage du score
                    text = font.render("Score actuel : " + str(pl.combi.score), 1, (255, 255, 255))
                    screen.blit(text, pl.scorePos)
                    # affichage du nom du joueur
                    text = font.render(pl.name, 1, constant.BLACK)

                    screen.blit(text, pl.namePos)


                screen.blit(self.power[self.player1.bonus*2], self.powerRect)
                screen.blit(self.power[self.player2.bonus*2], self.powerRect2)

                if self.player1.malus[1]:
                    screen.blit(self.invasion, self.invasionRect)
                if self.player2.malus[1]:
                    screen.blit(self.invasion, self.invasionRect2)

                if self.player1.malus[2]:
                    self.player1.temps += 1
                    if self.player1.temps >= 0 and self.player1.temps < 15:
                        text_temps = font.render("3", 1, constant.RED)
                        text_temps_pos = (constant.WIDTH // 4 + 130, 560)
                        screen.blit(text_temps, text_temps_pos)
                    elif self.player1.temps >= 15 and self.player1.temps < 30:
                        text_temps = font.render("2", 1, constant.RED)
                        text_temps_pos = (constant.WIDTH // 4 + 130, 560)
                        screen.blit(text_temps, text_temps_pos)
                    elif self.player1.temps >= 30 and self.player1.temps < 45:
                        text_temps = font.render("1", 1, constant.RED)
                        text_temps_pos = (constant.WIDTH // 4 + 130, 560)
                        screen.blit(text_temps, text_temps_pos)
                    elif self.player1.temps == 45:
                        self.player1.combi.newRandom(4)
                        self.player1.temps = -1
                        error = pygame.mixer.Sound('assets/sound/error.ogg')
                        error.set_volume(0.02)
                        if isSoundOn():
                            error.play()

                if self.player2.malus[2]:
                    self.player2.temps += 1
                    if self.player2.temps >= 0 and self.player2.temps < 15:
                        text_temps = font.render("3", 1, constant.RED)
                        text_temps_pos = (3 * constant.WIDTH // 4 + 130, 560)
                        screen.blit(text_temps, text_temps_pos)
                    elif self.player2.temps >= 15 and self.player2.temps < 30:
                        text_temps = font.render("2", 1, constant.RED)
                        text_temps_pos = (3 * constant.WIDTH // 4 + 130, 560)
                        screen.blit(text_temps, text_temps_pos)
                    elif self.player2.temps >= 30 and self.player2.temps < 45:
                        text_temps = font.render("1", 1, constant.RED)
                        text_temps_pos = (3 * constant.WIDTH // 4 + 130, 560)
                        screen.blit(text_temps, text_temps_pos)
                    elif self.player2.temps == 45:
                        self.player2.combi.newRandom(4)
                        self.player2.temps = -1
                        error = pygame.mixer.Sound('assets/sound/error.ogg')
                        error.set_volume(0.02)
                        if isSoundOn():
                            error.play()

                if self.player1.success >= 3:
                    text_bonus = font.render("BONUS", 1, constant.GREEN)
                    text_bonus_pos = (60, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    space = pygame.image.load('assets/HUD/space.png').convert_alpha()
                    space_rect = space.get_rect()
                    space_rect.x = 40
                    space_rect.y = 540
                    screen.blit(space, space_rect)
                    text_nombre = font.render("x5", 1, constant.GREEN)
                    text_nombre_pos = (170, 560)
                    screen.blit(text_nombre, text_nombre_pos)

                if self.player2.success >= 3:
                    text_bonus = font.render("BONUS", 1, constant.GREEN)
                    text_bonus_pos = (constant.WIDTH // 2 + 60, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    space = pygame.image.load('assets/HUD/enter.png').convert_alpha()
                    space_rect = space.get_rect()
                    space_rect.x = constant.WIDTH // 2 + 80
                    space_rect.y = 540
                    screen.blit(space, space_rect)
                    text_nombre = font.render("x5", 1, constant.GREEN)
                    text_nombre_pos = (constant.WIDTH // 2 + 140, 560)
                    screen.blit(text_nombre, text_nombre_pos)

                if self.player1.malus[0]:
                    text_bonus = font.render("MALUS", 1, constant.RED)
                    text_bonus_pos = (constant.WIDTH // 4 + 30, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    text_nombre = font.render("Inversion !", 1, constant.RED)
                    text_nombre_pos = (constant.WIDTH // 4 + 20, 560)
                    screen.blit(text_nombre, text_nombre_pos)

                if self.player2.malus[0]:
                    text_bonus = font.render("MALUS", 1, constant.RED)
                    text_bonus_pos = (3 * constant.WIDTH // 4 + 30, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    text_nombre = font.render("Inversion !", 1, constant.RED)
                    text_nombre_pos = (3 * constant.WIDTH // 4 + 20, 560)
                    screen.blit(text_nombre, text_nombre_pos)

                if self.player1.malus[1]:
                    text_bonus = font.render("MALUS", 1, constant.RED)
                    text_bonus_pos = (constant.WIDTH // 4 + 30, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    text_nombre = font.render("Invasion !", 1, constant.RED)
                    text_nombre_pos = (constant.WIDTH // 4 + 20, 560)
                    screen.blit(text_nombre, text_nombre_pos)

                if self.player2.malus[1]:
                    text_bonus = font.render("MALUS", 1, constant.RED)
                    text_bonus_pos = (3 * constant.WIDTH // 4 + 30, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    text_nombre = font.render("Invasion !", 1, constant.RED)
                    text_nombre_pos = (3 * constant.WIDTH // 4 + 20, 560)
                    screen.blit(text_nombre, text_nombre_pos)

                if self.player1.malus[2]:
                    text_bonus = font.render("MALUS", 1, constant.RED)
                    text_bonus_pos = (constant.WIDTH // 4 + 30, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    text_nombre = font.render("Temps :", 1, constant.RED)
                    text_nombre_pos = (constant.WIDTH // 4 + 20, 560)
                    screen.blit(text_nombre, text_nombre_pos)

                if self.player2.malus[2]:
                    text_bonus = font.render("MALUS", 1, constant.RED)
                    text_bonus_pos = (3 * constant.WIDTH // 4 + 30, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    text_nombre = font.render("Temps :", 1, constant.RED)
                    text_nombre_pos = (3 * constant.WIDTH // 4 + 20, 560)
                    screen.blit(text_nombre, text_nombre_pos)

                if self.player1.malus[3]:
                    text_bonus = font.render("MALUS", 1, constant.RED)
                    text_bonus_pos = (constant.WIDTH // 4 + 30, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    text_nombre = font.render("Miroir", 1, constant.RED)
                    text_nombre_pos = (constant.WIDTH // 4 + 20, 560)
                    screen.blit(text_nombre, text_nombre_pos)

                if self.player2.malus[3]:
                    text_bonus = font.render("MALUS", 1, constant.RED)
                    text_bonus_pos = (3 * constant.WIDTH // 4 + 30, 520)
                    screen.blit(text_bonus, text_bonus_pos)
                    text_nombre = font.render("Miroir", 1, constant.RED)
                    text_nombre_pos = (3 * constant.WIDTH // 4 + 20, 560)
                    screen.blit(text_nombre, text_nombre_pos)

            # Animation de mec qui souffle pour le joueur 1
            if isBlow1:
                if blowCount1 <= 12:
                    self.player1.blow(0)
                    blowCount1 += 1
                elif blowCount1 == 13 :
                    self.player1.image = self.player1.images[1]
                    blowCount1 += 1
                elif blowCount1 <= 20:
                    blowCount1 += 1
                elif blowCount1 <= 33 :
                    self.player1.blow(1)
                    blowCount1 += 1

                if blowCount1 == 18:
                    self.player1.image = self.player1.images[0]

                if blowCount1 == 34:
                    blowCount1 = 0
                    isBlow1 = False

                if blowCount1 > 13 and blowCount1 < 27:
                    windRect1 = self.windLeft[blowCount1-13].get_rect()
                    windRect1.x = 200
                    windRect1.y = 350
                    screen.blit(self.windLeft[blowCount1-13], windRect1)

            # Animation de mec qui souffle pour le joueur 2
            if isBlow2:
                if blowCount2 <= 12:
                    self.player2.blow(0)
                    blowCount2 += 1
                elif blowCount2 == 13:
                    self.player2.image = self.player2.images[1]
                    blowCount2 += 1
                elif blowCount2 <= 20:
                    blowCount2 += 1
                elif blowCount2 <= 33:
                    self.player2.blow(1)
                    blowCount2 += 1

                if blowCount2 == 18:
                    self.player2.image = self.player2.images[0]

                if blowCount2 == 34:
                    blowCount2 = 0
                    isBlow2 = False

                if blowCount2 > 13 and blowCount2 < 27:
                    windRect2 = self.windRight[blowCount2-13].get_rect()
                    windRect2.x = 500
                    windRect2.y = 350
                    screen.blit(self.windRight[blowCount2-13], windRect2)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.play = False

                elif event.type == pygame.KEYDOWN and finish == False:
                    # Si c'est une touche du clavier, alors on regarde si elle est parmis les touches possibles des joueurs
                    if event.key == pygame.K_SPACE and self.player1.success >= 3:
                        self.player1.bonus += 1
                        if self.player1.bonus == 5:
                            self.player2.addRandomMalus()
                            self.player1.success = 0
                    elif event.key == pygame.K_RETURN and self.player2.success >= 3:
                        self.player2.bonus += 1
                        if self.player2.bonus == 5:
                            self.player1.addRandomMalus()
                            self.player2.success = 0
                    else:
                        for pl in self.players:
                            try:
                                key = eval("pygame.K_" + event.unicode)
                            except:
                                key = event.key
                            if pl.combi.keysValue.count(key) > 0:
                                count = i  # On prend le numéro du joueur dans players à qui appartient la touche
                            i += 1
                    if count != -1:  # Si la touche appartient à un joueur, alors on appelle tried pour essayé la combinaison
                        if self.players[count].malus[0]:
                            key = self.players[count].combi.reverse(key)
                        self.players[count].combi.tried(key)
                        if self.players[count].combi.state == -1:
                            error = pygame.mixer.Sound('assets/sound/error.ogg')
                            error.set_volume(0.02)
                            if isSoundOn():
                                error.play()
                            self.players[count].success = 0
                            self.players[count].combi.newRandom(4)  # newRandom(4) 4 = taille de la combinaison à changer
                            self.players[count].temps = -1
                        elif self.players[count].combi.state == 1:
                            if count == 1:
                                isBlow2 = True
                            else:
                                isBlow1 = True
                            blow = pygame.mixer.Sound('assets/sound/blow.ogg')
                            blow.set_volume(0.4)
                            if isSoundOn():
                                blow.play()
                            if not self.players[(count +1) % 2].haveMalus():
                                self.players[count].success += 1
                            if self.players[count].haveMalus():
                                self.players[(count + 1) % 2].bonus = 0
                                self.players[count].malus[self.players[count].whichMalus()] = False
                            self.players[count].temps = -1

                            self.players[count].combi.newRandom(4)
                            if count == 0:
                                self.pipe.moveRight()
                            else:
                                self.pipe.moveLeft()

                    count = -1
                    i = 0

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if menu.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.play = False
                        running = False
            clock.tick(constant.FPS)