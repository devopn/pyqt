from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 96)
        self.button = QtWidgets.QPushButton(Form)
        self.button.setGeometry(QtCore.QRect(10, 40, 65, 20))
        self.button.setObjectName("button")
        self.text_field = QtWidgets.QTextEdit(Form)
        self.text_field.setGeometry(QtCore.QRect(100, 20, 271, 64))
        self.text_field.setObjectName("text_field")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button.setText(_translate("Form", "PushButton"))


class Pseudonym(QtWidgets, Ui_Form):
    stone_amount = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resultLabel.clear()

        self.startButton.clicked.connect(self.set)
        self.takeButton.clicked.connect(self.take)





if __name__ == "__main__":
    app = QtWidgets(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec_())
