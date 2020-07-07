# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserSection.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_MainWindow(object):
    # function for database connection
    def dbcon(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="votingdb")
        return con

    # Function for message
    def message(self, title, msg):
        window = QtWidgets.QMessageBox()
        window.setWindowTitle(title)
        window.setText(msg)
        window.setStandardButtons(QtWidgets.QMessageBox.Ok)
        window.exec_()

    # Function for vote submitting
    def submitVote(self):
        con=self.dbcon()
        cursor=con.cursor()

        # Storing line edits data in variables
        voterName=self.lineEdit.text()
        voterIdCard=self.lineEdit_2.text()

        # Checking voter data in voter table
        checkReg="select * from voters where VoterIdCard=%s"
        cursor.execute(checkReg,(voterIdCard))
        countReg=cursor.rowcount

        # Checking vote in votes table
        checkVote="select * from votes where VoterIdCard=%s"
        cursor.execute(checkVote,(voterIdCard))
        countVote=cursor.rowcount

        # Checking user registration and vote
        # Also checking radio buttons
        if countReg!=1:
            self.message("Error","Your data is not present in our database.")
        elif countVote==1:
            self.message("Error","You have already submitted vote.")

        # Pti Vote
        elif self.radioButton.isChecked():
            vote="PTI"
            insert="insert into votes(VoterName,VoterIdCard,VoteParty) values(%s,%s,%s)"
            run=cursor.execute(insert,(voterName,voterIdCard,vote))
            if run:
                self.message("Submitted","Your vote submitted successfully. Thank you.")

        # PMLN Vote
        elif self.radioButton_2.isChecked():
            vote = "PMLN"
            insert = "insert into votes(VoterName,VoterIdCard,VoteParty) values(%s,%s,%s)"
            run = cursor.execute(insert, (voterName, voterIdCard, vote))
            if run:
                self.message("Submitted", "Your vote submitted successfully. Thank you.")

        # PPP Vote
        elif self.radioButton_3.isChecked():
            vote = "PPP"
            insert = "insert into votes(VoterName,VoterIdCard,VoteParty) values(%s,%s,%s)"
            run = cursor.execute(insert, (voterName, voterIdCard, vote))
            if run:
                self.message("Submitted", "Your vote submitted successfully. Thank you.")
        con.commit()
        con.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 348)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background-color: rgb(39, 107, 24);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 110, 431, 20))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(23, 116, 26);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 160, 431, 20))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(23, 116, 26);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(160, 230, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(320, 230, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(520, 230, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 270, 431, 23))
        self.pushButton.clicked.connect(self.submitVote)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 166, 23);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User Section - Version 1.2.1"))
        self.label.setText(_translate("MainWindow", "Voting Application"))
        self.label_2.setText(_translate("MainWindow", "Name :"))
        self.label_3.setText(_translate("MainWindow", "Id Card No :"))
        self.label_4.setText(_translate("MainWindow", "Select Vote :"))
        self.radioButton.setText(_translate("MainWindow", "TMC"))
        self.radioButton_2.setText(_translate("MainWindow", "BJP"))
        self.radioButton_3.setText(_translate("MainWindow", "CPI"))
        self.pushButton.setText(_translate("MainWindow", "Submit Vote"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
