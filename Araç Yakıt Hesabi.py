# My-Python-Projects
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Program(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.grid = QGridLayout()
        self.grid.addWidget(QLabel("Gideceğiniz Yol (KM): "),0,0)
        self.gidilenyol  = QLineEdit()
        self.gidilenyol.setInputMask("0000000000") # 10 basamaklı sayı olmalı(max),,,
        self.grid.addWidget(self.gidilenyol,0,1)

        self.grid.addWidget(QLabel("Yakıtın Litre Fiyatı: "),1,0)
        self.yakitfiyat = QLineEdit()
        self.yakitfiyat.setInputMask("0.00")
        self.grid.addWidget(self.yakitfiyat,1,1)

        self.grid.addWidget(QLabel("100 Km' de Tüketilen Yakıt: "),2,0)
        self.yakittuketim = QLineEdit()
        self.yakittuketim.setInputMask("00.0")
        self.grid.addWidget(self.yakittuketim,2,1)

        self.grid.addWidget(QLabel("Toplam Tutar: "),3,0)
        self.tutar = QLabel("<i> KM Giriniz </i>")
        self.grid.addWidget(self.tutar,3,1)

        self.hesaplaDugme = QPushButton("Hesapla")
        self.hesaplaDugme.clicked.connect(self.hesaplama)
        self.grid.addWidget(self.hesaplaDugme,4,0,2,2)

        self.setLayout(self.grid)
        self.setWindowTitle("Yakıt Hesaplayıcısı")

        self.show()
    def hesaplama(self):
        yol = 0
        try: yol=int(self.gidilenyol.text())
        except: pass
        fiyat = 0
        try: fiyat = float(self.yakitfiyat.text())
        except: pass
        tuketim = 0
        try: tuketim = float(self.yakittuketim.text())
        except: pass

        if not yol:
            self.tutar.setText('<font color = "red"> <i> KM Giriniz </i> </font>')
            self.gidilenyol.setFocus()
        elif not fiyat:
            self.tutar.setText('<font color = "red" > <i> Fiyat Giriniz </i> </font>')
            self.yakitfiyat.setFocus()
        elif not tuketim:
            self.tutar.setText('<font color = "red" > <i> Tüketim Giriniz </i> </font>')
            self.yakittuketim.setFocus()
        else:
            tutar = fiyat*(yol*tuketim)/100
            self.tutar.setText('<font color = "blue" > <b> %0.2f </b> TL </font>' % tutar)

app = QApplication(sys.argv)
program = Program()
program.setGeometry(100,100,500,300)
sys.exit(app.exec_())
