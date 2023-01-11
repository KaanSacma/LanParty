import math
import pygame as py
import pygame
import sys
import os
from pygame.locals import *

py.init() 

clock = py.time.Clock()

# Sprites
spaceship = pygame.image.load("spaceship.png")
new_spaceship = pygame.transform.scale(spaceship, (80, 90))

laser = pygame.image.load("newlaser.jpg")
new_laser = pygame.transform.scale(laser, (120, 45))

x_ss, y_ss = 30, 30
speed_ss = 5

x_l, y_l = 30, 30 
speed_l = 10

Height = 600
Width = 1200

# Fenêtre
py.display.set_caption("Space Invader!")
screen = py.display.set_mode((Width, Height))
  
# Image
background = py.image.load("background.jpg").convert()
  
# main variables pour le scrolling
scroll = 0
max = math.ceil(Width / background.get_width()) + 1

# Main loop
while 1:

    # Vitesse de scroll
    clock.tick(33)

    # Closinf scrolling
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x_ss -= speed_ss
    if keys[pygame.K_RIGHT]:
        x_ss += speed_ss
    if keys[pygame.K_UP]:
        y_ss -= speed_ss
    if keys[pygame.K_DOWN]:
        y_ss += speed_ss
   # if keys[pygame.K_SPACE]:
   #    x_l += speed_l

    # Effacer l'écran
    screen.fill((0, 0, 0))

    # Screen scroll
    i = 0
    while(i < max):
        screen.blit(background, (background.get_width()*i + scroll, 0))
        i += 1

    # Frame pour scroll
    scroll -= 6
  
    # Reset le scrolling
    if abs(scroll) > background.get_width():
        scroll = 0

    # Afficher le sprite à sa new pos
    screen.blit(new_spaceship, (x_ss, y_ss))
    screen.blit(new_laser, (x_l, y_l))
    pygame.display.flip()
  
    # py.display.update()
  
py.quit()