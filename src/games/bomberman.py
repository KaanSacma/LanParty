def getMaps():
    with open('../../maps/bomberman/map1.txt') as f:
        lines = f.read().splitlines()
    print(lines)

#def createBomberman():