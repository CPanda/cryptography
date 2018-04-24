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
from save_graph import Ui_save_graph
from english_frequency import Ui_english_freq_dialog
from textsplit import Ui_split_Dialog
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
        self.eng_freq_button.clicked.connect(self.showenglish_freq_dialog)
        self.save_image.clicked.connect(self.saveimage)
    def freq_analyze(self):
        self.freq_graph.axes.clear()
        text = self.freq_encrypt_text.toPlainText()
        text = vg.processtext(text)
        #figure = pt.freq_analysis(text)
        letter_count = Counter(text)
        letter_count = sorted(letter_count.items())
        labels, values = zip(*letter_count)
        indexes = np.arange(len(labels))
        width = 0.8
        self.freq_graph.axes.bar(indexes, values, width, align='center')
        self.freq_graph.axes.set_xticks(indexes )
        self.freq_graph.axes.set_xticklabels(labels)
        self.freq_graph.draw()
        #self.freq_graph.figure.savefig('fig.png')
    def saveimage(self):
        dialog = QDialog()
        dialog.ui = Ui_save_graph()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.ui.save_image.clicked.connect(self.freq_graph.figure.savefig(dialog.ui.lineEdit.text()))

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
    def showenglish_freq_dialog(self):
        dialog = QDialog()
        dialog.ui = Ui_english_freq_dialog()
        #dialog.ui.english_freq.axes.bar(5,3,0.8,align='center')
        values = [8.167,1.492,2.782,4.253,12.702,
                       2.228,2.015,6.094,6.966,0.153,0.772,4.025,
                       2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,
                       2.758,0.978,2.360,0.150,1.974,0.074]
        labels=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u','v','w','x','y','z']
        indexes = np.arange(len(labels))
        width = 0.8
        dialog.ui.setupUi(dialog)
        dialog.ui.english_freq.axes.bar(indexes,values,width,align='center')
        dialog.ui.english_freq.axes.set_xticks(indexes)
        dialog.ui.english_freq.axes.set_xticklabels(labels)
        dialog.ui.english_freq.draw()
        dialog.exec_()
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




