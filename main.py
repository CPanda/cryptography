"""
This is the main python file that will use functions from playfair, vigenere, etc.

Simple QT5 Gui

"""

import sys
import vigenere as vg
import plots as pt
import playfair as pf
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from crypto import Ui_MainWindow
from about import Ui_about
from collections import Counter
import numpy as np

class MainW (QMainWindow, Ui_MainWindow):
    """
    Defines actions and functions for the buttons on the screen.
    """
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionQuit.triggered.connect(QApplication.quit)
        self.vg_encryptText.clicked.connect(self.vg_encrypt)
        self.vg_decryptText.clicked.connect(self.vg_decrypt)
        self.actionAbout.triggered.connect(self.showDial)
        self.analyze_friedman.clicked.connect(self.friedman)
        self.analyze_freq.clicked.connect(self.freq_analyze)
    def freq_analyze(self):
        self.freq_graph.axes.clear()
        text = self.freq_encrypt_text.toPlainText()
        text = vg.processtext(text)
        figure = pt.freq_analysis(text)
        letter_count = Counter(text)
        letter_count = sorted(letter_count.items())
        labels, values = zip(*letter_count)
        indexes = np.arange(len(labels))
        width = 0.8
        self.freq_graph.axes.bar(indexes, values, width, align='center')
        self.freq_graph.axes.set_xticks(indexes )
        self.freq_graph.axes.set_xticklabels(labels)
        self.freq_graph.draw()

    def friedman(self):
        text = self.friedman_text.toPlainText()
        self.friedman_results.setText(str(vg.friedmantest(text)))
    def vg_decrypt(self):
        text = self.vg_encrypted_text.toPlainText()
        key = self.vg_key.toPlainText()
        self.vg_plaintextEdit.setText(vg.decrypt(text,key))
    def vg_encrypt(self):
        text = self.vg_plaintextEdit.toPlainText()
        key = self.vg_key.toPlainText()
        #print(vg.encrypt(text, key))
        self.vg_encrypted_text.setText(vg.encrypt(text,key))

    def showDial(self):
        dialog = QDialog()
        dialog.ui = Ui_about()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    myapp = MainW()
    myapp.show()
    sys.exit(app.exec_())




