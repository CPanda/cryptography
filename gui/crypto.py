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
        MainWindow.resize(649, 843)
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
        self.rsa = QtWidgets.QWidget()
        self.rsa.setToolTip("")
        self.rsa.setToolTipDuration(5)
        self.rsa.setObjectName("rsa")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.rsa)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_19 = QtWidgets.QLabel(self.rsa)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_9.addWidget(self.label_19)
        self.rsa_encdec_n = QtWidgets.QLineEdit(self.rsa)
        self.rsa_encdec_n.setObjectName("rsa_encdec_n")
        self.horizontalLayout_9.addWidget(self.rsa_encdec_n)
        self.label_20 = QtWidgets.QLabel(self.rsa)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        self.rsa_encdec_e = QtWidgets.QLineEdit(self.rsa)
        self.rsa_encdec_e.setObjectName("rsa_encdec_e")
        self.horizontalLayout_9.addWidget(self.rsa_encdec_e)
        self.label_21 = QtWidgets.QLabel(self.rsa)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_9.addWidget(self.label_21)
        self.rsa_encdec_d = QtWidgets.QLineEdit(self.rsa)
        self.rsa_encdec_d.setObjectName("rsa_encdec_d")
        self.horizontalLayout_9.addWidget(self.rsa_encdec_d)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.label_22 = QtWidgets.QLabel(self.rsa)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_9.addWidget(self.label_22)
        self.csv_rsa_plain = QtWidgets.QTextEdit(self.rsa)
        self.csv_rsa_plain.setObjectName("csv_rsa_plain")
        self.verticalLayout_9.addWidget(self.csv_rsa_plain)
        self.label_16 = QtWidgets.QLabel(self.rsa)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_9.addWidget(self.label_16)
        self.csv_rsa_encrypt = QtWidgets.QTextEdit(self.rsa)
        self.csv_rsa_encrypt.setObjectName("csv_rsa_encrypt")
        self.verticalLayout_9.addWidget(self.csv_rsa_encrypt)
        self.rsa_encrypt_decrypt = QtWidgets.QPushButton(self.rsa)
        self.rsa_encrypt_decrypt.setObjectName("rsa_encrypt_decrypt")
        self.verticalLayout_9.addWidget(self.rsa_encrypt_decrypt)
        self.encrypt_decrypt_tab.addTab(self.rsa, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.knap_m = QtWidgets.QLineEdit(self.tab_4)
        self.knap_m.setObjectName("knap_m")
        self.horizontalLayout_7.addWidget(self.knap_m)
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.knap_w = QtWidgets.QLineEdit(self.tab_4)
        self.knap_w.setObjectName("knap_w")
        self.horizontalLayout_7.addWidget(self.knap_w)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_30 = QtWidgets.QLabel(self.tab_4)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_11.addWidget(self.label_30)
        self.knap_invw = QtWidgets.QLineEdit(self.tab_4)
        self.knap_invw.setObjectName("knap_invw")
        self.horizontalLayout_11.addWidget(self.knap_invw)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_31 = QtWidgets.QLabel(self.tab_4)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_12.addWidget(self.label_31)
        self.knap_ez = QtWidgets.QLineEdit(self.tab_4)
        self.knap_ez.setObjectName("knap_ez")
        self.horizontalLayout_12.addWidget(self.knap_ez)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.label_32 = QtWidgets.QLabel(self.tab_4)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_12.addWidget(self.label_32)
        self.knap_bin = QtWidgets.QTextEdit(self.tab_4)
        self.knap_bin.setObjectName("knap_bin")
        self.verticalLayout_12.addWidget(self.knap_bin)
        self.label_33 = QtWidgets.QLabel(self.tab_4)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_12.addWidget(self.label_33)
        self.knap_encrypted_text = QtWidgets.QTextEdit(self.tab_4)
        self.knap_encrypted_text.setObjectName("knap_encrypted_text")
        self.verticalLayout_12.addWidget(self.knap_encrypted_text)
        self.knap_btn_encdec = QtWidgets.QPushButton(self.tab_4)
        self.knap_btn_encdec.setObjectName("knap_btn_encdec")
        self.verticalLayout_12.addWidget(self.knap_btn_encdec)
        self.encrypt_decrypt_tab.addTab(self.tab_4, "")
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
        self.default_cipher_textbox = QtWidgets.QTextEdit(self.tab_9)
        self.default_cipher_textbox.setObjectName("default_cipher_textbox")
        self.verticalLayout_10.addWidget(self.default_cipher_textbox)
        self.default_cipher = QtWidgets.QPushButton(self.tab_9)
        self.default_cipher.setObjectName("default_cipher")
        self.verticalLayout_10.addWidget(self.default_cipher)
        self.encrypt_decrypt_tab_2.addTab(self.tab_9, "")
        self.kasiski_2 = QtWidgets.QWidget()
        self.kasiski_2.setObjectName("kasiski_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.kasiski_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.kasiski_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.kasiski_test = QtWidgets.QTextEdit(self.kasiski_2)
        self.kasiski_test.setObjectName("kasiski_test")
        self.verticalLayout_7.addWidget(self.kasiski_test)
        self.label_9 = QtWidgets.QLabel(self.kasiski_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.kasiski_results = QtWidgets.QTextEdit(self.kasiski_2)
        self.kasiski_results.setObjectName("kasiski_results")
        self.verticalLayout_7.addWidget(self.kasiski_results)
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
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_11.addWidget(self.label_25)
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_11.addWidget(self.label_23)
        self.rsa_n = QtWidgets.QLineEdit(self.tab_3)
        self.rsa_n.setObjectName("rsa_n")
        self.verticalLayout_11.addWidget(self.rsa_n)
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_11.addWidget(self.label_24)
        self.pq_results = QtWidgets.QTextEdit(self.tab_3)
        self.pq_results.setObjectName("pq_results")
        self.verticalLayout_11.addWidget(self.pq_results)
        self.rsa_pq_button = QtWidgets.QPushButton(self.tab_3)
        self.rsa_pq_button.setObjectName("rsa_pq_button")
        self.verticalLayout_11.addWidget(self.rsa_pq_button)
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_11.addWidget(self.label_26)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_10.addWidget(self.label_27)
        self.rsa_p_find_d = QtWidgets.QLineEdit(self.tab_3)
        self.rsa_p_find_d.setObjectName("rsa_p_find_d")
        self.horizontalLayout_10.addWidget(self.rsa_p_find_d)
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_10.addWidget(self.label_28)
        self.rsa_q_find_d = QtWidgets.QLineEdit(self.tab_3)
        self.rsa_q_find_d.setObjectName("rsa_q_find_d")
        self.horizontalLayout_10.addWidget(self.rsa_q_find_d)
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_10.addWidget(self.label_29)
        self.rsa_e_find_d = QtWidgets.QLineEdit(self.tab_3)
        self.rsa_e_find_d.setObjectName("rsa_e_find_d")
        self.horizontalLayout_10.addWidget(self.rsa_e_find_d)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.rsa_box_find_d = QtWidgets.QTextEdit(self.tab_3)
        self.rsa_box_find_d.setObjectName("rsa_box_find_d")
        self.verticalLayout_11.addWidget(self.rsa_box_find_d)
        self.rsa_find_d = QtWidgets.QPushButton(self.tab_3)
        self.rsa_find_d.setObjectName("rsa_find_d")
        self.verticalLayout_11.addWidget(self.rsa_find_d)
        self.set_rsa = QtWidgets.QPushButton(self.tab_3)
        self.set_rsa.setObjectName("set_rsa")
        self.verticalLayout_11.addWidget(self.set_rsa)
        self.encrypt_decrypt_tab_2.addTab(self.tab_3, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_37 = QtWidgets.QLabel(self.tab_6)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_13.addWidget(self.label_37)
        self.anal_knapsack_m = QtWidgets.QLineEdit(self.tab_6)
        self.anal_knapsack_m.setObjectName("anal_knapsack_m")
        self.horizontalLayout_13.addWidget(self.anal_knapsack_m)
        self.label_36 = QtWidgets.QLabel(self.tab_6)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_13.addWidget(self.label_36)
        self.anal_knapsack_winverse = QtWidgets.QLineEdit(self.tab_6)
        self.anal_knapsack_winverse.setToolTip("")
        self.anal_knapsack_winverse.setToolTipDuration(3)
        self.anal_knapsack_winverse.setStatusTip("")
        self.anal_knapsack_winverse.setText("")
        self.anal_knapsack_winverse.setObjectName("anal_knapsack_winverse")
        self.horizontalLayout_13.addWidget(self.anal_knapsack_winverse)
        self.label_35 = QtWidgets.QLabel(self.tab_6)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_13.addWidget(self.label_35)
        self.anal_knapsack_w = QtWidgets.QLineEdit(self.tab_6)
        self.anal_knapsack_w.setObjectName("anal_knapsack_w")
        self.horizontalLayout_13.addWidget(self.anal_knapsack_w)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.label_34 = QtWidgets.QLabel(self.tab_6)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_13.addWidget(self.label_34)
        self.anal_hard_knapsack = QtWidgets.QTextEdit(self.tab_6)
        self.anal_hard_knapsack.setObjectName("anal_hard_knapsack")
        self.verticalLayout_13.addWidget(self.anal_hard_knapsack)
        self.label_38 = QtWidgets.QLabel(self.tab_6)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_13.addWidget(self.label_38)
        self.anal_ez_knapsack = QtWidgets.QTextEdit(self.tab_6)
        self.anal_ez_knapsack.setObjectName("anal_ez_knapsack")
        self.verticalLayout_13.addWidget(self.anal_ez_knapsack)
        self.find_ez_knapsack = QtWidgets.QPushButton(self.tab_6)
        self.find_ez_knapsack.setObjectName("find_ez_knapsack")
        self.verticalLayout_13.addWidget(self.find_ez_knapsack)
        self.set_knapsack = QtWidgets.QPushButton(self.tab_6)
        self.set_knapsack.setObjectName("set_knapsack")
        self.verticalLayout_13.addWidget(self.set_knapsack)
        self.encrypt_decrypt_tab_2.addTab(self.tab_6, "")
        self.horizontalLayout_3.addWidget(self.encrypt_decrypt_tab_2)
        self.main_tab.addTab(self.crypto_analysis, "")
        self.verticalLayout.addWidget(self.main_tab)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 20))
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
        self.main_tab.setCurrentIndex(0)
        self.encrypt_decrypt_tab.setCurrentIndex(4)
        self.encrypt_decrypt_tab_2.setCurrentIndex(5)
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
        self.label_19.setText(_translate("MainWindow", "N:"))
        self.label_20.setText(_translate("MainWindow", "E:"))
        self.label_21.setText(_translate("MainWindow", "D:"))
        self.label_22.setText(_translate("MainWindow", "Plain Numbers/Encoding Scheme: (Usually A = 01, B=02,..Z=26)"))
        self.label_16.setText(_translate("MainWindow", "Encrypted Numbers:"))
        self.rsa_encrypt_decrypt.setText(_translate("MainWindow", "Decrypt/Encrypt"))
        self.encrypt_decrypt_tab.setTabText(self.encrypt_decrypt_tab.indexOf(self.rsa), _translate("MainWindow", "RSA"))
        self.label_17.setText(_translate("MainWindow", "M:"))
        self.label_18.setText(_translate("MainWindow", "W:"))
        self.label_30.setText(_translate("MainWindow", "W-:"))
        self.label_31.setText(_translate("MainWindow", "Easy Knapsack:"))
        self.label_32.setText(_translate("MainWindow", "Binary Plain:"))
        self.label_33.setText(_translate("MainWindow", "Encoded (comma separated):"))
        self.knap_btn_encdec.setText(_translate("MainWindow", "Encode/Decode"))
        self.encrypt_decrypt_tab.setTabText(self.encrypt_decrypt_tab.indexOf(self.tab_4), _translate("MainWindow", "Knapsack"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.encrypt_decrypt), _translate("MainWindow", "Encrypt and Decrypt"))
        self.default_cipher.setText(_translate("MainWindow", "Set CipherText For All Analysis Options"))
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
        self.label_25.setText(_translate("MainWindow", "Try to find P and Q: (Extremely large numbers will not work.)"))
        self.label_23.setText(_translate("MainWindow", "N:"))
        self.label_24.setText(_translate("MainWindow", "Results:"))
        self.rsa_pq_button.setText(_translate("MainWindow", "Analyze"))
        self.label_26.setText(_translate("MainWindow", "Find D supplying P and Q along with the encryption key, E: "))
        self.label_27.setText(_translate("MainWindow", "P:"))
        self.label_28.setText(_translate("MainWindow", "Q:"))
        self.label_29.setText(_translate("MainWindow", "E:"))
        self.rsa_find_d.setText(_translate("MainWindow", "Find D"))
        self.set_rsa.setText(_translate("MainWindow", "Set N, E, and D in Encrypt/Decrypt Tab"))
        self.encrypt_decrypt_tab_2.setTabText(self.encrypt_decrypt_tab_2.indexOf(self.tab_3), _translate("MainWindow", "RSA"))
        self.label_37.setText(_translate("MainWindow", "M"))
        self.label_36.setText(_translate("MainWindow", "W-: (optional)"))
        self.label_35.setText(_translate("MainWindow", "W"))
        self.label_34.setText(_translate("MainWindow", "Hard Knapsack"))
        self.label_38.setText(_translate("MainWindow", "Easy Knapsack"))
        self.find_ez_knapsack.setText(_translate("MainWindow", "Find Easy Knapsack/W-"))
        self.set_knapsack.setText(_translate("MainWindow", "Set M, W, Easy Knapsack in Encrypt/Decrypt Tab"))
        self.encrypt_decrypt_tab_2.setTabText(self.encrypt_decrypt_tab_2.indexOf(self.tab_6), _translate("MainWindow", "Knapsack"))
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
