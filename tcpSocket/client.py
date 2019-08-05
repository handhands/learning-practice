#! /usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
from tcpSocket.conf import SERVER_ADDR, BUFSIZE

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(SERVER_ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break

    print data

tcpCliSock.close()


