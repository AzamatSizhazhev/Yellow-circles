from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randrange
from UI import Ui_MainWindow


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и желтые окружности')
        self.painting = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.painting = True
        self.repaint()

    def paintEvent(self, event):
        if self.painting:
            qp = QPainter()
            qp.begin(self)

            range_num = randrange(5, 13)
            for _ in range(range_num):
                diameter = randrange(20, 151)
                x, y = randrange(150, 451), randrange(150, 351)
                red = randrange(0, 256)
                green = randrange(0, 256)
                blue = randrange(0, 256)
                qp.setBrush(QColor(red, green, blue))
                qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = YellowCircles()
    ex.show()
    exit(app.exec_())
