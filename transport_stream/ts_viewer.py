import sys
from ts_file import TSFile,PTS_SIZE
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QMessageBox
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

'''
class Application(tk.Frame):
    def create_widgets(self):
        ts_file = TSFile("mepg2.ts")
        file_data = list()
        for i in range(PTS_SIZE):
            data = ts_file.read_file(i,1)
            file_data.append(hex(data))

        font = tkFont.Font(size=20)
        self.hello_lable = tk.Label(self, text=file_data,width = 128,wraplength=512*2,font=font)
        self.hello_lable.pack()
        self.quit_button = tk.Button(self,text='Quit', command=self.quit)
        self.quit_button.pack()

'''
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):

        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a button widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        quit_btn = QPushButton('Quit', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.move(50, 100)

        self.setGeometry(300,300,300,220)
        self.setWindowTitle('TS Viewer')
        #get the window
        widget = self.frameGeometry()
        #get the center_point of the screen
        center_point = QDesktopWidget().availableGeometry().center()
        #move the window to the center point
        widget.moveCenter(center_point)
        self.move(widget.topLeft())

        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes|QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



def main():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()