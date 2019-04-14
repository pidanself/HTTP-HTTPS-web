import get
import getpic



def main():
    host="http://poj.org"
    get.gethtml(host)
    getpic.getpic(host)

if __name__ == '__main__':
    main()