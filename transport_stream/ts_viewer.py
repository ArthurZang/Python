import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtWidgets import QMenu,QToolTip,QPushButton,QMessageBox,qApp
from PyQt5.QtWidgets import QDesktopWidget,QAction
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Transport Stream Viewer'
        self.left = 40
        self.top = 40
        self.width = 640
        self.height = 480
        self.init_UI()

    def init_UI(self):


        #self.init_menu()


        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setWindowTitle(self.title)

        self.statusBar().showMessage('Ready')
        #self.center_display()
        self.show()
    def init_menu(self):
        exit_action = QAction(QIcon('exit.png'),'&Exit',self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        #self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')

        import_menu = QMenu('Import',self)
        import_action = QAction('Import file', self)
        import_menu.addAction(import_action)

        file_menu.addMenu(import_menu)

        file_menu.addAction(exit_action)

    def center_display(self):
        # get the window
        widget = self.frameGeometry()
        # get the center_point of the screen
        center_point = QDesktopWidget().availableGeometry().center()
        # move the window to the center point
        widget.moveCenter(center_point)
        self.move(widget.topLeft())


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()