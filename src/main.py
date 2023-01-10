import pygame, sys
from classes.button import *
from classes.menu import *

running = True


def printMessage():
    print("Coucou")


def closeGame():
    global running
    running = False
    pygame.display.quit()
    pygame.quit()
    sys.exit()


def main():
    global running
    pygame.init()
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h
    window = pygame.display.set_mode((WIDTH / 2, HEIGHT))
    pygame.display.set_caption('Tech Party')


    SettingsMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Back", None, "./font/pixel.ttf", 35, (255, 255, 255))
    ]
    SettingsMenu = Menu("./asset/background.png", [0, 0], SettingsMenuButtons, "Setting Menu")
    MainMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Play", printMessage, "./font/pixel.ttf", 35, (255, 255, 255)),
        Button("./asset/blue_button.png", 0, ((HEIGHT / 2) + 50), "Settings", None, "./font/pixel.ttf", 35,
               (255, 255, 255), SettingsMenu),
        Button("./asset/blue_button.png", 0, ((HEIGHT / 2) + 125), "Quit", closeGame, "./font/pixel.ttf", 35,
               (255, 255, 255))
    ]
    MainMenuButtons[0].centerToMiddleScreen()
    MainMenuButtons[1].centerTheX()
    MainMenuButtons[2].centerTheX()
    MainMenu = Menu("./asset/background.png", [0, 0], MainMenuButtons, "Main Menu")
    SettingsMenu.buttons[0].linkedMenu = MainMenu
    currentMenu = MainMenu
    currentMenu.setName()

    while running:
        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                closeGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in currentMenu.buttons:
                    if button.isOver(mousePos):
                        if button.linkedMenu:
                            currentMenu = button.linkedMenu
                            currentMenu.setName()
                        elif button.onClick is not None:
                            button.onClick()
            #if event.type == pygame.MOUSEMOTION:
            #    for button in currentMenu.buttons:
            #        if button.isOver(mousePos):
            #            button.color = (255, 0, 0)
            #        else:
            #            button.color = (0, 255, 0)
        window.fill((255, 255, 255))
        currentMenu.drawBackground(window)
        currentMenu.drawButtons(window)
        pygame.display.update()


if __name__ == '__main__':
    main()
