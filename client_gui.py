from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time
import client

#########################
# Window Size DEF
#########################
XPOS = 600
YPOS = 200
WIDTH = 560
HEIGTH = 600

#########################
# Wigdegts Size DEF
#########################

# left margin
L_MARGIN = 25
TOP_MARGIN = 50

# output text area def
OUT_TEXT_X = L_MARGIN + 20
OUT_TEXT_Y = TOP_MARGIN
OUT_TEXT_W = 380
OUT_TEXT_H = HEIGTH - TOP_MARGIN - 60

# in: label pos
IN_LABEL_X = L_MARGIN
IN_LABEL_Y = HEIGTH - 50

# input textbox def
SEND_TEXT_X = IN_LABEL_X + 20
SEND_TEXT_Y = IN_LABEL_Y
SEND_TEXT_W = OUT_TEXT_W
SEND_TEXT_H = 30

# SEND Button pos
SEND_BUTTON_X = SEND_TEXT_X + SEND_TEXT_W + 10
SEND_BUTTON_Y = IN_LABEL_Y

# DISSC Button def
DISSC_BUTTON_X = 0
DISSC_BUTTON_Y = 0


class ClientWindow(QMainWindow):
    def __init__(self):
        super(ClientWindow, self).__init__()
        self.setGeometry(XPOS, YPOS, WIDTH, HEIGTH)
        self.setWindowTitle("Chat App")
        self.initUI()
        
    def initUI(self):
        welcome_msg = client.recv()
        self.out_textarea = QtWidgets.QPlainTextEdit(self)
        self.out_textarea.insertPlainText(welcome_msg)
        self.out_textarea.move(OUT_TEXT_X, OUT_TEXT_Y)
        self.out_textarea.resize(OUT_TEXT_W, OUT_TEXT_H)
        self.out_textarea.setReadOnly(True)
        
        self.in_label = QtWidgets.QLabel(self)
        self.in_label.setText("in:")
        self.in_label.move(IN_LABEL_X, IN_LABEL_Y)

        self.in_textbox = QtWidgets.QLineEdit(self)
        self.in_textbox.move(SEND_TEXT_X, SEND_TEXT_Y)
        self.in_textbox.resize(SEND_TEXT_W, SEND_TEXT_H)

        self.send_button = QtWidgets.QPushButton(self)
        self.send_button.setText("SEND")
        self.send_button.move(SEND_BUTTON_X, SEND_BUTTON_Y)
        # this called signals in PyQt...
        self.send_button.clicked.connect(self.send_clicked)

        self.dissc_button = QtWidgets.QPushButton(self)
        self.dissc_button.setText("dissconnect")
        self.dissc_button.move(DISSC_BUTTON_X, DISSC_BUTTON_Y)
        # this called signals in PyQt...
        self.dissc_button.clicked.connect(self.dissc_clicked)

    def send_clicked(self):
        self.refresh_textboxarea()
        self.update()

    def dissc_clicked(self):
        client.dissconnect()
        exit_print = "[SERVER] --- dissconnected successfully --- [\\SERVER]\n"
        self.out_textarea.appendPlainText(exit_print)
        self.in_textbox.setText('')
        self.dissable_input()

    def dissable_input(self):
        self.in_textbox.setReadOnly(True)
        self.send_button.setEnabled(False)
        self.dissc_button.setEnabled(False)
    
    def update(self):
##        self.in_label.adjustSize()
        pass
    
    
    def refresh_textboxarea(self):
        my_msg = self.in_textbox.text()
        my_input = 'You >>> ' + my_msg
        self.out_textarea.appendPlainText(my_input)
        self.in_textbox.setText('')
        server_reply = '[SERVER] --- ' +self.send_msg(my_msg)+ ' --- [\\SERVER]'
        self.out_textarea.appendPlainText(server_reply + '\n')

    def send_msg(self, msg):
        return client.send(msg)
        


def window():
    app = QApplication(sys.argv)
    win = ClientWindow()
    
    win.show()
    
    sys.exit(app.exec_())

window()
