import math
import random
import pygame as py
import pygame
import sys
import os
from pygame.locals import *

py.init() 

clock = py.time.Clock()
clock.tick(60)

# Screen + Background
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = py.image.load("./asset/background.jpg").convert()

# Icon+captions
py.display.set_caption("Space Invader!")
icon = pygame.image.load("./asset/spaceship.png")
pygame.display.set_icon(icon)

# Ships
shipIcon = pygame.image.load("./asset/spaceship.png")
new_ship = pygame.transform.scale(shipIcon, (80, 90))
ship_x = 370
ship_y = 700
ship_xchange = 0

ship2Icon = pygame.image.load("./asset/spaceship2.png")
new_ship2 = pygame.transform.scale(ship2Icon, (80, 90))
ship2_x = 750
ship2_y = 700
ship2_xchange = 0


# Lasers
laserfirst = pygame.image.load("./asset/newlaser.jpg")
laser = pygame.transform.scale(laserfirst, (15, 60))
laser_x = 15
laser_y = 700
laser_xchange = 0
laser_ychange = 5
laser_state = "ready"

laser2first = pygame.image.load("./asset/newlaser2.jpg")
laser2 = pygame.transform.scale(laser2first, (15, 60))
laser2_x = 30
laser2_y = 700
laser2_xchange = 0
laser2_ychange = 5
laser2_state = "ready"

# Enemies
enemy_icon = []
enemy_x = []
enemy_y = []
enemy_xchange = []
enemy_ychange = []
enemiesNumber = 15

for i in range(enemiesNumber):
    enemy_icon.append(pygame.image.load('./asset/pigeon.png'))
    enemy_x.append(random.randint(0, 650))
    enemy_y.append(random.randint(20, 150))
    enemy_xchange.append(2)
    enemy_ychange.append(25)


# Texts
score_value = 0
score2_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
go_font = pygame.font.Font('freesansbold.ttf', 64)
Xsize = 10
Ysize = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_score2(x, y):
    score2 = font.render("Score : " + str(score2_value), True, (255, 255, 255))
    screen.blit(score2, (x, y))

def game_over():
    over_text = go_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, ((WIDTH/2) - 210, 250))
    display_winner = font.render("THE WINNER IS PLAYER ONE: " + str(score_value), True, (255, 255, 255))
    display_winner2 = font.render("THE WINNER IS PLAYER TWO: " + str(score2_value), True, (255, 255, 255))
    if score_value > score2_value:
        screen.blit(display_winner, ((WIDTH/2) - 310, 330))
    elif score2_value > score_value:
        screen.blit(display_winner2, ((WIDTH/2) - 310, 330))

def ship(x, y):
    screen.blit(new_ship, (x, y))

def ship2(x, y):
    screen.blit(new_ship2, (x, y))

def shoot_laser(x, y):
    global laser_state
    laser_state = "shoot"
    screen.blit(laser, (x + 16, y + 5))

def shoot_laser2(x, y):
    global laser2_state
    laser2_state = "shoot"
    screen.blit(laser2, (x + 16, y + 5))    

def enemy(x, y, i):
    screen.blit(enemy_icon[i], (x, y))

def isCollision(enemy_x, enemy_y, laser_x, laser_y):
    distance = math.sqrt(math.pow(enemy_x - laser_x, 2) + (math.pow(enemy_y - laser_y, 2)))
    if distance < 28:
        return True
    else:
        return False

def isCollision(enemy_x, enemy_y, laser2_x, laser2_y):
    distance = math.sqrt(math.pow(enemy_x - laser2_x, 2) + (math.pow(enemy_y - laser2_y, 2)))
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

        if event.type == pygame.KEYDOWN or event.type == pygame.K_s:
            if event.key == pygame.K_q:
                ship_xchange = -2
            if event.key == pygame.K_d:
                ship_xchange = 2
            if event.key == pygame.K_e:
                if laser_state == "ready":
                    laser_x = ship_x + 10
                    shoot_laser(laser_x, laser_y) 
            if event.key == pygame.K_LEFT:
                ship2_xchange = -2
            if event.key == pygame.K_RIGHT:
                ship2_xchange = 2
            if event.key == pygame.K_SPACE:
                if laser2_state == "ready":
                    laser2_x = ship2_x + 10
                    shoot_laser2(laser2_x, laser2_y)
        
        if event.type == pygame.KEYUP or event.type == pygame.K_z:
            if event.key == pygame.K_q or event.key == pygame.K_d:
                ship_xchange = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship2_xchange = 0

    ship_x += ship_xchange
    if ship_x <= 20:
        ship_x = 20
    elif ship_x >= 655:
        ship_x = 655
    
    ship2_x += ship2_xchange
    if ship2_x <= (WIDTH/2):
        ship2_x = (WIDTH/2)
    elif ship2_x >= (WIDTH - 80):
        ship2_x = (WIDTH - 80)
    
    for i in range(enemiesNumber):
        # Game Over
        if enemy_y[i] > 540:
            for j in range(enemiesNumber):
                enemy_y[j] = 2000
            game_over()
            break

        enemy_x[i] += enemy_xchange[i]
        if enemy_x[i] <= 0:
            enemy_xchange[i] = 4
            enemy_y[i] += enemy_ychange[i]
        elif enemy_x[i] >= (WIDTH - 80):
            enemy_xchange[i] = -4
            enemy_y[i] += enemy_ychange[i]

    # Collision
        collision = isCollision(enemy_x[i], enemy_y[i], laser_x, laser_y)
        collision2 = isCollision(enemy_x[i], enemy_y[i], laser2_x, laser2_y)
        
        if collision:
            laser_y = 580
            laser_state = "ready"
            score_value += 500
            enemy_x[i] = random.randint(0, 650)
            enemy_y[i] = random.randint(30, 120)
        
        if collision2:
            laser2_y = 580
            laser2_state = "ready"
            score2_value += 500
            enemy_x[i] = random.randint(0, 650)
            enemy_y[i] = random.randint(30, 120)

        enemy(enemy_x[i], enemy_y[i], i)


    # Laser Move
    if laser_y <= 0:
        laser_y = 625
        laser_state = "ready"
    
    if laser2_y <= 0:
        laser2_y = 625
        laser2_state = "ready"

    if laser_state == "shoot":
        shoot_laser(laser_x, laser_y)
        laser_y -= laser_ychange

    if laser2_state == "shoot":
        shoot_laser2(laser2_x, laser2_y)
        laser2_y -= laser2_ychange

    # Afficher le sprite à sa new pos
    ship(ship_x, ship_y)
    ship2(ship2_x, ship2_y)
    show_score(Xsize, Ysize)
    show_score2((WIDTH - 225) , Ysize)
    pygame.display.flip()
  
    # py.display.update()
  
py.quit()