import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtWidgets import QMenu,QToolTip,QPushButton,QMessageBox,QLabel
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

        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setWindowTitle(self.title)

        self.statusBar().showMessage('Ready')

        self.init_button()
        self.init_menu()

        label1 = QLabel('Parse Type',self)
        label1.move(100,100)




        #self.center_display()
        self.show()
    #@pyqtSlot()
    def init_button(self):
        button = QPushButton('button',self)
        button.setToolTip("example button")
        button.move(100,70)
        button.clicked.connect(self.on_click)

    def on_click(self):
        print('button click')

    def init_messagebox(self):
        button_reply = QMessageBox.question(self, 'message', 'Do you happy',
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
        if button_reply == QMessageBox.Yes:
            print('Yes')
        else:
            print('No')

    def init_menu(self):


        #self.statusBar()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        edit_menu = main_menu.addMenu('Edit')
        vide_menu = main_menu.addMenu('View')
        help_menu = main_menu.addMenu('Help')

        import_action = QAction('Import file', self)

        exit_action = QAction(QIcon('exit.png'),'&Exit',self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)
        file_menu.addAction(import_action)

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