# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textsplit.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_split_Dialog(object):
    def setupUi(self, split_Dialog):
        split_Dialog.setObjectName("split_Dialog")
        split_Dialog.resize(529, 461)
        self.verticalLayout = QtWidgets.QVBoxLayout(split_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(split_Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(split_Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(split_Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.split_encrypted = QtWidgets.QTextEdit(split_Dialog)
        self.split_encrypted.setObjectName("split_encrypted")
        self.verticalLayout.addWidget(self.split_encrypted)
        self.label_3 = QtWidgets.QLabel(split_Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.split_result = QtWidgets.QTextEdit(split_Dialog)
        self.split_result.setObjectName("split_result")
        self.verticalLayout.addWidget(self.split_result)
        self.split_analyze = QtWidgets.QPushButton(split_Dialog)
        self.split_analyze.setObjectName("split_analyze")
        self.verticalLayout.addWidget(self.split_analyze)
        self.buttonBox = QtWidgets.QDialogButtonBox(split_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(split_Dialog)
        self.buttonBox.accepted.connect(split_Dialog.accept)
        self.buttonBox.rejected.connect(split_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(split_Dialog)

    def retranslateUi(self, split_Dialog):
        _translate = QtCore.QCoreApplication.translate
        split_Dialog.setWindowTitle(_translate("split_Dialog", "Split Text"))
        self.label.setText(_translate("split_Dialog", "Key Length (Number of splits. You can determine this from the Kasiski test)"))
        self.label_2.setText(_translate("split_Dialog", "Encrypted Text"))
        self.label_3.setText(_translate("split_Dialog", "Result"))
        self.split_analyze.setText(_translate("split_Dialog", "Analyze"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    split_Dialog = QtWidgets.QDialog()
    ui = Ui_split_Dialog()
    ui.setupUi(split_Dialog)
    split_Dialog.show()
    sys.exit(app.exec_())

