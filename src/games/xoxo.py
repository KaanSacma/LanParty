import pygame, sys

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
        self.count = 0

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
        self.count = 0

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
            self.count += 1
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

    def save_score(self, score1, score2):
        save = "X:" + str(score1) + "\nO:" + str(score2)
        with open("save.txt", "w+") as fichier:
            fichier.write(save)
        fichier.close()

    def setTextWinner(self):
        if self.Choice == 'X':
            self.scores[1] += 1
            self.save_score(self.scores[0], self.scores[1])
            self.text = self.font.render("The Winner is O: " + str(self.scores[1]), 1, (255, 255, 255))
        else:
            self.scores[0] += 1
            self.save_score(self.scores[0], self.scores[1])
            self.text = self.font.render("The Winner is X: " + str(self.scores[0]), 1, (255, 255, 255))

    def checkWin(self):
        if self.isSameChoice(0, 1, 2) or self.isSameChoice(3, 4, 5) or self.isSameChoice(6, 7, 8):
            self.canPlay = False
            self.setTextWinner()
            return ()
        elif self.isSameChoice(0, 3, 6) or self.isSameChoice(1, 4, 7) or self.isSameChoice(2, 5, 8):
            self.canPlay = False
            self.setTextWinner()
            return ()
        elif self.isSameChoice(0, 4, 8) or self.isSameChoice(2, 4, 6):
            self.canPlay = False
            self.setTextWinner()
            return ()
        if self.count == 9:
            self.canPlay = False
            self.text = self.font.render("It's a Draw", 1, (255, 255, 255))
            return ()

def loadScore():
    save = open("save.txt", "r")
    contents = save.read()
    contents_array = contents.split("\n")
    x = contents_array[0].split(":")
    o = contents_array[1].split(":")
    return([int(x[1]), int(o[1])])

def closeGame():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def createXoxo():
    XoxoButtons = [
        Button("./asset/blue_button.png", 40, 40, "Back", None, "./font/pixel.ttf", 35, (255, 255, 255)),
        Button("./asset/blue_button.png", 640, 540, "Continue", None, "./font/pixel.ttf", 25, (255, 255, 255), None),
        Button("./asset/blue_button.png", 1300, 40, "Quit", closeGame, "./font/pixel.ttf", 25, (255, 255, 255), None)
    ]
    GameXoxoImages = [
        "./asset/square.png", "./asset/square.png", "./asset/square.png",
        "./asset/square.png", "./asset/square.png", "./asset/square.png",
        "./asset/square.png", "./asset/square.png", "./asset/square.png"
    ]
    GameXoxoPos = [
        (620, 300), (700, 300), (780, 300),
        (620, 380), (700, 380), (780, 380),
        (620, 460), (700, 460), (780, 460)
    ]
    GameXoxo = Xoxo("./asset/background.png", [0, 0], "Xoxo", GameXoxoImages, GameXoxoPos, XoxoButtons, loadScore())
    GameXoxo.loadImages()
    GameXoxo.buttons[0].onClick = GameXoxo.resetXoxo
    GameXoxo.buttons[1].onClick = GameXoxo.resetXoxo
    return GameXoxo
