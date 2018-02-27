# -*- coding: utf-8 -*-

import socket
import threading
import time

# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'welcome')

#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

#     sock.close()
#     print('Connection from %s:%s closed.' % addr)

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.bind(('127.0.0.1', 33803))
# s.listen(5)
# print('waiting for connection...')

# while True:
#     sock, addr = s.accept()
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 33803))

print('bind udp on 33803 success')

while True:
    data, addr = server.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    server.sendto(b'Hello, %s!' % data, addr)

