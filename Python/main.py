from PyQt5 import QtCore, QtGui, QtWidgets
import LoginDialog, MainForm, RyuSocketClient

def on_logined():
    form.show()

def on_send(msg):
    socket.send(login.user_name + "> "+ msg)

def on_received(msg):
    form.ui.textBrowser.append(msg)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    login = LoginDialog.LoginDialog()
    form = MainForm.MainForm()
    socket = RyuSocketClient.RyuSocketClient()

    socket.connect( "127.0.0.1", 1234)

    login.setOnLogined(on_logined)
    form.setOnSend(on_send)
    socket.setOnReceived(on_received)

    login.show()

    sys.exit(app.exec_())