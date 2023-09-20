import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
from book_sheet import Ui_MainWindow


class MyNotes(QMainWindow, Ui_MainWindow):
    buttons = dict()
    request, now = "0", ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addContactBtn.clicked.connect(self.add_contact)

    def add_contact(self):
        self.contactList.addItem(
            self.contactName.text() + " " + self.contactNumber.text()
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec_())
