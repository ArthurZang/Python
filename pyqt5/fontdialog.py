import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QSizePolicy,QLabel,QFontDialog

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        self.btn = QPushButton('Dialog',self)
        self.btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.btn.move(20,20)

        vbox.addWidget(self.btn)

        self.btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130,20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Main window')
        self.show()
    def showDialog(self):
        font,ok = QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())