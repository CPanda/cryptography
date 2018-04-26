"""
This is the main python file that will use functions from playfair, vigenere, etc.

Simple QT5 Gui

Dylan Hoban

"""

import sys
import crypto_algs.vigenere as vg
#import playfair as pf
#from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *
from gui.crypto import Ui_MainWindow
from gui.about import Ui_about
from gui.english_frequency import Ui_english_freq_dialog
from gui.textsplit import Ui_split_Dialog
from collections import Counter
import crypto_algs.kasiski as ks
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
        self.save_text.setText("plot.png")
        self.split_text.clicked.connect(self.split)
        self.default_cipher.clicked.connect(self.defaultciphertext)
        self.analyze_kasisiki.clicked.connect(self.kasiski)
    def kasiski(self):
        text = self.kasiski_test.toPlainText()
        if text:
            result = ks.kasiskitest(text)
            #stringresult = str(result)
            self.kasiski_results.setText("possibile key lengths: :"+str(result))

    #sets the default ciphertext for options in the analyze tabs
    def defaultciphertext(self):
        text = self.default_cipher_textbox.toPlainText()
        if text:
            self.kasiski_test.setText(text)
            self.friedman_text.setText(text)
            self.freq_encrypt_text.setText(text)

    #splits the text based on keylength found from kasiski test.
    def split(self):
        text = self.freq_encrypt_text.toPlainText()
        if text:
            loopno = int(self.key_len.text())
            arry = []
            for i in range(1,loopno+1):
                arry.append(self.getNthLetters(i, loopno, text))
            dialog = QDialog(self)
            dialog.ui = Ui_split_Dialog()
            dialog.ui.setupUi(dialog)
            for i in range(len(arry)):
                dialog.ui.split_result.append(arry[i]+'\n')
            dialog.setModal(False)
            dialog.show()

    #gets the Nth letter from a string so that it can be displayed in the "split" dialog.
    def getNthLetters(self, n, keylen, msg):
        i = n - 1
        letters = []
        while i < len(msg):
            letters.append(msg[i])
            i += keylen
        return ''.join(letters)


    #analyzes and sets the figure for the frequency count of the letters.
    def freq_analyze(self):
        self.freq_graph.axes.clear()
        text = self.freq_encrypt_text.toPlainText()
        text = vg.processtext(text)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        if text and alphabet:
            text+=alphabet
            #figure = pt.freq_analysis(text)
            letter_count = Counter(text)
            letter_count = sorted(letter_count.items())
            labels, values = zip(*letter_count)
            values = list(values)
            indexes = np.arange(len(labels))
            width = 0.8
            for i in range(len(values)):
                values[i]-=1 #take away the added values from alphabet.
            self.freq_graph.axes.bar(indexes, values, width, align='center')
            self.freq_graph.axes.set_xticks(indexes )
            self.freq_graph.axes.set_xticklabels(labels)
            self.freq_graph.draw()

    #saves an iamge to the current working directory.
    def saveimage(self):
        text = self.save_text.text()
        if text:
            self.freq_graph.figure.savefig(text)

    #performs the friedman test on the text from the friedman test text box.
    def friedman(self):
        text = self.friedman_text.toPlainText()
        if text:
            self.friedman_results.setText(str(vg.friedmantest(text)))
    #performs vigenere decryption on the ciphertext in the vg tab.
    def vg_decrypt(self):
        text = self.vg_encrypted_text.toPlainText()
        key = self.vg_key.toPlainText()
        if text:
            self.vg_plaintextEdit.setText(vg.decrypt(text,key))
    #encrypts text in the vinenere tab.
    def vg_encrypt(self):
        text = self.vg_plaintextEdit.toPlainText()
        key = self.vg_key.toPlainText()
        #print(vg.encrypt(text, key))
        if text and key:
            self.vg_encrypted_text.setText(vg.encrypt(text,key))

    #shows a dynamic dialog that contains the english frequencies for the alphabet.
    def showenglish_freq_dialog(self):
        dialog = QDialog(self)
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
        dialog.show()
    #shows the about dialog.
    def showDial(self):
        dialog = QDialog(self)
        dialog.ui = Ui_about()
        dialog.ui.setupUi(dialog)
        dialog.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    myapp = MainW()
    myapp.show()
    sys.exit(app.exec_())




