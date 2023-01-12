import pygame

class Menu:
    def __init__(self, backgroundImage, position, buttons, name, images, imagesPos):
        self.background = pygame.image.load(backgroundImage)
        self.buttons = buttons
        self.name = name
        self.images = images
        self.imagesPos = imagesPos
        self.imagesLoaded = images
        self.rect = self.background.get_rect()
        self.rect.left, self.rect.top = position
        if images is not None:
            self.rects = list(imagesPos)

    def loadImages(self):
        if self.images is not None:
            for i in range(len(self.images)):
                self.imagesLoaded[i] = pygame.image.load(self.images[i])
                self.imagesLoaded[i] = pygame.transform.scale(self.imagesLoaded[i], (125, 125))
                self.rects[i] = self.imagesLoaded[i].get_rect()
                self.rects[i].left, self.rects[i].top = self.imagesPos[i]

    def setName(self):
        pygame.display.set_caption('Tech Party - ' + self.name)

    def drawImages(self, window):
        for i in range(len(self.imagesLoaded)):
            window.blit(self.imagesLoaded[i], self.rects[i])
    def drawBackground(self, window):
        window.fill([255, 255, 255])
        window.blit(self.background, self.rect)

    def drawButtons(self, window, outline=None):
        for button in self.buttons:
            button.draw(window, outline)
