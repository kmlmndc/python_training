import sys
import requests

from PyQt5 import QtWidgets

url = "http://data.fixer.io/api/latest?access_key=711ea465c37dff1c876d6e893ab879e3"
response = requests.get(url)
jsonData = response.json()


class ExchangeProgram(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        print(1)

    def init_ui(self):



        self.text_area = QtWidgets.QLineEdit()
        self.btn_tlToUsd = QtWidgets.QPushButton("Dolara Çevir")
        self.btn_usdToTl = QtWidgets.QPushButton("Türk Lirasına Çevir")
        self.text_print = QtWidgets.QLabel()

        self.button_box = QtWidgets.QHBoxLayout()
        self.button_box.addWidget(self.btn_tlToUsd)
        self.button_box.addWidget(self.btn_usdToTl)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()
        v_box.addWidget(self.text_area)
        v_box.addLayout(self.button_box)
        v_box.addWidget(self.text_print)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.btn_tlToUsd.clicked.connect(self.toDollar)
        self.btn_usdToTl.clicked.connect(self.toLira)

        self.show()

    def toDollar(self):


        dollar = float(self.text_area.text()) / jsonData["rates"]["TRY"]

        self.text_print.setText(str(dollar))

    def toLira(self):
        dollar = float(self.text_area.text()) * jsonData["rates"]["TRY"]

        self.text_print.setText(str(dollar))


app = QtWidgets.QApplication(sys.argv)

exchangeProgram = ExchangeProgram()

sys.exit(app.exec_())
