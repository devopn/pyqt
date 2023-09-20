import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
from calc_sheet import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    buttons = dict()
    request, now = "0", ""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Generate dict of buttons

        for i in self.buttonGroup_digits.buttons():
            digit = i.text()
            i.clicked.connect(self.make_click_digit(digit))
            self.buttons.update({digit: i})

        for button in self.buttonGroup_binary.buttons():
            print(button.text())

        self.btn_plus.clicked.connect(self.make_operand("+"))
        self.btn_div.clicked.connect(self.make_operand("/"))
        self.btn_minus.clicked.connect(self.make_operand("-"))
        self.btn_mult.clicked.connect(self.make_operand("*"))
        self.btn_pow.clicked.connect(self.make_operand("**"))
        self.btn_dot.clicked.connect(self.dot)
        self.btn_eq.clicked.connect(self.calculate)
        self.btn_clear.clicked.connect(self.clear_display)

    def make_click_digit(self, digit):

        def click_digit(a):
            self.now += digit
            self.display_update()
            print(self.now)
        
        return click_digit
    
    # Function to display nums in qlcd
    def display_update(self):
        self.table.display(self.now)

    # Function to clear display
    def clear_display(self):
        self.now,self.request = "", ""
        self.display_update()
    
    def make_operand(self, oper):
        def operand(a):
            self.request = "(" + self.request + oper + ")"
            self.now = ""
            self.display_update()

        return operand

    def dot(self):
        self.now += "."
        self.display_update()

    def calculate(self):
        self.now = str(eval(self.request + self.now))
        print(self.request, self.now)
        self.display_update()

    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

