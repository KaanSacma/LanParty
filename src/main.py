import sys
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
    SettingsMenu = Menu("./asset/background.png", [0, 0], SettingsMenuButtons, "Setting Menu", None, None)

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

    MainMenuButtons = [
        Button("./asset/blue_button.png", 0, 0, "Play", None, "./font/pixel.ttf", 35, (255, 255, 255), PlayerSelectionMenu),
        Button("./asset/blue_button.png", 0, ((HEIGHT / 2) + 50), "Settings", None, "./font/pixel.ttf", 35,
               (255, 255, 255), SettingsMenu),
        Button("./asset/blue_button.png", 0, ((HEIGHT / 2) + 125), "Quit", closeGame, "./font/pixel.ttf", 35,
               (255, 255, 255))
    ]
    MainMenuButtons[0].centerToMiddleScreen()
    MainMenuButtons[1].centerTheX()
    MainMenuButtons[2].centerTheX()
    MainMenu = Menu("./asset/background.png", [0, 0], MainMenuButtons, "Main Menu", None, None)
    SettingsMenu.buttons[0].linkedMenu = MainMenu
    PlayerSelectionMenu.buttons[0].linkedMenu = MainMenu

    currentMenu = MainMenu
    currentMenu.setName()
    #getMaps()

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
                        if button.onClick is not None:
                            button.onClick()
            #if event.type == pygame.MOUSEMOTION:
            #    for button in currentMenu.buttons:
            #        if button.isOver(mousePos):
            #            button.color = (255, 0, 0)
            #        else:
            #            button.color = (0, 255, 0)
        window.fill((255, 255, 255))
        currentMenu.drawBackground(window)
        if currentMenu.images is not None:
            currentMenu.drawImages(window)
        currentMenu.drawButtons(window)
        pygame.display.update()


if __name__ == '__main__':
    main()
