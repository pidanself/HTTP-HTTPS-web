import socket
import ssl
from tkinter import *

#调用图形界面
def graph():
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
    #返回IP地址
    return v.get()

#针对HTTP网站的申请
def HTTP(host):
    # 创建一个socket，AF_INET指定使用IPv4协议，AF_INET6为IPV6协议
    # SOCK_STREAM指定使用面向流的TCP协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, 80))

    # 发送数据:
    s.send(b'GET / HTTP/1.1\r\nHost: ' + host.encode(encoding="utf-8") + b'\r\nConnection: close\r\n\r\n')

    # 接收数据
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('web/index.html', 'wb') as f:
        f.write(html)

#针对HTTPS网站的申请
def HTTPS(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 443))
    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                        ssl_version=ssl.PROTOCOL_SSLv23)

    s.sendall(b"GET / HTTP/1.1\r\nHost: "+host.encode(encoding="utf-8")+b"\r\nConnection: close\r\n\r\n")

    # 接收数据
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break

    data = b''.join(buffer)
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('web/index.html', 'wb') as f:
        f.write(html)

def display():
    # 调用库显示html
    import eel
    eel.init('web')
    web_app_options = {
        'mode': "chrome-app",  # or "chrome"
        'port': 8082,
        'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
    }
    eel.start('index.html', options=web_app_options)

def iss(host):
    if(host[0:5]=='https'):
        return True
    else:
        return False

#主函数
def main():
    # 调用图形界面获得IP地址
    host = graph()
    if(iss(host)):
        HTTPS(host)
    else:
        HTTP(host)
    display()

if __name__ == '__main__':
    main()