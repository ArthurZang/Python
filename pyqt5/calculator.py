import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #The instance of a QGridLayout is created and set to be the layout for the window
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['cls','Bck','','Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']
        #We create a list of position in the grid
        positions = [(i,j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            #buttons are created and added to the layout
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())