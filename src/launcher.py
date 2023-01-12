import sys, os
from classes.button import *
from classes.menu import *
from games.xoxo import *

def closeGame():
    global running
    running = False
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def launchSpaceInvader():
    os.system("python3 src/space_invaders.py")

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
    MainMenu.buttons[0].linkedMenu.buttons[1].linkedMenu.buttons[0].linkedMenu = PlayerSelectionMenu
    return MainMenu


def createPlayerSelectionMenu():
    PlayerSelectionImagesPos = ([100, 100], [275, 100], [100, 275], [275, 275])
    PlayerSelectionMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Back", None, "./font/pixel.ttf", 35, (255, 255, 255)),
        Button("./asset/blue_button.png", 660, 540, "Xoxo", None, "./font/pixel.ttf", 25, (255, 255, 255), createXoxo()),
        Button("./asset/blue_button.png", 660, 600, "Space Invaders", launchSpaceInvader, "./font/pixel.ttf", 25, (255, 255, 255), None),
    ]
    PlayerSelectionMenu = Menu("./asset/background.png", [0, 0], PlayerSelectionMenuButtons, "Player Selection Menu",
                               None, PlayerSelectionImagesPos)
    PlayerSelectionMenu.loadImages()
    return PlayerSelectionMenu

def createSettingsMenu():
    SettingsMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Back", None, "./font/pixel.ttf", 35, (255, 255, 255))
    ]
    SettingsMenu = Menu("./asset/background.png", [0, 0], SettingsMenuButtons, "Setting Menu", None, None)
    return SettingsMenu
