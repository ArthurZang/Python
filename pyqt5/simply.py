#Here we provide the necessary imports.
#The basic widgets are located in PyQt5.QtWidgets module.
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    #Every PyQt5 application must create an application object.
    #The sys.argv parameter is a list of arguments from a command line.
    app = QApplication(sys.argv)

    #The QWidget widget is the base class of all user interface objects in PyQt5.
    w = QWidget()

    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('Simple')
    #The show() method displays the widget on the screen.
    w.show()

    sys.exit(app.exec_())