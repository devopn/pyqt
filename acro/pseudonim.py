import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.stones = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.stones.setObjectName("stones")
        self.horizontalLayout.addWidget(self.stones)
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.remainLcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.remainLcd.setObjectName("remainLcd")
        self.verticalLayout.addWidget(self.remainLcd)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.takeinput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.takeinput.setObjectName("takeinput")
        self.horizontalLayout_2.addWidget(self.takeinput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.takeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.takeButton.setObjectName("takeButton")
        self.verticalLayout.addWidget(self.takeButton)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.resultLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.resultLabel.setFont(font)
        self.resultLabel.setTextFormat(QtCore.Qt.AutoText)
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Stones:"))
        self.startButton.setText(_translate("Form", "Set"))
        self.label_2.setText(_translate("Form", "Take amount"))
        self.takeButton.setText(_translate("Form", "Take"))
        self.resultLabel.setText(_translate("Form", "TextLabel"))

class Pseudonym(QMainWindow, Ui_Form):
    stone_amount = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resultLabel.clear()

        self.startButton.clicked.connect(self.set)
        self.takeButton.clicked.connect(self.take)


    def set(self):
        self.listWidget.clear()
        self.stone_amount = self.stones.value()
        self.display()
        self.takeButton.setEnabled(True)
        self.resultLabel.clear()

    def display(self):
        self.remainLcd.display(self.stone_amount)

    def take(self):
        amount = self.takeinput.text()
        try:
            if (int(amount) > 0) and (int(amount) < 4):
                self.stone_amount -= int(amount)
                self.display()
                self.listWidget.addItem(f"Игрок взял - {amount}")
                if self.stone_amount <= 0:
                    self.resultLabel.setText("Победа пользователя!")
                    self.end_game()


                if (self.stone_amount <= 3) and (self.stone_amount > 0):
                    self.listWidget.addItem(f"Компьютер взял {self.stone_amount}")
                    self.stone_amount = 0
                    self.resultLabel.setText("Победа компьютера!")
                    self.end_game()

                else:
                    if self.stone_amount > 0:
                        stons = random.randint(1,3)
                        self.stone_amount -= stons
                        self.listWidget.addItem(f"Компьютер взял - {stons}")

        except ValueError:
            pass 
        self.display()
        
    def end_game(self):
        self.display()
        self.takeButton.setEnabled(False)



        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec_())
