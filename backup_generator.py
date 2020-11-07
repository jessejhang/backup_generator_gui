import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

import shutil, os, errno
import datetime

def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Folder Coverter'
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.getInteger()
        self.getText()
        # self.getDouble()
        # self.getChoice()

        # self.show()

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Folder Copy", "Directory:", QLineEdit.Normal, 'D://NIP_DB_PLUS')
        if okPressed and text != '':
            src = text
            dest = src + '_' + datetime.datetime.today().strftime('%Y%m%d')
            copy(src, dest)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())