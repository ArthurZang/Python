import sys
from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #QAction is an abstraction for actions performed with a menubar,toolbar, or with a custom keyboard
        #We create an action with a specific icon and an 'Exit' label.
        exitAct = QAction(QIcon('exit.png'),'&Exit',self)
        #We define a shortcut for this action
        exitAct.setShortcut('Ctrl+Q')
        #Create a status tip which is shown in the statusbar when we hover a mouse pointer over the menu item.
        exitAct.setStatusTip('Exit application')
        #When we select this particular action, a triggered signal is emitted.
        #The signal is connected to the quit() method of the QApplication widget.
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Simple menu')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())