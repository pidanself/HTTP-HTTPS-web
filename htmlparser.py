import urllib .request  #导入用于打开URL的扩展库模块
import urllib .parse
import re    #导入正则表达式模块

#src='images/fengmian_2.jpg'
pp = r'src="|\'([^"]+\.jpg)"'


f=open('./web/index.html','rb')
html=str(f.read())

imglist2=re.findall(pp,html )

for each in imglist2:
    # 以/为分隔符，-1返回最后一个值
    filename = each.split("/")[-1]
    print(each)