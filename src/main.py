from launcher import *
from games.bomberman import *

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
    #Récupere les info du display de l'ordinateur
    info = pygame.display.Info()
    #Récupere le Width et le Height du display de l'ordinateur
    WIDTH, HEIGHT = info.current_w, info.current_h
    window = pygame.display.set_mode((WIDTH / 2, HEIGHT))
    pygame.display.set_caption('Tech Party')

    #Crée le PlayerSelectMenu
    PlayerSelectionMenu = createPlayerSelectionMenu()
    #Crée le SettingsMenu
    SettingsMenu = createSettingsMenu()
    #Crée le MainMenu
    MainMenu = createMainMenu(SettingsMenu, PlayerSelectionMenu, HEIGHT)
    #Met pour le Bouton 1 du SettingsMenu qu'au click il doit switch à MainMenu
    SettingsMenu.buttons[0].linkedMenu = MainMenu
    #Met pour le Bouton 1 du PlayerSelectionMenu qu'au click il doit switch à MainMenu
    PlayerSelectionMenu.buttons[0].linkedMenu = MainMenu

    #Stock le Menu Actuelle pour MainMenu
    currentMenu = MainMenu
    #Change Le nom du fenetre avec le nom du Menu
    currentMenu.setName()

    while running:
        for event in pygame.event.get():
            #Stock la position de la souris
            mousePos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                closeGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Loop dans toute la liste des boutons du CurrentMenu
                for button in currentMenu.buttons:
                    #Si la souris est sûr le boutton
                    if button.isOver(mousePos):
                        #Si le boutton possède le Menu à Switch
                        if button.linkedMenu:
                            #Change le CurrentMenu celui que le boutton posssède
                            currentMenu = button.linkedMenu
                            #Change le nom de la fenetre avec le nom du Menu
                            currentMenu.setName()
                            #Print le nom du Menu Suivant
                            print(currentMenu.name)
                        #Si le boutton possède une fonction à executuer
                        if button.onClick is not None:
                            #Execute la fonction du boutton
                            button.onClick()
        window.fill((255, 255, 255))
        #Draw le background du CurrentMenu
        currentMenu.drawBackground(window)
        #Si le CurrentMenu à des images à draw
        if currentMenu.images is not None:
            #Draw les images
            currentMenu.drawImages(window)
        #Draw les bouttons du CurrentMenu
        currentMenu.drawButtons(window)
        pygame.display.update()


if __name__ == '__main__':
    main()
