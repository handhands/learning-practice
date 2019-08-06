#! /usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
from time import ctime

from conf import ADDR, BUFSIZE

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from :', addr

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send('[%s]  %s' % (ctime(), data))

        #tcpCliSock.close()

tcpSerSock.close()

