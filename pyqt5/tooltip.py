import sys
from PyQt5.QtWidgets import (QWidget,QToolTip,QPushButton,QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #We use a 10pt SansSerif font.
        QToolTip.setFont(QFont('SansSerif',10))
        #To create a tooltip
        self.setToolTip('This is a <b>QWidget</b> widget')

        #We create a push button widget and set a tooltip for it
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        #The button is resized and moved on the window
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
