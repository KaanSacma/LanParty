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
    window = pygame.display.set_mode((WIDTH / 2, HEIGHT))
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
                for button in currentMenu.buttons:
                    if button.isOver(mousePos):
                        if button.linkedMenu:
                            currentMenu = button.linkedMenu
                            currentMenu.setName()
                            print(currentMenu.name)
                        if button.onClick is not None:
                            button.onClick()
        window.fill((255, 255, 255))
        currentMenu.drawBackground(window)
        if currentMenu.images is not None:
            currentMenu.drawImages(window)
        currentMenu.drawButtons(window)
        pygame.display.update()


if __name__ == '__main__':
    main()
