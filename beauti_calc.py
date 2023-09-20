import sys


from PyQt5.QtWidgets import QApplication, QMainWindow
from calc_sheet import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    buttons = dict()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for i in self.buttonGroup_digits:


        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

