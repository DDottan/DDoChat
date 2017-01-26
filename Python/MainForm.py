# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("DDoChat")
        Form.resize(800, 600)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 550, 701, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.edChat = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edChat.setObjectName("edChat")

        self.horizontalLayout.addWidget(self.edChat)

        self.btSend = QtWidgets.QPushButton(Form)
        self.btSend.setGeometry(QtCore.QRect(720, 560, 71, 23))
        self.btSend.setObjectName("btSend")

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 11, 781, 531))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.edChat.setFocus()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("DDoChat", "DDoChat"))
        self.btSend.setText(_translate("Form", "Send"))


class MainForm(object):

    def __init__(self):
        self.OnSend = None

        self.form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)

        self.ui.btSend.clicked.connect(self.on_btSend_clicked)
        self.ui.edChat.returnPressed.connect(self.on_btSend_clicked)

    def show(self):
        self.form.show()

    def on_btSend_clicked(self):
        if self.OnSend != None:
            self.OnSend( self.ui.edChat.text() )
        self.ui.edChat.setText("")

    def setOnSend(self, event_handler):
        self.OnSend = event_handler
        