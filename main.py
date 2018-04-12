"""
This is the main python file that will use functions from playfair, vigenere, etc.

Simple QT5 Gui 

"""

import sys
import vigenere as vg
import playfair as pf
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from crypto import Ui_MainWindow

class MainW (QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionQuit.triggered.connect(QApplication.quit)
        self.vg_encryptText.clicked.connect(self.vg_encrypt)
    def vg_encrypt(self):
        text = self.vg_plaintextEdit.toPlainText()
        key = self.vg_key.toPlainText()
        #print(vg.encrypt(text, key))
        self.vg_encrypted_text.setText(vg.encrypt(text,key))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    myapp = MainW()
    myapp.show()
    sys.exit(app.exec_())




