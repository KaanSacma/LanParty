def getCurrentMap():
    with open('./maps/bomberman/map1.txt') as f:
        mapLines = f.read().splitlines()
    return mapLines

def getListCurrentMapImage():
    mapLines = getCurrentMap()
    LENGTH = len(mapLines)
    IMAGES_LIST = [[None] * LENGTH] * LENGTH
    for i in range(len(mapLines)):
        for j in range(len(mapLines[i])):
            currentChar = mapLines[i][j]
            if currentChar == '-':
                IMAGES_LIST[i][j] = "./asset/grass.png"
            else:
                IMAGES_LIST[i][j] = ""
    return IMAGES_LIST

def getPositionCurrentMap():
    IMAGE_LIST = getListCurrentMapImage()
    LENGTH = len(IMAGE_LIST)
    START_POINT = [100, 100]
    IMAGES_POSITIONS = [[(100, 100)] * LENGTH] * LENGTH
    print(IMAGES_POSITIONS)


#def createBomberman():