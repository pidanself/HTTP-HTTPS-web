import requests
from bs4 import BeautifulSoup
import re

def parserhtml(htmldoc):
    # r=requests.get('https://www.temple.edu/')
    # r.status_code
    # r.encoding=r.apparent_encoding

    #取消注释
    re_comment = re.compile('<!--[^>]*-->')
    result = re_comment.sub('', htmldoc)

    soup=BeautifulSoup(result,'html.parser')#,from_encoding='utf-8'
    soup.prettify()
    # with open('test.html','w',encoding=r.encoding) as f:
    #     f.write(soup.prettify())
    # f.close()

    # for i in son:
    #     print(i.string)
    # print(soup.title.string)

    #打印头部
    headdoc=soup.title.string
    print(headdoc)

    #查找出所有的名字为a的标签
    # alist=soup.find_all('a')
    # print(len(sons))

    alist1=soup.body.descendants

    #遍历每一个名字为a的标签，查看它是否有超链接
    # for a in alist1:
    #     if 'herf'in a.attrs:
    #         print(a.herf)


    for a in alist1:
        try:
            if a.string != None and a.string!='\n':
                print(a.string)


            if 'href' in a.attrs:
                print(a.attrs['href'])
            #获取照片的源地址
            if a.img != None:
                print(a.img.attrs['src'])
        except:
            print('')
    #查找标签里面的所有文字资料
    # for string in soup.stripped_strings:
    #     print(repr(string))