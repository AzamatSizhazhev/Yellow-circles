from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import choice


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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

            range_num = choice([i for i in range(5, 13)])
            for _ in range(range_num):
                diameter = choice([j for j in range(20, 151)])
                qp.setBrush(QColor(255, 255, 0))
                x, y = choice([l for l in range(150, 451)]), choice([k for k in range(150, 351)])
                qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = YellowCircles()
    ex.show()
    exit(app.exec_())
