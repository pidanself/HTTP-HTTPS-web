import socket
import sys
from tkinter import *

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='cn.bing.com'
s.connect((host,80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: '+host.encode(encoding="utf-8")+b'\r\nConnection: close\r\n\r\n')

#接收数据
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data=b''.join(buffer)
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('233.html', 'wb') as f:
    f.write(html)