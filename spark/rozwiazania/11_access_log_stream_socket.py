#!/usr/bin/env python
import socket
import time
import random
import os
import random
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 8899
sock.bind((host, port))

base_path = os.path.dirname(__file__)

with open(os.path.join(base_path, 'data/access_log')) as f:
    log = f.readlines()

log_len = len(log)

def get_log_line():
    i = random.randint(0, log_len)
    return log[i]

class client(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.sock = socket
        self.start()

    def run(self):
        print('{}: starting client connection'.format(self.name))
        i = 0
        isOn = True
        while isOn:
            try:
                self.sock.send(get_log_line().encode())
                i += 1
                time.sleep(1)
            except Exception as e:
                isOn = False
                print('{}: closing client connection'.format(self.name))

sock.listen(5)
print ('Server started and listening on host: {} and port: {}'.format(host, port))
while True:
    clientsock = None # <---
    try:
        clientsock, address = sock.accept()
        client(clientsock)
    except KeyboardInterrupt:
        if clientsock:
            clientsock.close()
        break
