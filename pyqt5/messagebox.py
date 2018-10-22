import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,250)
        self.setWindowTitle('Quit button')
        self.show()

    def closeEvent(self,event):
        #We show a message box with two buttons: Yes and No.
        #The first string appears on the titlebar.
        #The second string is the message text display by the dialog
        #The third argument specifies the combination of buttons appearing int the dialog
        #The last parameter is the default button.
        reply = QMessageBox.question(self,'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
