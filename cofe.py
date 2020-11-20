import sqlite3
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from cofee import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("cofeee.db")
        self.ph = {}
        self.cur = self.connection.cursor()
        self.ph2 = self.cur.execute("""SELECT * FROM cofee """).fetchall()
        self.setcombobox()
        self.pushButton.clicked.connect(self.run)

    def setcombobox(self):
        r = []
        pharms = self.cur.execute("""SELECT name FROM cofee """).fetchall()
        for k in pharms:
            r.append(k[0])
        self.comboBox.addItems(r)

    def run(self):
        self.ph2 = self.cur.execute("SELECT * FROM cofee WHERE name LIKE '%{}%'".format(self.comboBox.currentText()))
        self.ph2 = self.ph2.fetchall()
        self.lineEdit.setText(str(self.ph2[0][0]))
        self.lineEdit_2.setText(str(self.ph2[0][1]))
        self.lineEdit_3.setText(str(self.ph2[0][2]))
        self.lineEdit_4.setText(str(self.ph2[0][3]))
        self.textEdit.setText(str(self.ph2[0][4]))
        self.lineEdit_6.setText(str(self.ph2[0][5]))
        self.lineEdit_7.setText(str(self.ph2[0][6]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())