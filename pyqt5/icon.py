import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

#The Example class inherits from the QWidget class.
class Example(QWidget):
    def __init__(self):
        #The super() method returns the parent object of the Example class and we call it constructor.
        super().__init__()
        #The creation of the GUI is delegated to the initUI() method
        self.initUI()

    def initUI(self):
        #The setGeometry() does two things: it locates the window on the screen and sets it size.
        #The first two parameters are the x and y positions of the window.
        #The third is the width and the fourth is the height of the window.
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        #Set the application icon
        self.setWindowIcon(QIcon('web.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())