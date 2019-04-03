import socket
import sys
from tkinter import *

root=Tk()
aLable=Label(root,text="请输入URL")
aLable.pack()
#输入框
v=StringVar()
e=Entry(root,textvariable=v)
e.pack()

#按钮
quitButton = Button(root,text="提交",command=root.quit)
quitButton.pack()

root.mainloop()

#获得IP地址
host = v.get()

#创建一个socket，AF_INET指定使用IPv4协议，AF_INET6为IPV6协议
#SOCK_STREAM指定使用面向流的TCP协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(host)


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

with open('233.html', 'wb') as f:
    f.write(html)