#!/usr/bin/python3

import pygame
from pygame.locals import *
from socket import socket

try:
    server = socket()

    server.bind(("127.0.0.1", 5000)) #tuple = une liste constante

    server.listen(2)

    client, adr = server.accept()
    client2, adr2 = server.accept()

except KeyboardInterrupt:
    print("The server is closed")
