import sys
from classes.button import *
from classes.menu import *

def closeGame():
    global running
    running = False
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def createMainMenu(SettingsMenu, PlayerSelectionMenu, HEIGHT):
    MainMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Play", None, "./font/pixel.ttf", 35, (255, 255, 255),
               PlayerSelectionMenu),
        Button("./asset/blue_button.png", 0, ((HEIGHT / 2) + 50), "Settings", None, "./font/pixel.ttf", 35,
               (255, 255, 255), SettingsMenu),
        Button("./asset/blue_button.png", 0, ((HEIGHT / 2) + 125), "Quit", closeGame, "./font/pixel.ttf", 35,
               (255, 255, 255))
    ]
    MainMenuButtons[0].centerToMiddleScreen()
    MainMenuButtons[1].centerTheX()
    MainMenuButtons[2].centerTheX()
    MainMenu = Menu("./asset/background.png", [0, 0], MainMenuButtons, "Main Menu", None, None)
    return MainMenu


def createPlayerSelectionMenu():
    PlayerSelectionImages = ["./asset/male1.png", "./asset/male2.png", "./asset/female1.png", "./asset/female2.png"]
    PlayerSelectionImagesPos = ([100, 100], [275, 100], [100, 275], [275, 275])
    PlayerSelectionMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Back", None, "./font/pixel.ttf", 35, (255, 255, 255)),
        Button("./asset/blue_button.png", 0, 0, "Bomberman", None, "./font/pixel.ttf", 25, (255, 255, 255))
    ]
    PlayerSelectionMenuButtons[1].centerToMiddleScreen()
    PlayerSelectionMenu = Menu("./asset/background.png", [0, 0], PlayerSelectionMenuButtons, "Player Selection Menu",
                               PlayerSelectionImages, PlayerSelectionImagesPos)
    PlayerSelectionMenu.loadImages()
    return PlayerSelectionMenu


def createSettingsMenu():
    SettingsMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Back", None, "./font/pixel.ttf", 35, (255, 255, 255))
    ]
    SettingsMenu = Menu("./asset/background.png", [0, 0], SettingsMenuButtons, "Setting Menu", None, None)
    return SettingsMenu
