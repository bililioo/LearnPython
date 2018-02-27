# -*- coding: utf-8 -*-

import socket


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))

# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break

# data = b''.join(buffer)
# s.close()

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))

# with open('sina.html', 'wb') as f:
#     f.write(html)

####################################################

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('127.0.0.1', 33803))

# print(sock.recv(1024).decode('utf-8'))

# sock.send(b'ben')
# print(sock.recv(1024).decode())

# sock.send(b'22')
# print(sock.recv(1024).decode())

# sock.send(b'exit')
# sock.close()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b'ben', ('127.0.0.1', 33803))
print(client.recv(1024).decode())

client.sendto(b'ben', ('127.0.0.1', 33803))
print(client.recv(1024).decode())

