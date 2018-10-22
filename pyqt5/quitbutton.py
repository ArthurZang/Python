import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #We create a push button.
        #The first parameter is the label of the button,
        #The second parameter is the parent widget
        qbtn = QPushButton('Quit', self)

        #If we click on the button, the signal clicked is emitted.
        #The clicked signal is connected to the quit() method
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(300,300,250,250)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
