#!/usr/bin/python3

# import pygame
# from pygame.locals import *
from socket import socket
import os
from main import main

is_closed = False

server = socket()

server.connect(("127.0.0.1", 5505))

print("You are connected")

main()
