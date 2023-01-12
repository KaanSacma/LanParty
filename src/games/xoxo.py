import pygame

from classes.game import *


class Xoxo(Game):
    def __init__(self, backgroundImage, position, name, images, imagesPos, scores):
        super().__init__(backgroundImage, position, name, images, imagesPos, scores)
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

    def printWinner(self):
        if self.Choice == 'X':
            print("The winner is O")
        else:
            print("The winner is X")
    def checkWin(self):
        if self.isSameChoice(0, 1, 2) or self.isSameChoice(3, 4, 5) or self.isSameChoice(6, 7, 8):
            self.printWinner()
        elif self.isSameChoice(0, 3, 6) or self.isSameChoice(1, 4, 7) or self.isSameChoice(2, 5, 8):
            self.printWinner()
        elif self.isSameChoice(0, 4, 8) or self.isSameChoice(2, 4, 6):
            self.printWinner()


def createXoxo():
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
    GameXoxo = Xoxo("./asset/background.png", [0, 0], "Xoxo", GameXoxoImages, GameXoxoPos, [0, 0])
    GameXoxo.loadImages()
    return GameXoxo
