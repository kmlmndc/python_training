# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagedesign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PIL import Image, ImageFilter

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QAction, qApp, QMainWindow

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class Ui_Form(QtWidgets.QMainWindow):
    image_name = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1046, 847)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 740, 1022, 102))
        self.layoutWidget.setObjectName("layoutWidget")
        self.outer = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.outer.setContentsMargins(5, 5, 5, 5)
        self.outer.setObjectName("outer")
        self.middle_1 = QtWidgets.QHBoxLayout()
        self.middle_1.setContentsMargins(5, 5, 5, 5)
        self.middle_1.setObjectName("middle_1")
        self.inner_1 = QtWidgets.QHBoxLayout()
        self.inner_1.setContentsMargins(5, 5, 5, 5)
        self.inner_1.setObjectName("inner_1")
        self.open = QtWidgets.QPushButton(self.layoutWidget)
        self.open.setObjectName("open")
        self.inner_1.addWidget(self.open)
        self.Save = QtWidgets.QPushButton(self.layoutWidget)
        self.Save.setObjectName("Save")
        self.inner_1.addWidget(self.Save)
        self.middle_1.addLayout(self.inner_1)
        self.inner_2 = QtWidgets.QHBoxLayout()
        self.inner_2.setContentsMargins(5, 5, 5, 5)
        self.inner_2.setObjectName("inner_2")
        self.convert = QtWidgets.QPushButton(self.layoutWidget)
        self.convert.setObjectName("convert")
        self.inner_2.addWidget(self.convert)
        self.inputConvert = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputConvert.setText("")
        self.inputConvert.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputConvert.setObjectName("inputConvert")
        self.inner_2.addWidget(self.inputConvert)
        self.middle_1.addLayout(self.inner_2)
        self.inner_3 = QtWidgets.QHBoxLayout()
        self.inner_3.setContentsMargins(5, 5, 5, 5)
        self.inner_3.setObjectName("inner_3")
        self.rotate = QtWidgets.QPushButton(self.layoutWidget)
        self.rotate.setObjectName("rotate")
        self.inner_3.addWidget(self.rotate)
        self.inputRotate = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputRotate.setText("")
        self.inputRotate.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputRotate.setObjectName("inputRotate")
        self.inner_3.addWidget(self.inputRotate)
        self.middle_1.addLayout(self.inner_3)
        self.inner_4 = QtWidgets.QHBoxLayout()
        self.inner_4.setContentsMargins(5, 5, 5, 5)
        self.inner_4.setObjectName("inner_4")
        self.Filter = QtWidgets.QPushButton(self.layoutWidget)
        self.Filter.setObjectName("Filter")
        self.inner_4.addWidget(self.Filter)
        self.inputFilter = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputFilter.setText("")
        self.inputFilter.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputFilter.setObjectName("inputFilter")
        self.inner_4.addWidget(self.inputFilter)
        self.middle_1.addLayout(self.inner_4)
        self.outer.addLayout(self.middle_1)
        self.middle_2 = QtWidgets.QHBoxLayout()
        self.middle_2.setContentsMargins(5, 5, 5, 5)
        self.middle_2.setObjectName("middle_2")
        self.inner_5 = QtWidgets.QHBoxLayout()
        self.inner_5.setContentsMargins(5, 5, 5, 5)
        self.inner_5.setObjectName("inner_5")
        self.resize = QtWidgets.QPushButton(self.layoutWidget)
        self.resize.setObjectName("resize")
        self.inner_5.addWidget(self.resize)
        self.inputResize_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputResize_1.setText("")
        self.inputResize_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputResize_1.setObjectName("inputResize_1")
        self.inner_5.addWidget(self.inputResize_1)
        self.inputResize_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputResize_2.setText("")
        self.inputResize_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputResize_2.setObjectName("inputResize_2")
        self.inner_5.addWidget(self.inputResize_2)
        self.middle_2.addLayout(self.inner_5)
        self.inner_6 = QtWidgets.QHBoxLayout()
        self.inner_6.setContentsMargins(5, 5, 5, 5)
        self.inner_6.setObjectName("inner_6")
        self.Crop = QtWidgets.QPushButton(self.layoutWidget)
        self.Crop.setObjectName("Crop")
        self.inner_6.addWidget(self.Crop)
        self.inputCrop_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputCrop_1.setText("")
        self.inputCrop_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputCrop_1.setObjectName("inputCrop_1")
        self.inner_6.addWidget(self.inputCrop_1)
        self.inputCrop_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputCrop_2.setText("")
        self.inputCrop_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputCrop_2.setObjectName("inputCrop_2")
        self.inner_6.addWidget(self.inputCrop_2)
        self.inputCrop_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputCrop_3.setText("")
        self.inputCrop_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputCrop_3.setObjectName("inputCrop_3")
        self.inner_6.addWidget(self.inputCrop_3)
        self.inputCrop_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputCrop_4.setText("")
        self.inputCrop_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputCrop_4.setObjectName("inputCrop_4")
        self.inner_6.addWidget(self.inputCrop_4)
        self.middle_2.addLayout(self.inner_6)
        self.outer.addLayout(self.middle_2)
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(6, 2, 1021, 731))
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setObjectName("image")

        self.open.clicked.connect(self.openFile)
        self.Save.clicked.connect(self.saveFile)
        self.convert.clicked.connect(self.convert_image)
        self.rotate.clicked.connect(self.rotate_images)
        self.Filter.clicked.connect(self.filter_images)
        self.resize.clicked.connect(self.resize_images)
        self.Crop.clicked.connect(self.crop_images)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.open.setText(_translate("Form", "Open"))
        self.Save.setText(_translate("Form", "Save"))
        self.convert.setText(_translate("Form", "Convert (L ya da 1)"))
        self.rotate.setText(_translate("Form", "Rotate(0-360)"))
        self.Filter.setText(_translate("Form", "Filter(0-50)"))
        self.resize.setText(_translate("Form", "Resize"))
        self.Crop.setText(_translate("Form", "Crop"))

    def openFile(self):
        try:
            file_name = QFileDialog.getOpenFileName(self,"Open File", os.getenv("HOME"))
            self.image.setPixmap(QtGui.QPixmap(file_name[0]))
            self.image_name = file_name[0]
        except:
            self.image.setText("Bir Hata Oluştu...\nTekrar Deneyiniz.")
            self.image.setAlignment(Qt.AlignCenter)
            self.image.setFont(QFont('Arial', 36))


    def saveFile(self):
        try:
            file_sname = QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))
            image = Image.open(self.image_name)
            print(self.image_name)
            print(file_sname)
            image.save(file_sname[0])
        except:
            self.image.setText("Bir Hata Oluştu...\nTekrar Deneyiniz.")
            self.image.setAlignment(Qt.AlignCenter)
            self.image.setFont(QFont('Arial', 36))

    def convert_image(self):
        try:
            deger = self.inputConvert.displayText()
            image1 = Image.open(self.image_name)
            image1.convert(mode=deger).save("sil.jpg")
            self.image_name = "sil.jpg"
            self.image.setPixmap(QtGui.QPixmap("sil.jpg"))
        except:
            self.image.setText("Bir Hata Oluştu...\nTekrar Deneyiniz.")
            self.image.setAlignment(Qt.AlignCenter)
            self.image.setFont(QFont('Arial', 36))

    def rotate_images(self):
        try:
            deger = int(self.inputRotate.displayText())
            image1 = Image.open(self.image_name)
            image1.rotate(deger).save("sil.jpg")
            self.image_name = "sil.jpg"
            self.image.setPixmap(QtGui.QPixmap("sil.jpg"))
        except:
            self.image.setText("Bir Hata Oluştu...\nTekrar Deneyiniz.")
            self.image.setAlignment(Qt.AlignCenter)
            self.image.setFont(QFont('Arial', 36))

    def filter_images(self):
        try:
            deger = int(self.inputFilter.displayText())
            image1 = Image.open(self.image_name)
            image1.filter(ImageFilter.GaussianBlur(deger)).save("sil.jpg")
            self.image_name = "sil.jpg"
            self.image.setPixmap(QtGui.QPixmap("sil.jpg"))
        except:
            self.image.setText("Bir Hata Oluştu...\nTekrar Deneyiniz.")
            self.image.setAlignment(Qt.AlignCenter)
            self.image.setFont(QFont('Arial', 36))

    def resize_images(self):
        try:
            deger1 = int(self.inputResize_1.displayText())
            deger2 = int(self.inputResize_2.displayText())
            degistir = (deger1, deger2)
            image1 = Image.open(self.image_name)
            image1.thumbnail(degistir)
            image1.save("sil.jpg")
            self.image_name = "sil.jpg"
            self.image.setPixmap(QtGui.QPixmap("sil.jpg"))
        except:
            self.image.setText("Bir Hata Oluştu...\nTekrar Deneyiniz.")
            self.image.setAlignment(Qt.AlignCenter)
            self.image.setFont(QFont('Arial', 36))

    def crop_images(self):
        try:
            deger1 = int(self.inputCrop_1.displayText())
            deger2 = int(self.inputCrop_2.displayText())
            deger3 = int(self.inputCrop_3.displayText())
            deger4 = int(self.inputCrop_4.displayText())
            area = (deger1, deger2, deger3, deger4)
            image1 = Image.open(self.image_name)
            image1.crop(area).save("sil.jpg")
            self.image_name = "sil.jpg"
            self.image.setPixmap(QtGui.QPixmap("sil.jpg"))
        except:
            self.image.setText("Bir Hata Oluştu...\nTekrar Deneyiniz.")
            self.image.setAlignment(Qt.AlignCenter)
            self.image.setFont(QFont('Arial', 36))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

