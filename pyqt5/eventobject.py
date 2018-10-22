import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication,QGridLayout,QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()

        x = 0
        y = 0

        #the x and y coordinates are displayed in a QLabel widget
        self.text = "x: {0}, y: {1}".format(x,y)
        self.label = QLabel(self.text, self)

        grid.addWidget(self.label, 0,0,Qt.AlignTop)

        #mouse tracking is disabled by default, so the widget only receives mouse move evnets
        #when at least one mouse button is pressed while the mouse is being moved.
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Main window')
        self.show()

    #the e is the event object; it contains data about the event that was triggered
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x:{0}, y:{1}".format(x,y)
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())