import sys
from classes.button import *
from classes.menu import *
from games.xoxo import *

#Ferme La fenetre
def closeGame():
    global running
    running = False
    pygame.display.quit()
    pygame.quit()
    sys.exit()

#Créer le menu du jeu et le return
def createMainMenu(SettingsMenu, PlayerSelectionMenu, HEIGHT):
    #Créer les boutons depuis la classe Button et les stocks dans une liste
    MainMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Play", None, "./font/pixel.ttf", 35, (255, 255, 255),
               PlayerSelectionMenu),
        Button("./asset/blue_button.png", 0, ((HEIGHT / 2) + 50), "Settings", None, "./font/pixel.ttf", 35,
               (255, 255, 255), SettingsMenu),
        Button("./asset/blue_button.png", 0, ((HEIGHT / 2) + 125), "Quit", closeGame, "./font/pixel.ttf", 35,
               (255, 255, 255))
    ]
    #Centre le Bouton 1 en plein millieu
    MainMenuButtons[0].centerToMiddleScreen()
    #Centre le Bouton dans l'abscisse en X
    MainMenuButtons[1].centerTheX()
    MainMenuButtons[2].centerTheX()
    #Créer le menu Principal et le stock
    MainMenu = Menu("./asset/background.png", [0, 0], MainMenuButtons, "Main Menu", None, None)
    return MainMenu


#Créer le Menu de Sélection et le return
def createPlayerSelectionMenu():
    #Liste D'images à afficher dans le menu PlayerSelectionMenu
    PlayerSelectionImages = ["./asset/male1.png", "./asset/male2.png", "./asset/female1.png", "./asset/female2.png"]
    #Les positions de chaque image pour les draw
    PlayerSelectionImagesPos = ([100, 100], [275, 100], [100, 275], [275, 275])
    #Créer les boutons depuis la classe Button et les stocks dans une liste
    PlayerSelectionMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Back", None, "./font/pixel.ttf", 35, (255, 255, 255)),
        Button("./asset/blue_button.png", 0, 0, "Xoxo", None, "./font/pixel.ttf", 25, (255, 255, 255), createXoxo())
    ]
    #Centre le Bouton 1 en plein millieu
    PlayerSelectionMenuButtons[1].centerToMiddleScreen()
    #Créer le menu PlayerSelection et le stock
    PlayerSelectionMenu = Menu("./asset/background.png", [0, 0], PlayerSelectionMenuButtons, "Player Selection Menu",
                               PlayerSelectionImages, PlayerSelectionImagesPos)
    #Load les images pour les draw
    PlayerSelectionMenu.loadImages()
    return PlayerSelectionMenu

#Créer le menu de settings et le return
def createSettingsMenu():
    #Créer les boutons depuis la classe Button et les stocks dans une liste
    SettingsMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Back", None, "./font/pixel.ttf", 35, (255, 255, 255))
    ]
    #Créer le menu Settings et le stock
    SettingsMenu = Menu("./asset/background.png", [0, 0], SettingsMenuButtons, "Setting Menu", None, None)
    return SettingsMenu
