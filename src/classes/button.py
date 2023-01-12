import pygame


class Button:
    def __init__(self, baseImage, x, y, text='', onClick=None, fontPath="./font/pixel.ttf", fontSize=35, fontColor=(0, 0, 0), linkedMenu=None):
        self.baseImage = pygame.image.load(baseImage)
        self.x = x
        self.y = y
        self.text = text
        self.onClick = onClick
        self.fontPath = fontPath
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.linkedMenu = linkedMenu
        self.rect = self.baseImage.get_rect()
        self.width = self.rect.right
        self.height = self.rect.bottom
        self.rect.left, self.rect.top = [self.x, self.y]

    def draw(self, window, outline=None):
        window.blit(self.baseImage, self.rect)
        if self.text != '':
            font = pygame.font.Font(self.fontPath, self.fontSize)
            text = font.render(self.text, 1, self.fontColor)
            window.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2),
                      self.y + (self.height / 2 - text.get_height() / 2)))
    def centerToMiddleScreen(self):
        w, h = pygame.display.get_surface().get_size()
        self.x = (w / 2) - (self.width / 2)
        self.y = (h / 2) - (self.height / 2)
        self.rect.left, self.rect.top = [self.x, self.y]

    def centerTheX(self):
        w, h = pygame.display.get_surface().get_size()
        self.x = (w / 2) - (self.width / 2)
        self.rect.left, self.rect.top = [self.x, self.y]

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
