import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QCheckBox,
    QPlainTextEdit,
    QLineEdit
)


class MyWidget(QWidget):
    menu = {"Чизбургер": 10, "Гамбургер": 20, "Кока-кола": 15, "Нагетсы": 30}
    price = 0
    checkboxes = []
    inputs = []

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 470, len(self.menu) * 40 + len(self.menu) * 40 + 150)
        self.setWindowTitle("Заказ в Макдональдсе")



        # Button
        self.orderButton = QPushButton("Заказать", self)
        self.orderButton.adjustSize()
        self.orderButton.move(10, 30 + len(self.menu) * 40)
        self.orderButton.clicked.connect(self.order)

        # QLineEdit
        for i in range(len(self.menu)):
            obj = QLineEdit(self)
            obj.move(150, 20 + 40 * i)
            obj.setEnabled(False)
            obj.setText("0")
            self.inputs.append(obj)

        for i in range(len(self.menu)):
            obj = QCheckBox(list(self.menu.keys())[i], self)
            obj.move(10, 20 + 40 * i)
            obj.toggled.connect(self.make_change_state(i))
            self.checkboxes.append(obj)

        # QPlainTextEdit
        self.result = QPlainTextEdit(self)
        self.result.setEnabled(False)
        self.result.resize(400, 50 * len(self.menu))
        self.result.move(10, 40 + len(self.menu) * 40 + 50)

    def make_change_state(self, i):
        def change_state(a):
            self.inputs[i].setEnabled(self.checkboxes[i].isChecked())
            self.inputs[i].setText("1")

        return change_state

    def order(self):
        self.price = 0
        s = self.checkboxes
        order = []
        for i in range(len(s)):
            if s[i].isChecked():
                self.price += int(self.inputs[i].text()) * self.menu[s[i].text()]
                order.append(s[i].text() + '-' * 5 + str(int(self.inputs[i].text())) + '-' * 5 + str(int(self.inputs[i].text()) * self.menu[s[i].text()]))
        self.result.clear()
        self.result.insertPlainText("Ваш заказ:\n\n" + "\n".join(order) + "\n\nИтого: " + str(self.price))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
