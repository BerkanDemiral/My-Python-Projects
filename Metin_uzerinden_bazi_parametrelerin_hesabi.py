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
        grid = QGridLayout()
        self.yazi = QTextEdit()
        grid.addWidget(self.yazi,0,0,1,3)

        self.buton = QPushButton("İşlemi Gerçekleştir.")

        grid.addWidget(self.buton,1,1)
        self.buton.clicked.connect(self.butonislem)

        self.buton2 = QPushButton("Dosyadan Seç")
        self.buton2.clicked.connect(self.dosyasec)
        grid.addWidget(self.buton2,1,0)


        self.unlulabel = QLabel("Ünlü Harf Sayısı: ")
        grid.addWidget(self.unlulabel,2,0)
        self.unlusayi = QLineEdit()
        grid.addWidget(self.unlusayi,2,1)

        self.unsuzlabel = QLabel("Ünsüz Harf Sayısı: ")
        grid.addWidget(self.unsuzlabel,3,0)
        self.unsuzsayi = QLineEdit()
        grid.addWidget(self.unsuzsayi,3,1)

        self.kelimesayisi = QLabel("Toplam Kelime Sayisi: ")
        grid.addWidget(self.kelimesayisi,4,0)
        self.kelimesayinline = QLineEdit()
        grid.addWidget(self.kelimesayinline,4,1)

        self.harfsayisi = QLabel("Toplam Harf Sayisi: ")
        grid.addWidget(self.harfsayisi, 5, 0)
        self.harfsayiinline = QLineEdit()
        grid.addWidget(self.harfsayiinline, 5,1)


        self.harffrekans = QLabel("En Çok Kullanılan Harf Frekansı: ")
        grid.addWidget(self.harffrekans,6,0)
        self.frekansharf = QLineEdit()
        grid.addWidget(self.frekansharf,6,1)




        self.setLayout(grid)

        self.show()

    def butonislem(self):
        yazi = self.yazi.toPlainText() # ********* QTextEditteki yazıyı kullanmak için toPlainText() Kullan ***************
        list = yazi.split()
        self.kelimesayinline.setText(str(len(list))) # ********** QLineEdit lere bir şey yazarken str olarak yazdırmayı unutma. **************
        self.harfsayiinline.setText(str(len(yazi)))

        unluler = ["a","e","u","ü","ı","i","o","ö"]
        output = 0
        outputt = 0
        for x in yazi:
            if x in unluler:
                output+=1
            else:
                outputt+=1
        self.unlusayi.setText(str(output)) # ********* unlu harflerin sayısı burada yazdırılıyor
        self.unsuzsayi.setText(str(outputt)) # ********** unsuz harflerin sayısı burada yazdırılıyor.

        a_sayi = yazi.count("a")
        b_sayi = yazi.count("b")
        c_sayi = yazi.count("c")
        d_sayi = yazi.count("d")
        e_sayi = yazi.count("e")
        f_sayi = yazi.count("f")
        g_sayi = yazi.count("g")
        h_sayi = yazi.count("h")
        ı_sayi = yazi.count("ı")
        i_sayi = yazi.count("i")
        j_sayi = yazi.count("j")
        k_sayi = yazi.count("k")
        l_sayi = yazi.count("l")
        m_sayi = yazi.count("m")
        n_sayi = yazi.count("n")
        o_sayi = yazi.count("o")
        ö_sayi = yazi.count("ö")
        p_sayi = yazi.count("p")
        r_sayi = yazi.count("r")
        s_sayi = yazi.count("s")
        ş_sayi = yazi.count("ş")
        t_sayi = yazi.count("t")
        u_sayi = yazi.count("u")
        ü_sayi = yazi.count("ü")
        v_sayi = yazi.count("v")
        y_sayi = yazi.count("y")
        z_sayi = yazi.count("z")

        harfcount = [a_sayi,b_sayi,c_sayi,d_sayi,e_sayi,f_sayi,g_sayi,h_sayi,ı_sayi,i_sayi,j_sayi,k_sayi,l_sayi,m_sayi,n_sayi,o_sayi,ö_sayi,p_sayi,
                     r_sayi,s_sayi,ş_sayi,t_sayi,u_sayi,ü_sayi,v_sayi,y_sayi,z_sayi]
        self.frekansharf.setText(str(max(harfcount)))







    def dosyasec(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç",os.getenv("HOME"))  # dosya ekranı masaüstünden açılsın.

        with open(dosya_ismi[0], "r" , encoding="utf-8") as file:  # tıklanan dosyanın 0.indexi aslında dosyanın içeriğidir.
            self.yazi.setText(file.read())  # file.read() dosyanın içini aynı şekilde oku demektir.




app = QApplication(sys.argv)
program = Program()
program.setGeometry(100, 100, 570, 370)
program.setWindowTitle("Yazi Hesaplaması")
sys.exit(app.exec_())