from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication
import sys


class WidgetArt(QWidget):
    
    
    def __init__(self, matrix):
        self.matrix = matrix
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle("WidgetArt")
        widgetArt = QGridLayout(self)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                widgetArt.addWidget(
                    QPushButton("*" if self.matrix[i][j] == 1 else ""), i, j
                )




if __name__ == "__main__":
    app = QApplication(sys.argv)
    matrix = [
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
]
    ex = WidgetArt(matrix)
    ex.show()
    sys.exit(app.exec_())
