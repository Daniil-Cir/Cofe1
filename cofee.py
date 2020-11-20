# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cofee.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 552)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 20, 261, 31))
        self.comboBox.setStyleSheet("background-color: #77777e")
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, -10, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Swiss921 BT")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: #ff6666;\n"
"    background-color: #222222;\n"
"    border-color: rgb(66, 69, 183);\n"
"     border-width: 3px;        \n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"     margin:30px;\n"
"     padding:30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #333333;\n"
"    color: 220000;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 90, 161, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 100, 331, 31))
        self.lineEdit.setStyleSheet("color: white;\n"
"background-color: #555555;\n"
"border-radius: 10")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 150, 331, 31))
        self.lineEdit_2.setStyleSheet("color: white;\n"
"background-color: #555555;\n"
"border-radius: 10")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 200, 331, 31))
        self.lineEdit_3.setStyleSheet("color: white;\n"
"background-color: #555555;\n"
"border-radius: 10")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 260, 331, 31))
        self.lineEdit_4.setStyleSheet("color: white;\n"
"background-color: #555555;\n"
"border-radius: 10")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 370, 331, 31))
        self.lineEdit_6.setStyleSheet("color: white;\n"
"background-color: #555555;\n"
"border-radius: 10")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 420, 331, 31))
        self.lineEdit_7.setStyleSheet("color: white;\n"
"background-color: #555555;\n"
"border-radius: 10")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 300, 331, 51))
        self.textEdit.setStyleSheet("color: white;\n"
"background-color: #555555;\n"
"border-radius: 8")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Найти"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.label_2.setText(_translate("MainWindow", "Название сорта:"))
        self.label_3.setText(_translate("MainWindow", "Cтепень обжарки:"))
        self.label_4.setText(_translate("MainWindow", "Молотый/в зернах:"))
        self.label_5.setText(_translate("MainWindow", "Описание вкуса:"))
        self.label_6.setText(_translate("MainWindow", "Цена:"))
        self.label_7.setText(_translate("MainWindow", "Объем упаковки:"))