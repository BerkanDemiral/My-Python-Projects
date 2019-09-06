from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
from bs4 import BeautifulSoup
import sys
import os

class Program(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        url = "https://www.imdb.com/chart/top"

        response = requests.get(url)  # ********* print(response) yaparsak url'nin alınıp alınmadı kontrolü. 200 verirse çektik.


        html_icerigi = response.content

        soup = BeautifulSoup(html_icerigi,"html.parser")


        self.filmadi = soup.find_all("td",{"class":"titleColumn"}) # *** clası lister-item-header olan tüm td'leri al.
        self.raiting = soup.find_all("td",{"class":"ratingColumn imdbRating"})

        self.filmler = QComboBox()

        for ad, reyting in zip(self.filmadi,self.raiting):
            ad = ad.text
            reyting = reyting.text

            ad = ad.strip() # *** html bloklarındaki gereksiz boşlukların yok edilmesini söylüyoruz. // virgül yokedilecekse strip(",") derdik.
            ad = ad.replace("\n","") # *** \n leri boşluğa çevirmesini söyledik.

            reyting = reyting.strip()
            reyting = reyting.replace("\n","")



            file = open("dosya.txt", "a")  # a ibaresi dosya yoksa oluşturur. Varsa içine yazma işlemi sağlar.
            file.write("{}   {}".format(ad,reyting))
            file.write("\n")
            self.filmler.addItem("{}  {}".format(ad,reyting))



        horizontal_1 = QHBoxLayout()
        self.baslik = QLabel('<font color ="orange" size = "8"> <strong> IMDB VERİ ÇEKME </strong> </font>')
        self.buton = QPushButton('<<Favorilerime Ekle>>')

        self.buton2 = QPushButton('<<Favorilerimi Kaydet>>')
        self.buton.clicked.connect(self.baglanti)
        self.buton2.clicked.connect(self.Kaydet)

        self.textedit = QTextEdit()

        horizontal_1.addStretch()
        horizontal_1.addWidget(self.baslik)
        horizontal_1.addStretch()

        horizontal_2 = QHBoxLayout()
        horizontal_2.addStretch()
        horizontal_2.addWidget(self.filmler)
        horizontal_2.addStretch()

        horizontal_3 = QHBoxLayout()
        horizontal_3.addStretch()
        horizontal_3.addWidget(self.textedit)
        horizontal_3.addStretch()

        horizontal_4 = QHBoxLayout()
        horizontal_4.addStretch()
        horizontal_4.addWidget(self.buton)
        horizontal_4.addStretch()


        horizontal_5 = QHBoxLayout()
        horizontal_5.addStretch()
        horizontal_5.addWidget(self.buton2)
        horizontal_5.addStretch()

        vertical = QVBoxLayout()


        vertical.addLayout(horizontal_1)
        vertical.addStretch()
        vertical.addLayout(horizontal_2)

        vertical.addLayout(horizontal_4) # ****** Horizontalleri fazla yapmamdaki amaç, daha ortada bir buton ve yapı sağlamak.
        vertical.addLayout(horizontal_3)
        vertical.addLayout(horizontal_5)

        self.setLayout(vertical)

        self.show()

    def baglanti(self):
        comboBox = self.filmler.currentText()

        self.textedit.append(comboBox)


    def Kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, "Dosya Kaydet", os.getenv("HOME"))

        with open(dosya_ismi[0], "w") as file:
            file.write(self.textedit.toPlainText())



app = QApplication(sys.argv)
program = Program()
program.setGeometry(100, 100, 550, 340)
program.setWindowTitle("IMDB Veri Çekme İşlemleri")
sys.exit(app.exec_())