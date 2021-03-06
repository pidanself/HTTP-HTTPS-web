import socket
import ssl
from tkinter import *
from urllib import request
import urllib

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
#网站都不用输入www
#很好的处理异常的机制
# while (1):
#     try:
#         HTTP(host)
#     except:
#         print(u'[%s] HTTP请求失败！！！正在准备重发。。。')


#针对HTTPS网站的申请
def HTTPS(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 443))

    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                        ssl_version=ssl.PROTOCOL_SSLv23)

    s.sendall(b"GET /showPublic HTTP/1.1\r\nHost: "+host.encode(encoding="utf-8")+b"\r\nConnection: close\r\n\r\n")

    # 接收数据
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
#https://www.github.com
    data = b''.join(buffer)
    header, html = data.split(b'\r\n\r\n', 1)
    test,wu=data.split(b'\r\n', 1)
    test=test.decode('utf-8')
    san='301'
    if(san in test):
        print('重定向')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'www.' + host
        s.connect((host, 443))

        s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                            ssl_version=ssl.PROTOCOL_SSLv23)

        s.sendall(b"GET / HTTP/1.1\r\nHost: " + host.encode(encoding="utf-8") + b"\r\nConnection: close\r\n\r\n")

        # 接收数据
        buffer = []
        while True:
            d = s.recv(1024)
            if d:
                buffer.append(d)
            else:
                break
                # https://www.github.com
        data = b''.join(buffer)
        header, html = data.split(b'\r\n\r\n', 1)

    print(header.decode('utf-8'))
    with open('web/index.html', 'wb') as f:
        f.write(html)

# #只能处理把www去掉的
# #新浪的扒取要输入www
# host='news.baidu.com'
# HTTPS(host)
"""
使用GET在百度搜索引擎上查询
此例演示如何生成GET串,并进行请求.
"""
def BDAPI(host):
    url = "http://www.baidu.com/s"
    search = [('w',host)]
    getString = url + "?" + urllib.parse.urlencode(search)

    req = urllib.request.Request(getString)
    fd = urllib.request.urlopen(req)
    baiduResponse=""
    buffer=[]
    while 1:
        data= fd.read(1024)
        if not len(data):
            break
        buffer.append(data)
    data = b''.join(buffer)
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('web/index.html', 'wb') as f:
        f.write(html)



def iss(host):
    if(host[0:5]=='https'):
        return True
    else:
        return False

def ish(host):
    if(host[0:4]=='http'):
        return True
    else:
        return False

#输入host 扒取相应网页
def gethtml(host):
    if (iss(host)):
        if (host[8:3] == 'www'):
            host = host[12::]
        else:
            host = host[8::]
        HTTPS(host)
    elif (ish(host)):
        if (host[7:3] == 'www'):
            host = host[11::]
        else:
            host = host[7::]
        HTTP(host)
    else:
        BDAPI(host)


# host='www.hao123.com'
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((host, 80))
#
# # 发送数据:
# s.send(b'GET /mail HTTP/1.1\r\nHost: ' + host.encode(encoding="utf-8") + b'\r\nConnection: close\r\n\r\n')
# # 接收数据
# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# with open('web/index.html', 'wb') as f:
#     f.write(html)


#主函数
# def main():
#     # 调用图形界面获得IP地址
#     #IP的输入格式有两种，
#     #http的为：http://poj.org
#         # http://bailian.openjudge.cn
#         #http://www.runoob.com
#         # http://www.uml.org.cn
#         #http://www.ustb.edu.cn
#         #http://teach.ustb.edu.cn 可以扒下来 但会乱码 需要显示的时候调整
#         #http://www.cnki.net
#
#     #https的为：https://www.bj.lianjia.com
#         # https://www.baidu.com
#         # https://www.cnblogs.com
#          # https://github.com
#         #https://blog.csdn.net
#         # https://wmathor.com
#         #https://www.sina.com.cn
#         #https://www.weibo.com 失败 应该有反扒机制，只获取了0
#         # https://pay.ustb.edu.cn 修改相应代码可以查看，因为Cache-Control: private
#         #https://www.liaoxuefeng.com 扒不到    302 Found 并且Location: /404
#
#
#     host = graph()
#
#     if(iss(host)):
#         if(host[8:3] == 'www'):
#             host = host[12::]
#         else:
#             host = host[8::]
#         HTTPS(host)
#     elif(ish(host)):
#         if (host[7:3] == 'www'):
#             host = host[11::]
#         else:
#             host = host[7::]
#         HTTP(host)
#     else:
#         BDAPI(host)
#     display()
#https://www.weibo.com
# if __name__ == '__main__':
#     main()
