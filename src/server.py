#!/usr/bin/python3

import pygame
from pygame.locals import *
from socket import socket

def send_msg_and_receiv(to_, from_):

    while (1):
        notif = from_.recv(1024).decode() #nb de char lu par def
        if (len(notif) > 0):
            to_.send(notif.encode())

try:
    server = socket()

    server.bind(("127.0.0.1", 5000)) #tuple = une liste constante

    server.listen(2)

    client, adr = server.accept()
    client2, adr2 = server.accept()

except KeyboardInterrupt:
    print("The server is closed")
