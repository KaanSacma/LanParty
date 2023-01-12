import pygame

from launcher import *

running = True


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
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption('Tech Party')

    PlayerSelectionMenu = createPlayerSelectionMenu()
    SettingsMenu = createSettingsMenu()
    MainMenu = createMainMenu(SettingsMenu, PlayerSelectionMenu, HEIGHT)
    SettingsMenu.buttons[0].linkedMenu = MainMenu
    PlayerSelectionMenu.buttons[0].linkedMenu = MainMenu

    currentMenu = MainMenu
    currentMenu.setName()

    while running:
        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                closeGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hasattr(currentMenu, "buttons"):
                    for button in currentMenu.buttons:
                        if hasattr(button, "isOver") and button.isOver(mousePos):
                            if button.linkedMenu:
                                currentMenu = button.linkedMenu
                                currentMenu.setName()
                                print(currentMenu.name)
                            if currentMenu.name != "Xoxo" and button.onClick is not None:
                                button.onClick()
                            elif currentMenu.name == "Xoxo" and not currentMenu.canPlay:
                                button.onClick()
                if hasattr(currentMenu, "images"):
                    if (currentMenu.name == "Xoxo") and (currentMenu.canPlay == True):
                        for i in range(len(currentMenu.images)):
                            if currentMenu.isOver(mousePos, i):
                                currentMenu.addChoice(i)
        window.fill((255, 255, 255))
        currentMenu.drawBackground(window)
        if currentMenu.images is not None:
            currentMenu.drawImages(window)
        if hasattr(currentMenu, 'buttons') and currentMenu.name != "Xoxo":
            currentMenu.drawButtons(window)
        if currentMenu.name == "Xoxo":
            currentMenu.drawChoiceImages(window)
            if not currentMenu.canPlay:
                window.blit(currentMenu.text,((WIDTH / 2) - 150, 50))
                currentMenu.drawButtons(window)
        pygame.display.update()


if __name__ == '__main__':
    main()