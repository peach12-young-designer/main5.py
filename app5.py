# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\am745\Desktop\kmzip5\app5.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1178, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.samplenum1 = QtWidgets.QPushButton(self.centralwidget)
        self.samplenum1.setGeometry(QtCore.QRect(0, 30, 151, 23))
        self.samplenum1.setObjectName("samplenum1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 3, 151, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 141, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.samplenum2 = QtWidgets.QPushButton(self.centralwidget)
        self.samplenum2.setGeometry(QtCore.QRect(170, 30, 161, 23))
        self.samplenum2.setObjectName("samplenum2")
        self.openkey = QtWidgets.QPushButton(self.centralwidget)
        self.openkey.setGeometry(QtCore.QRect(350, 30, 161, 23))
        self.openkey.setObjectName("openkey")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 10, 161, 20))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.closedkey = QtWidgets.QPushButton(self.centralwidget)
        self.closedkey.setGeometry(QtCore.QRect(530, 30, 181, 23))
        self.closedkey.setObjectName("closedkey")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 10, 181, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.shareopenkey = QtWidgets.QPushButton(self.centralwidget)
        self.shareopenkey.setGeometry(QtCore.QRect(740, 30, 161, 23))
        self.shareopenkey.setObjectName("shareopenkey")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(740, 10, 161, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 270, 1221, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.getopenkey = QtWidgets.QPushButton(self.centralwidget)
        self.getopenkey.setGeometry(QtCore.QRect(0, 320, 161, 23))
        self.getopenkey.setObjectName("getopenkey")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 300, 161, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.shifrmessege = QtWidgets.QPushButton(self.centralwidget)
        self.shifrmessege.setGeometry(QtCore.QRect(180, 320, 171, 23))
        self.shifrmessege.setObjectName("shifrmessege")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 300, 171, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.sharemessege = QtWidgets.QPushButton(self.centralwidget)
        self.sharemessege.setGeometry(QtCore.QRect(380, 320, 211, 23))
        self.sharemessege.setObjectName("sharemessege")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 300, 211, 16))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 231, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 120, 231, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 160, 231, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 190, 231, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 360, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(250, 80, 201, 16))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(250, 120, 151, 16))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 160, 131, 16))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(250, 190, 131, 16))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(250, 220, 131, 16))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1030, 20, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1040, 300, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1178, 21))
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
        self.samplenum1.setText(_translate("MainWindow", "?????????????????? ???????????????? ?????????? 1"))
        self.samplenum2.setText(_translate("MainWindow", "?????????????????? ???????????????? ?????????? 2"))
        self.openkey.setText(_translate("MainWindow", "???????????????? ????????"))
        self.closedkey.setText(_translate("MainWindow", "???????????????? ????????"))
        self.shareopenkey.setText(_translate("MainWindow", "???????????????????? ?????????????? ????????????"))
        self.getopenkey.setText(_translate("MainWindow", "???????????????? ???????????????? ????????"))
        self.shifrmessege.setText(_translate("MainWindow", "?????????????????????? ??????????????????"))
        self.sharemessege.setText(_translate("MainWindow", "?????????????????? ?????????????????????????? ??????????????????"))
        self.pushButton.setText(_translate("MainWindow", "???????????????? ?????????????????????????? ??????????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "???????????????????????? ??????????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "???????????????? ???? ???????????????? 1"))
        self.pushButton_4.setText(_translate("MainWindow", "???????????????? ???? ???????????????? 2"))
        self.label_14.setText(_translate("MainWindow", "????????????????????"))
        self.label_15.setText(_translate("MainWindow", "??????????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
