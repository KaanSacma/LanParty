#!/usr/bin/python3

import pygame
from pygame.locals import *
from socket import socket
import os

is_closed = False

server = socket()

server.connect(("127.0.0.1", 5000))

print("You are connected")
pygame.init()
window = pygame.display.set_mode((640, 480), RESIZABLE)

bg = pygame.image.load("background.jpg").convert()
window.blit(bg, (0,0))

pygame.display.flip()

game = 1

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0
