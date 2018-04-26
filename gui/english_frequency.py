# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'english_frequency.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_english_freq_dialog(object):
    def setupUi(self, english_freq_dialog):
        english_freq_dialog.setObjectName("english_freq_dialog")
        english_freq_dialog.resize(712, 770)
        self.verticalLayout = QtWidgets.QVBoxLayout(english_freq_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(english_freq_dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.english_freq = MatplotlibWidget(english_freq_dialog)
        self.english_freq.setObjectName("english_freq")
        self.verticalLayout.addWidget(self.english_freq)
        self.buttonBox = QtWidgets.QDialogButtonBox(english_freq_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(english_freq_dialog)
        self.buttonBox.accepted.connect(english_freq_dialog.accept)
        self.buttonBox.rejected.connect(english_freq_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(english_freq_dialog)

    def retranslateUi(self, english_freq_dialog):
        _translate = QtCore.QCoreApplication.translate
        english_freq_dialog.setWindowTitle(_translate("english_freq_dialog", "English Frequency"))
        self.label.setText(_translate("english_freq_dialog", "English Frequency"))

from matplotlibwidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    english_freq_dialog = QtWidgets.QDialog()
    ui = Ui_english_freq_dialog()
    ui.setupUi(english_freq_dialog)
    english_freq_dialog.show()
    sys.exit(app.exec_())

