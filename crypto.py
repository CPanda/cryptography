# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crypto.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tab.setObjectName("main_tab")
        self.encrypt_decrypt = QtWidgets.QWidget()
        self.encrypt_decrypt.setObjectName("encrypt_decrypt")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.encrypt_decrypt)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.encrypt_decrypt_tab = QtWidgets.QTabWidget(self.encrypt_decrypt)
        self.encrypt_decrypt_tab.setObjectName("encrypt_decrypt_tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.vg_key = QtWidgets.QTextEdit(self.tab)
        self.vg_key.setObjectName("vg_key")
        self.verticalLayout_4.addWidget(self.vg_key)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.vg_plaintextEdit = QtWidgets.QTextEdit(self.tab)
        self.vg_plaintextEdit.setObjectName("vg_plaintextEdit")
        self.verticalLayout_4.addWidget(self.vg_plaintextEdit)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.vg_encrypted_text = QtWidgets.QTextEdit(self.tab)
        self.vg_encrypted_text.setObjectName("vg_encrypted_text")
        self.verticalLayout_4.addWidget(self.vg_encrypted_text)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vg_encryptText = QtWidgets.QPushButton(self.tab)
        self.vg_encryptText.setObjectName("vg_encryptText")
        self.horizontalLayout.addWidget(self.vg_encryptText)
        self.vg_decryptText = QtWidgets.QPushButton(self.tab)
        self.vg_decryptText.setObjectName("vg_decryptText")
        self.horizontalLayout.addWidget(self.vg_decryptText)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.encrypt_decrypt_tab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_3.addWidget(self.textEdit_4)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_3.addWidget(self.textEdit_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.encrypt_decrypt_tab.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_7.setObjectName("textEdit_7")
        self.verticalLayout_8.addWidget(self.textEdit_7)
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.textEdit_8 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_8.setObjectName("textEdit_8")
        self.verticalLayout_8.addWidget(self.textEdit_8)
        self.atbash = QtWidgets.QPushButton(self.tab_5)
        self.atbash.setObjectName("atbash")
        self.verticalLayout_8.addWidget(self.atbash)
        self.encrypt_decrypt_tab.addTab(self.tab_5, "")
        self.horizontalLayout_4.addWidget(self.encrypt_decrypt_tab)
        self.main_tab.addTab(self.encrypt_decrypt, "")
        self.crypto_analysis = QtWidgets.QWidget()
        self.crypto_analysis.setObjectName("crypto_analysis")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.crypto_analysis)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.encrypt_decrypt_tab_2 = QtWidgets.QTabWidget(self.crypto_analysis)
        self.encrypt_decrypt_tab_2.setObjectName("encrypt_decrypt_tab_2")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_10.addWidget(self.textEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.tab_9)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_10.addWidget(self.pushButton)
        self.encrypt_decrypt_tab_2.addTab(self.tab_9, "")
        self.kasiski_2 = QtWidgets.QWidget()
        self.kasiski_2.setObjectName("kasiski_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.kasiski_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.kasiski_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.textEdit_6 = QtWidgets.QTextEdit(self.kasiski_2)
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_7.addWidget(self.textEdit_6)
        self.label_9 = QtWidgets.QLabel(self.kasiski_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.textEdit_9 = QtWidgets.QTextEdit(self.kasiski_2)
        self.textEdit_9.setObjectName("textEdit_9")
        self.verticalLayout_7.addWidget(self.textEdit_9)
        self.analyze_kasisiki = QtWidgets.QPushButton(self.kasiski_2)
        self.analyze_kasisiki.setObjectName("analyze_kasisiki")
        self.verticalLayout_7.addWidget(self.analyze_kasisiki)
        self.encrypt_decrypt_tab_2.addTab(self.kasiski_2, "")
        self.friedman_test_2 = QtWidgets.QWidget()
        self.friedman_test_2.setObjectName("friedman_test_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.friedman_test_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.friedman_test_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.friedman_text = QtWidgets.QTextEdit(self.friedman_test_2)
        self.friedman_text.setObjectName("friedman_text")
        self.verticalLayout_6.addWidget(self.friedman_text)
        self.label_12 = QtWidgets.QLabel(self.friedman_test_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.friedman_results = QtWidgets.QLineEdit(self.friedman_test_2)
        self.friedman_results.setObjectName("friedman_results")
        self.verticalLayout_6.addWidget(self.friedman_results)
        self.analyze_friedman = QtWidgets.QPushButton(self.friedman_test_2)
        self.analyze_friedman.setObjectName("analyze_friedman")
        self.verticalLayout_6.addWidget(self.analyze_friedman)
        self.encrypt_decrypt_tab_2.addTab(self.friedman_test_2, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.tab_8)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.freq_encrypt_text = QtWidgets.QTextEdit(self.tab_8)
        self.freq_encrypt_text.setObjectName("freq_encrypt_text")
        self.verticalLayout_5.addWidget(self.freq_encrypt_text)
        self.analyze_freq = QtWidgets.QPushButton(self.tab_8)
        self.analyze_freq.setObjectName("analyze_freq")
        self.verticalLayout_5.addWidget(self.analyze_freq)
        self.freq_graph = MatplotlibWidget(self.tab_8)
        self.freq_graph.setObjectName("freq_graph")
        self.verticalLayout_5.addWidget(self.freq_graph)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_15 = QtWidgets.QLabel(self.tab_8)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.save_text = QtWidgets.QLineEdit(self.tab_8)
        self.save_text.setObjectName("save_text")
        self.horizontalLayout_6.addWidget(self.save_text)
        self.save_image = QtWidgets.QPushButton(self.tab_8)
        self.save_image.setObjectName("save_image")
        self.horizontalLayout_6.addWidget(self.save_image)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.tab_8)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.key_len = QtWidgets.QLineEdit(self.tab_8)
        self.key_len.setObjectName("key_len")
        self.horizontalLayout_5.addWidget(self.key_len)
        self.split_text = QtWidgets.QPushButton(self.tab_8)
        self.split_text.setObjectName("split_text")
        self.horizontalLayout_5.addWidget(self.split_text)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.eng_freq_button = QtWidgets.QPushButton(self.tab_8)
        self.eng_freq_button.setObjectName("eng_freq_button")
        self.verticalLayout_5.addWidget(self.eng_freq_button)
        self.encrypt_decrypt_tab_2.addTab(self.tab_8, "")
        self.horizontalLayout_3.addWidget(self.encrypt_decrypt_tab_2)
        self.main_tab.addTab(self.crypto_analysis, "")
        self.verticalLayout.addWidget(self.main_tab)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionKasiski_Test = QtWidgets.QAction(MainWindow)
        self.actionKasiski_Test.setObjectName("actionKasiski_Test")
        self.actionFriedman_Test = QtWidgets.QAction(MainWindow)
        self.actionFriedman_Test.setObjectName("actionFriedman_Test")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.main_tab.setCurrentIndex(1)
        self.encrypt_decrypt_tab.setCurrentIndex(2)
        self.encrypt_decrypt_tab_2.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cryptography Tool"))
        self.label.setText(_translate("MainWindow", "Key"))
        self.label_2.setText(_translate("MainWindow", "Plain Text"))
        self.label_3.setText(_translate("MainWindow", "Encrypted"))
        self.vg_encryptText.setText(_translate("MainWindow", "Encrypt"))
        self.vg_decryptText.setText(_translate("MainWindow", "Decrypt"))
        self.encrypt_decrypt_tab.setTabText(self.encrypt_decrypt_tab.indexOf(self.tab), _translate("MainWindow", "Vigenere"))
        self.label_4.setText(_translate("MainWindow", "Key"))
        self.label_5.setText(_translate("MainWindow", "Plain Text"))
        self.label_6.setText(_translate("MainWindow", "Encrypted"))
        self.pushButton_3.setText(_translate("MainWindow", "Encrypt"))
        self.pushButton_4.setText(_translate("MainWindow", "Decrypt"))
        self.encrypt_decrypt_tab.setTabText(self.encrypt_decrypt_tab.indexOf(self.tab_2), _translate("MainWindow", "Playfair"))
        self.label_7.setText(_translate("MainWindow", "Plain Text"))
        self.label_8.setText(_translate("MainWindow", "Encrypted"))
        self.atbash.setText(_translate("MainWindow", "Encrypt/Decrypt"))
        self.encrypt_decrypt_tab.setTabText(self.encrypt_decrypt_tab.indexOf(self.tab_5), _translate("MainWindow", "Atbash"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.encrypt_decrypt), _translate("MainWindow", "Encrypt and Decrypt"))
        self.pushButton.setText(_translate("MainWindow", "Set CipherText For All Analysis Options"))
        self.encrypt_decrypt_tab_2.setTabText(self.encrypt_decrypt_tab_2.indexOf(self.tab_9), _translate("MainWindow", "Default CipherText"))
        self.label_10.setText(_translate("MainWindow", "Encrypted Text"))
        self.label_9.setText(_translate("MainWindow", "Results"))
        self.analyze_kasisiki.setText(_translate("MainWindow", "Analyze"))
        self.encrypt_decrypt_tab_2.setTabText(self.encrypt_decrypt_tab_2.indexOf(self.kasiski_2), _translate("MainWindow", "&Kasiski Test"))
        self.label_11.setText(_translate("MainWindow", "Encrypted Text"))
        self.label_12.setText(_translate("MainWindow", "Results"))
        self.analyze_friedman.setText(_translate("MainWindow", "Analyze"))
        self.encrypt_decrypt_tab_2.setTabText(self.encrypt_decrypt_tab_2.indexOf(self.friedman_test_2), _translate("MainWindow", "Friedman Test"))
        self.label_13.setText(_translate("MainWindow", "Encrypted Text"))
        self.analyze_freq.setText(_translate("MainWindow", "Plot Frequency"))
        self.label_15.setText(_translate("MainWindow", "File Name:  "))
        self.save_image.setText(_translate("MainWindow", "Save Image"))
        self.label_14.setText(_translate("MainWindow", "Key Length:"))
        self.split_text.setText(_translate("MainWindow", "Split Text"))
        self.eng_freq_button.setText(_translate("MainWindow", "English Freqency Graph"))
        self.encrypt_decrypt_tab_2.setTabText(self.encrypt_decrypt_tab_2.indexOf(self.tab_8), _translate("MainWindow", "Frequency Analysis"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.crypto_analysis), _translate("MainWindow", "Analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionKasiski_Test.setText(_translate("MainWindow", "Kasiski Test"))
        self.actionFriedman_Test.setText(_translate("MainWindow", "Friedman Test"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))

from matplotlibwidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

