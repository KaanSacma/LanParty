import pygame


class Menu:
    def __init__(self, backgroundImage, position, buttons, name):
        self.background = pygame.image.load(backgroundImage)
        self.buttons = buttons
        self.name = name
        self.rect = self.background.get_rect()
        self.rect.left, self.rect.top = position

    def setName(self):
        pygame.display.set_caption('Tech Party - ' + self.name)

    def drawBackground(self, window):
        window.fill([255, 255, 255])
        window.blit(self.background, self.rect)

    def drawButtons(self, window, outline=None):
        for button in self.buttons:
            button.draw(window, outline)
