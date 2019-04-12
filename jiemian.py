
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI.Index import *

class MainWindow( QMainWindow ,Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
