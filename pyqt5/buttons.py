import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QHBoxLayout,QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        #We create a horizontal box layout and add a stretch factor and both buttons
        #The stretch adds a stretchable space before two buttons.
        #This will push them to the right of the window
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        #The horizontal layout is placed into the vertical layout.
        #The stretch factor in the vertical box will push the horizontal box to the bottom of the window
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Main window')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())