# Bu program tek bir kullanıcıya mail gönderebiliyor, düzeltilmesi gerek

# maillerin yazıldığı alanlar Qtextedit ile oluşturuldu daha uygun bir alan seçilmeli.
#
# cc ve bcc boş geçilemiyor

from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

class Ui_SendMail(object):
    def setupUi(self, SendMail):
        SendMail.setObjectName("SendMail")
        SendMail.resize(658, 449)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(SendMail)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 661, 454))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.mainWindow = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.mainWindow.setContentsMargins(10, 10, 10, 10)
        self.mainWindow.setObjectName("mainWindow")

        self.grup1_dis = QtWidgets.QHBoxLayout()
        self.grup1_dis.setContentsMargins(10, 10, 10, 10)
        self.grup1_dis.setObjectName("grup1_dis")

        self.grup1_label = QtWidgets.QVBoxLayout()
        self.grup1_label.setObjectName("grup1_label")

        self.to_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.to_label.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.to_label.setFont(font)
        self.to_label.setObjectName("to_label")
        self.grup1_label.addWidget(self.to_label)

        self.cc_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.cc_label.setMinimumSize(QtCore.QSize(25, 25))
        self.cc_label.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cc_label.setFont(font)
        self.cc_label.setObjectName("cc_label")
        self.grup1_label.addWidget(self.cc_label)

        self.bcc_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.bcc_label.setMinimumSize(QtCore.QSize(25, 25))
        self.bcc_label.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bcc_label.setFont(font)
        self.bcc_label.setObjectName("bcc_label")
        self.grup1_label.addWidget(self.bcc_label)

        self.subject_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.subject_label.setMinimumSize(QtCore.QSize(50, 25))
        self.subject_label.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subject_label.setFont(font)
        self.subject_label.setObjectName("subject_label")
        self.grup1_label.addWidget(self.subject_label)

        self.grup1_dis.addLayout(self.grup1_label)

        self.grup1_textbox = QtWidgets.QVBoxLayout()
        self.grup1_textbox.setContentsMargins(10, 10, 10, 10)
        self.grup1_textbox.setObjectName("grup1_textbox")

        self.to_text = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.to_text.setMaximumSize(QtCore.QSize(1000, 25))
        self.to_text.setBaseSize(QtCore.QSize(0, 10))
        self.to_text.setObjectName("to_text")
        self.grup1_textbox.addWidget(self.to_text)

        self.cc_text = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.cc_text.setMaximumSize(QtCore.QSize(1000, 25))
        self.cc_text.setObjectName("cc_text")
        self.grup1_textbox.addWidget(self.cc_text)

        self.bcc_text = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.bcc_text.setMaximumSize(QtCore.QSize(1000, 25))
        self.bcc_text.setObjectName("bcc_text")
        self.grup1_textbox.addWidget(self.bcc_text)

        self.subject_text = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.subject_text.setMaximumSize(QtCore.QSize(1000, 25))
        self.subject_text.setObjectName("subject_text")
        self.grup1_textbox.addWidget(self.subject_text)

        self.grup1_dis.addLayout(self.grup1_textbox)
        self.mainWindow.addLayout(self.grup1_dis)
        
        self.grup2 = QtWidgets.QHBoxLayout()
        self.grup2.setContentsMargins(10, 10, 10, 10)
        self.grup2.setSpacing(10)
        self.grup2.setObjectName("grup2")

        self.message_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)

        self.message_label.setFont(font)
        self.message_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.message_label.setObjectName("message_label")
        self.grup2.addWidget(self.message_label)

        self.message_text = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.message_text.setMinimumSize(QtCore.QSize(100, 250))
        self.message_text.setBaseSize(QtCore.QSize(0, 0))
        self.message_text.setTabStopWidth(80)
        self.message_text.setObjectName("message_text")
        self.grup2.addWidget(self.message_text)

        self.mainWindow.addLayout(self.grup2)

        self.grup3 = QtWidgets.QHBoxLayout()
        self.grup3.setSpacing(10)
        self.grup3.setObjectName("grup3")

        self.temizle = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.temizle.setObjectName("temizle")
        self.grup3.addWidget(self.temizle)
        self.temizle.clicked.connect(self.clear_file)

        self.gonder = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.gonder.setObjectName("gonder")
        self.grup3.addWidget(self.gonder)
        self.gonder.clicked.connect(self.send_mail)

        self.cikis = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.cikis.setObjectName("cikis")
        self.grup3.addWidget(self.cikis)
        self.cikis.clicked.connect(self.exit_file)

        self.mainWindow.addLayout(self.grup3)

        self.retranslateUi(SendMail)
        QtCore.QMetaObject.connectSlotsByName(SendMail)

    def clear_file(self):
        self.message_text.clear()

    def exit_file(self):
        QtWidgets.qApp.quit()

    def send_mail(self):


        mesaj = MIMEMultipart()

        mesaj["From"] = "kmlmndc@gmail.com"

        mesaj["To"] = self.to_text.toPlainText()

        mesaj["CC"] = self.cc_text.toPlainText()

        mesaj["BCC"] = self.bcc_text.toPlainText()

        mesaj["Subject"] = self.subject_text.toPlainText()

        metin = self.message_text.toPlainText()

        mesaj_govdesi = MIMEText(metin, "plain")

        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)

            mail.ehlo()

            mail.starttls()

            mail.login("kmlmndc", "Kmlm.1299")

            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            mail.sendmail(mesaj["From"], mesaj["CC"], mesaj.as_string())
            mail.sendmail(mesaj["From"], mesaj["BCC"], mesaj.as_string())

            print("Gönderildi")

            mail.close()

        except:
            sys.stderr.write("Bir sorun oluştu")
            sys.stderr.flush()



    def retranslateUi(self, SendMail):
        _translate = QtCore.QCoreApplication.translate
        SendMail.setWindowTitle(_translate("SendMail", "Send Mail"))
        self.to_label.setText(_translate("SendMail", "To "))
        self.cc_label.setText(_translate("SendMail", "Cc"))
        self.bcc_label.setText(_translate("SendMail", "Bcc"))
        self.subject_label.setText(_translate("SendMail", "Konu"))
        self.message_label.setText(_translate("SendMail", "Mesaj"))
        self.temizle.setText(_translate("SendMail", "Temizle"))
        self.gonder.setText(_translate("SendMail", "Gönder"))
        self.cikis.setText(_translate("SendMail", "Çıkış"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SendMail = QtWidgets.QWidget()
    ui = Ui_SendMail()
    ui.setupUi(SendMail)
    SendMail.show()
    sys.exit(app.exec_())

