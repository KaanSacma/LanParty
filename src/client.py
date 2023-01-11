#!/usr/bin/python3

from socket import socket
import os
from main import main

res = False
is_closed = False
mutex = Lock()

def send_msg(server):
    global is_closed, mutex
    msg = ""
    while (msg):
        msg = input("")
        if(len(msg) > 0):
            server.send(msg.encode())
    mutex.acquire()
    is_closed = True
    mutex.release()    

def receiv_msg(server):
    global is_closed, mutex
    msg = ""
    while (msg):
        msg = server.recv(1024).decode()
        if (len(msg) > 0):
            print('\n' + msg)
    mutex.acquire()
    is_closed = True
    mutex.release()

server = socket()

server.connect(("127.0.0.1", 5505))

print("You are connected")

main()

res = False
while(True):
    mutex.acquire()
    res = is_closed
    mutex.release()
    if (res == True):
        server.close()
        os._exit(0)

thread_one = Thread(target=send_msg, args=(server,))
thread_two = Thread(target=receiv_msg, args=(server,))

thread_one.start()
thread_two.start()
