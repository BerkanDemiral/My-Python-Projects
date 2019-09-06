from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os


class Program(QDialog):
    def __init__(self):

        super().__init__()

        self.init_ui()



    def init_ui(self):

        self.islem = QLabel("")
        self.sayi1 = QLineEdit()
        self.sayi2 = QLineEdit()

        self.sonuc = QLineEdit()
        self.buton = QPushButton("Hesapla")


        vertical1 = QVBoxLayout()
        self.toplama = QRadioButton("Toplama")
        self.cikarma = QRadioButton("Çıkarma")
        self.carpma = QRadioButton("Çarpma")
        self.bolme = QRadioButton("Bölme")



        vertical1.addStretch()
        vertical1.addWidget(self.toplama)
        vertical1.addWidget(self.cikarma)
        vertical1.addWidget(self.carpma)
        vertical1.addWidget(self.bolme)
        vertical1.addStretch()

        horiontal = QHBoxLayout()
        horiontal.addWidget(self.sayi1)
        horiontal.addWidget(self.islem)
        horiontal.addWidget(self.sayi2)
        horiontal.addWidget(self.buton)
        horiontal.addWidget(self.sonuc)

        horiontal2 = QHBoxLayout()
        horiontal2.addLayout(vertical1)

        horiontal2.addLayout(horiontal)

        self.setLayout(horiontal2)

        self.buton.clicked.connect(lambda : self.hesaplama(self.toplama.isChecked(), self.cikarma.isChecked(), self.carpma.isChecked(), self.bolme.isChecked(),self.sayi1,self.sayi2,self.islem))

        if self.sayi1.text() == None:
            self.sonuc.setText('<font color="red" > Lütfen sayi1 Giriniz </font')
            self.sayi1.setFocus()
        elif self.sayi2.text() == None:
            self.sonuc.setText('<font color="red" > Lütfen sayi2 Giriniz </font')
            self.sayi2.setFocus()
        else:
            pass

        self.show()

    def hesaplama(self,toplama,cikarma,carpma,bolme,sayi1,sayi2,islem):
        intsayi1 = float(sayi1.text())
        intsayi2 = float(sayi2.text())


        if toplama:
            islem.setText("+")
            self.sonuc.setText(str(intsayi1+intsayi2))
        if cikarma:
            islem.setText("-")
            self.sonuc.setText(str(intsayi1 - intsayi2))

        if carpma:
            islem.setText("*")
            self.sonuc.setText(str(intsayi1 * intsayi2))
        if bolme:
            islem.setText("/")
            self.sonuc.setText(str(intsayi1 / intsayi2))



app = QApplication(sys.argv)
program = Program()
program.setGeometry(100, 100, 500, 270)
program.setWindowTitle("Basit Hesap Makinesi")
sys.exit(app.exec_())