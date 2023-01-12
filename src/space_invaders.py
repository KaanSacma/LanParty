import math
import random
import pygame as py
import pygame
import sys
import os
from pygame.locals import *

py.init() 

clock = py.time.Clock()

# Screen + Background
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH / 2, HEIGHT))
background = py.image.load("background.jpg").convert()

# Icon+captions
py.display.set_caption("Space Invader!")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Ship
shipIcon = pygame.image.load("spaceship.png")
new_ship = pygame.transform.scale(shipIcon, (80, 90))
ship_x = 370
ship_y = 700
ship_xchange = 0

# Lasers
laserfirst = pygame.image.load("newlaser.jpg")
laser = pygame.transform.scale(laserfirst, (15, 60))
laser_x = 15
laser_y = 700
laser_xchange = 0
laser_ychange = 5
laser_state = "ready"

# Enemies
enemy_icon = []
enemy_x = []
enemy_y = []
enemy_xchange = []
enemy_ychange = []
enemiesNumber = 8

for i in range(enemiesNumber):
    enemy_icon.append(pygame.image.load('pigeon.png'))
    enemy_x.append(random.randint(0, 650))
    enemy_y.append(random.randint(20, 150))
    enemy_xchange.append(2)
    enemy_ychange.append(25)


# Texts
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
go_font = pygame.font.Font('freesansbold.ttf', 64)
Xsize = 10
Ysize = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over():
    over_text = go_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (180, 250))

def ship(x, y):
    screen.blit(new_ship, (x, y))

def shoot_laser(x, y):
    global laser_state
    laser_state = "shoot"
    screen.blit(laser, (x + 16, y + 5))

def enemy(x, y, i):
    screen.blit(enemy_icon[i], (x, y))

def isCollision(enemy_x, enemy_y, laser_x, laser_y):
    distance = math.sqrt(math.pow(enemy_x - laser_x, 2) + (math.pow(enemy_y - laser_y, 2)))
    if distance < 28:
        return True
    else:
        return False

# Main loop
while 1:

    # Delete/refresh Screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in py.event.get():
        if event.type == py.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_xchange = -2
            if event.key == pygame.K_RIGHT:
                ship_xchange = 2
            if event.key == pygame.K_SPACE:
                if laser_state == "ready":
                    laser_x = ship_x + 10
                    shoot_laser(laser_x, laser_y)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship_xchange = 0


    ship_x += ship_xchange
    if ship_x <= 20:
        ship_x = 20
    elif ship_x >= 655:
        ship_x = 655
    
    for i in range(enemiesNumber):
        # Game Over
        if enemy_y[i] > 540:
            for j in range(enemiesNumber):
                enemy_y[j] = 2000
            game_over()
            break

        enemy_x[i] += enemy_xchange[i]
        if enemy_x[i] <= 0:
            enemy_xchange[i] = 2
            enemy_y[i] += enemy_ychange[i]
        elif enemy_x[i] >= 665:
            enemy_xchange[i] = -2
            enemy_y[i] += enemy_ychange[i]

    # Collision
        collision = isCollision(enemy_x[i], enemy_y[i], laser_x, laser_y)
        if collision:
            laser_y = 580
            laser_state = "ready"
            score_value += 500
            enemy_x[i] = random.randint(0, 650)
            enemy_y[i] = random.randint(30, 120)

        enemy(enemy_x[i], enemy_y[i], i)

    # Laser Move
    if laser_y <= 0:
        laser_y = 625
        laser_state = "ready"
    
    if laser_state == "shoot":
        shoot_laser(laser_x, laser_y)
        laser_y -= laser_ychange

    # Afficher le sprite à sa new pos
    ship(ship_x, ship_y)
    show_score(Xsize, Ysize)
    pygame.display.flip()
  
    # py.display.update()
  
py.quit()