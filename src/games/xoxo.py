import pygame

from classes.game import *
from classes.button import *


class Xoxo(Game):
    def __init__(self, backgroundImage, position, name, images, imagesPos, buttons, scores):
        super().__init__(backgroundImage, position, name, images, imagesPos, buttons, scores)
        self.ChoiceImages = ["", "", "",
                             "", "", "",
                             "", "", ""]
        self.ChoiceImagesRects = [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
                                  (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
                                  (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
        self.Choice = 'X'
        self.StockChoice = ["", "", "",
                            "", "", "",
                            "", "", ""]
        self.canPlay = True
        self.font = pygame.font.Font("./font/pixel.ttf", 32)
        self.text = ""

    def resetXoxo(self):
        self.ChoiceImages = ["", "", "",
                             "", "", "",
                             "", "", ""]
        self.ChoiceImagesRects = [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
                                  (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
                                  (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
        self.StockChoice = ["", "", "",
                            "", "", "",
                            "", "", ""]
        self.Choice = 'X'
        self.canPlay = True

    def isOver(self, pos, i):
        if self.imagesPos[i][0] < pos[0] < self.imagesPos[i][0] + 70:
            if self.imagesPos[i][1] < pos[1] < self.imagesPos[i][1] + 70:
                return True
        return False

    def addChoice(self, i):
        if self.ChoiceImages[i] == "":
            SquarePos = self.imagesPos[i]
            if self.Choice == 'X':
                self.ChoiceImages[i] = pygame.image.load("./asset/X.png")
                self.StockChoice[i] = 'X'
                self.Choice = 'O'
            else:
                self.ChoiceImages[i] = pygame.image.load("./asset/O.png")
                self.StockChoice[i] = 'O'
                self.Choice = 'X'
            self.ChoiceImagesRects[i] = self.ChoiceImages[i].get_rect()
            self.ChoiceImagesRects[i].left, self.ChoiceImagesRects[i].top = SquarePos
            self.checkWin()

    def isSameChoice(self, pos1, pos2, pos3):
        if (len(self.StockChoice[pos1]) == 0) or (len(self.StockChoice[pos2]) == 0) or (
                len(self.StockChoice[pos3]) == 0):
            return False
        if (self.StockChoice[pos1] == self.StockChoice[pos2]) and (self.StockChoice[pos2] == self.StockChoice[pos3]):
            return True
        return False

    def drawChoiceImages(self, window):
        for i in range(len(self.ChoiceImages)):
            if type(self.ChoiceImages[i]) is pygame.Surface:
                window.blit(self.ChoiceImages[i], self.ChoiceImagesRects[i])

    def setTextWinner(self):
        if self.Choice == 'X':
            self.text = self.font.render("The Winner is O", 1, (255, 255, 255))
        else:
            self.text = self.font.render("The Winner is X", 1, (255, 255, 255))

    def checkWin(self):
        if self.isSameChoice(0, 1, 2) or self.isSameChoice(3, 4, 5) or self.isSameChoice(6, 7, 8):
            self.canPlay = False
            self.setTextWinner()
        elif self.isSameChoice(0, 3, 6) or self.isSameChoice(1, 4, 7) or self.isSameChoice(2, 5, 8):
            self.canPlay = False
            self.setTextWinner()
        elif self.isSameChoice(0, 4, 8) or self.isSameChoice(2, 4, 6):
            self.canPlay = False
            self.setTextWinner()


def createXoxo():
    XoxoButtons = [
        Button("./asset/blue_button.png", 0, 0, "Back", None, "./font/pixel.ttf", 35, (255, 255, 255)),
        Button("./asset/blue_button.png", 500, 500, "Continue", None, "./font/pixel.ttf", 25, (255, 255, 255), None)
    ]
    GameXoxoImages = [
        "./asset/square.png", "./asset/square.png", "./asset/square.png",
        "./asset/square.png", "./asset/square.png", "./asset/square.png",
        "./asset/square.png", "./asset/square.png", "./asset/square.png"
    ]
    GameXoxoPos = [
        (100, 100), (180, 100), (260, 100),
        (100, 180), (180, 180), (260, 180),
        (100, 260), (180, 260), (260, 260)
    ]
    GameXoxo = Xoxo("./asset/background.png", [0, 0], "Xoxo", GameXoxoImages, GameXoxoPos, XoxoButtons, [0, 0])
    GameXoxo.loadImages()
    GameXoxo.buttons[1].onClick = GameXoxo.resetXoxo
    return GameXoxo
