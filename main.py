import htmlparser
import get




def main():
    host="http://www.ustb.edu.cn"
    get.gethtml(host)
    with open('./web/index.html','r',encoding='utf-8') as f:
        str=f.read()
        htmlparser.parserhtml(str)
    f.close()

if __name__ == '__main__':
    main()