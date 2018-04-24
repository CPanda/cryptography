# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_graph.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_save_graph(object):
    def setupUi(self, save_graph):
        save_graph.setObjectName("save_graph")
        save_graph.resize(352, 164)
        self.verticalLayout = QtWidgets.QVBoxLayout(save_graph)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(save_graph)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(save_graph)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.save_image = QtWidgets.QPushButton(save_graph)
        self.save_image.setObjectName("save_image")
        self.verticalLayout.addWidget(self.save_image)
        self.buttonBox = QtWidgets.QDialogButtonBox(save_graph)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(save_graph)
        QtCore.QMetaObject.connectSlotsByName(save_graph)

    def retranslateUi(self, save_graph):
        _translate = QtCore.QCoreApplication.translate
        save_graph.setWindowTitle(_translate("save_graph", "Save Graph"))
        self.label.setText(_translate("save_graph", "Save Current Graph:"))
        self.lineEdit.setText(_translate("save_graph", "graph.png"))
        self.save_image.setText(_translate("save_graph", "Save Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    save_graph = QtWidgets.QDialog()
    ui = Ui_save_graph()
    ui.setupUi(save_graph)
    save_graph.show()
    sys.exit(app.exec_())

