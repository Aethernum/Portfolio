import pygame

from src import constant


class InputBox:
    def __init__(self, x, y, h, w, text=''):
        self.image = pygame.Surface((h, w))
        self.image.fill(constant.GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        self.active = False
        self.font = pygame.font.Font(None, 50)
        self.color = constant.BLACK
        self.txt_surface = self.font.render(text, True, self.color)

    def h_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if self.active:
            self.color = constant.WHITE
        else:
            self.color = constant.BLACK
        if event.type == pygame.KEYDOWN and event.key != pygame.K_TAB:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 10))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


