import pygame
from classes.button import *
from classes.menu import *

def printMessage(string):
    print(string)

def main():
    pygame.init()
    window = pygame.display.set_mode((400, 500))
    pygame.display.set_caption('Tech Party')

    MainMenuButtons = [Button((0, 255, 0), 150, 225, 250, 100, "Play", printMessage)]
    MainMenuButtons[0].centerIt()
    MainMenu = Menu("./src/asset/background.png", [0, 0], MainMenuButtons, "Main Menu")
    MainMenu.setName()
    running = True

    while running:
        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in MainMenu.buttons:
                    if button.isOver(mousePos):
                        button.onClick("Coucou tu m'as cliqué")
            if event.type == pygame.MOUSEMOTION:
                for button in MainMenu.buttons:
                    if button.isOver(mousePos):
                        button.color = (255, 0, 0)
                    else:
                        button.color = (0, 255, 0)
        window.fill((255, 255, 255))
        MainMenu.drawBackground(window)
        MainMenu.drawButtons(window)
        pygame.display.update()

if __name__ == '__main__':
    main()