# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filmBul.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests

from bs4 import BeautifulSoup

class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(435, 549)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 381, 451))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 480, 41, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 480, 101, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 480, 201, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.getir)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "IMDB Puanını Giriniz : "))
        self.pushButton.setText(_translate("Form", "ÇALIŞ"))

    def getir(self):

        self.textEdit.clear()
        url = "http://www.imdb.com/chart/top"

        response = requests.get(url)

        html_icerigi = response.content

        soup = BeautifulSoup(html_icerigi, "html.parser")


        a = float(self.plainTextEdit.toPlainText())

        basliklar = soup.find_all("td", {"class": "titleColumn"})
        ratingler = soup.find_all("td", {"class", "ratingColumn imdbRating"})

        for baslik, rating in zip(basliklar, ratingler):
            baslik = baslik.text
            rating = rating.text

            baslik = baslik.strip()
            baslik = baslik.replace("\n", "")

            rating = rating.strip()
            rating = rating.replace("\n", "")

            if (float(rating) > a):
                self.textEdit.append("Film ismi: {} Filmin Ratingi : {}".format(baslik, rating))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

