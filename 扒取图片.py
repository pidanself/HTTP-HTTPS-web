import urllib .request  #导入用于打开URL的扩展库模块
import urllib .parse
import re    #导入正则表达式模块
import socket
import ssl

# def open_url(url):
#   req=urllib .request .Request (url)   #将Request类实例化并传入url为初始值，然后赋值给req
#   #添加header，伪装成浏览器
#   req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
#   #访问url，并将页面的二进制数据赋值给page
#   page=urllib .request .urlopen(req)
#   #将page中的内容转换为utf-8编码
#   html=page .read().decode('utf-8')
#
#   return html

def get_img(html):
  # [^"]+\.jpg 匹配除"以外的所有字符多次,后面跟上转义的.和png
  p=r'src="([^"]+\.png)"'
  pp=r'src="([^"]+\.jpg)"'
  #返回正则表达式在字符串中所有匹配结果的列表
  imglist=re.findall(p,html )
  imglist2=re.findall(pp,html )
  #循环遍历列表的每一个值
  for each in imglist :
    #以/为分隔符，-1返回最后一个值
    filename=each.split("/")[-1]
    #访问each，并将页面的二进制数据赋值给photo
    photo=urllib .request .urlopen(each )
    w=photo .read()
    #打开指定文件，并允许写入二进制数据
    f=open('C:\\Users\\Administrator\\Desktop\\计网实验\\实验二\\HTTP-HTTPS-web\\picture\\'+filename,'wb')
    #写入获取的数据
    f.write(w)
    #关闭文件
    f.close()
  for each in imglist2 :
    #以/为分隔符，-1返回最后一个值
    filename=each.split("/")[-1]
    #访问each，并将页面的二进制数据赋值给photo
    photo=urllib .request .urlopen(each )
    w=photo .read()
    #打开指定文件，并允许写入二进制数据
    f=open('C:\\Users\\Administrator\\Desktop\\计网实验\\实验二\\HTTP-HTTPS-web\\picture\\'+filename,'wb')
    #写入获取的数据
    f.write(w)
    #关闭文件
    f.close()

#该模块既可以导入到别的模块中使用，另外该模块也可自我执行
if __name__=='__main__':
  #通过链接获取html
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('bj.lianjia.com', 443))
  s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                      ssl_version=ssl.PROTOCOL_SSLv23)

  s.sendall(b"GET / HTTP/1.1\r\nHost: bj.lianjia.com\r\nConnection: close\r\n\r\n")

  # 接收数据
  buffer = []
  while True:
    d = s.recv(1024)
    if d:
      buffer.append(d)
    else:
      break
  html=str(buffer)
  #将url作为open_url()的参数，然后将open_url()的返回值作为参数赋给get_img()
  get_img(html)