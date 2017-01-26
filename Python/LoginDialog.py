# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import urllib.request, hashlib, json
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 160, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.edUserID = QtWidgets.QLineEdit(Dialog)
        self.edUserID.setGeometry(QtCore.QRect(90, 20, 201, 20))
        self.edUserID.setObjectName("edUserID")
        self.edUserPW = QtWidgets.QLineEdit(Dialog)
        self.edUserPW.setGeometry(QtCore.QRect(90, 50, 201, 20)) 
        self.edUserPW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edUserPW.setObjectName("edUserPW")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 56, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 56, 21))
        self.label_2.setObjectName("label_2")
        self.lbError = QtWidgets.QLabel(Dialog)
        self.lbError.setGeometry(QtCore.QRect(20, 100, 271, 21))
        self.lbError.setStyleSheet("color : red; ")
        self.lbError.setAlignment(QtCore.Qt.AlignCenter)
        self.lbError.setObjectName("lbError")

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.edUserID.setFocus()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "로그인"))
        self.label.setText(_translate("Dialog", "아이디"))
        self.label_2.setText(_translate("Dialog", "암호"))


class LoginDialog(object):

    def __init__(self):
        self.OnLogined = None
        self.user_name = None

        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.buttonBox.accepted.connect(self.on_login)

    def show(self):
        self.dialog.show()

    def on_login(self):
        self.ui.lbError.setText("")

        m = hashlib.md5()
        m.update(self.ui.edUserPW.text().encode())
        user_pw = m.hexdigest()

        url = "http://www.ddottan.com/api/login?user_id=%s&user_pw=%s" % (self.ui.edUserID.text(), user_pw)
        req = urllib.request.Request(url)
        data = urllib.request.urlopen(req).read()
        result = json.loads( data.decode() )

        print(data)

        if result["result"] ==  "ok":
            self.user_name = result["user_name"]
            if self.OnLogined != None:
                self.OnLogined()
            self.dialog.accept()
        else:
            self.ui.lbError.setText("아이디나 암호를 다시 확인해주시기 바랍니다.")            

    def setOnLogined(self, event_handler):
        self.OnLogined = event_handler


