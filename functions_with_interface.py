# program that runs certain programs

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, \
    QLineEdit, QTextEdit, QDialog, QMessageBox, QInputDialog
from functools import reduce


class K_Kucuk(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("K-Küçük İşlemi")
        self.setGeometry(100, 100, 400, 300)

        k_kucuk_label = QLabel("K. Küçük İndeks Giriniz:")
        self.k_kucuk_index_entry = QLineEdit()
        k_kucuk_list_label = QLabel("Listeyi '2,3,4,5' Şeklinde Giriniz: ")
        self.k_kucuk_list_entry = QLineEdit()
        k_kucuk_button = QPushButton("K-Küçük Hesapla")
        k_kucuk_button.clicked.connect(self.k_kucuk_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(k_kucuk_label)
        layout.addWidget(self.k_kucuk_index_entry)
        layout.addWidget(k_kucuk_list_label)
        layout.addWidget(self.k_kucuk_list_entry)
        layout.addWidget(k_kucuk_button)
        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def k_kucuk_calistir(self):
        try:
            index = self.k_kucuk_index_entry.text()
            liste = self.k_kucuk_list_entry.text().split(',')
            liste = [int(x) for x in liste]
            sonuc = self.k_kucuk(index, liste)
            self.sonuc_text.setPlainText(f"K-Küçük Sonucu: {sonuc}")
        except ValueError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText("Hatalı Giriş! Lütfen doğru bir giriş yapın.")
            error_box.exec_()

    def k_kucuk(self, index, liste):
        index = int(index)
        sorted_list = sorted(liste)
        if 0 <= len(liste):
            if index <= -1:
                k_kucuk_sonuc = sorted_list[index]
                return k_kucuk_sonuc
            else:
                k_kucuk_sonuc = sorted_list[index-1]
                return k_kucuk_sonuc



class En_Yakin_Cift(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("En Yakın Çift İşlemi")
        self.setGeometry(100, 100, 400, 300)

        en_yakin_cift_label = QLabel("En Yakını Bulunacak Sayıyı Giriniz: ")
        self.en_yakin_number_entry = QLineEdit()
        en_yakin_cift_list_label = QLabel("Listeyi '2,3,4,5' Şeklinde Giriniz: ")
        self.en_yakin_list_entry = QLineEdit()
        en_yakin_button = QPushButton("En Yakın Çifti Göster")
        en_yakin_button.clicked.connect(self.en_yakin_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(en_yakin_cift_label)
        layout.addWidget(self.en_yakin_number_entry)
        layout.addWidget(en_yakin_cift_list_label)
        layout.addWidget(self.en_yakin_list_entry)
        layout.addWidget(en_yakin_button)
        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def en_yakin_calistir(self):
        try:
            number = self.en_yakin_number_entry.text()
            liste = self.en_yakin_list_entry.text().split(",")
            liste = [int(x) for x in liste]
            result = self.en_yakin_cift(number, liste)
            self.sonuc_text.setPlainText(f"En Yakın Sonuc: {result}")
        except ValueError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText("Hatalı Giriş! Lütfen doğru bir giriş yapın.")
            error_box.exec_()

    def en_yakin_cift(self, intt, list):

        list = sorted(list)  # listeyi sıraladık
        intt = int(intt)

        en_kucuk_fark = abs(intt - (int(list[0]) + int(list[1])))  # ilk iki elemanı çift olarak başlatıyoruz

        for i in range(len(list) - 1):  # tüm olası çiftleri kontrol ediyoruz
            en_yakin_toplam = 0
            for x in range(i + 1, len(list)):
                en_yakin_toplam = list[i] + list[x]
                fark = abs(intt - en_yakin_toplam)

                if fark < en_kucuk_fark:
                    en_yakin_toplam_cifti = f"{list[i]} {list[x]}"
                    en_kucuk_fark = fark
        return en_yakin_toplam_cifti



class Tekrar_Eden_Eleman(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bir Listenin Tekrar Eden Elemanlarını Bulma")
        self.setGeometry(100, 100, 400, 300)

        tekrar_eden_eleman_liste_label = QLabel("Listeyi 1,2,3,4,5 şeklinde Giriniz:".title())
        self.tekrar_eden_eleman_liste_entry = QLineEdit()
        tekrar_eden_button = QPushButton("Tekrar Eden Elemanları Gör ")
        tekrar_eden_button.clicked.connect(self.tekrar_eden_eleman_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(tekrar_eden_eleman_liste_label)
        layout.addWidget(self.tekrar_eden_eleman_liste_entry)
        layout.addWidget(tekrar_eden_button)
        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def tekrar_eden_eleman_calistir(self):
        try:
            liste = self.tekrar_eden_eleman_liste_entry.text().split(",")
            liste = [int(x) for x in liste]
            result = self.tekrar_eden_elemanlar(liste)
            self.sonuc_text.setPlainText(f"En Çok Tekrar Eden Elemanlar: {result}")
        except ValueError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText("Hatalı Giriş! Lütfen doğru bir liste girin.")
            error_box.exec_()

    def tekrar_eden_elemanlar(self, liste):

        tekrar_eden_elemanlar_sonuc = [int(i) for i in liste if liste.count(i) > 1]
        # öncelikle list compherasion ile tekrar eden sayıları bulduk
        tekrar_eden_elemanlar_sonuc = list(set(tekrar_eden_elemanlar_sonuc))
        # sonra tekrar eden sayıların tekrar sayılarını göstermeden sadece hangilerini tekrar ettiğini
        # göstermek için set sınıfının içine aldık
        return tekrar_eden_elemanlar_sonuc



class Matris_Carpimi(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matris Çarpımı")
        self.setGeometry(100, 100, 400, 300)

        matris1_rows = QLabel("İlk matrisin satır sayısını girin: ".title())
        self.matris1_rows_entry = QLineEdit()
        matris1_columns = QLabel("İlk matrisin sütun sayısını girin: ".title())
        self.matris1_columns_entry = QLineEdit()
        matris1_liste = QLabel("İlk Matrisi Boşluklarla şu şekilde '2 3 4 5 6 7' giriniz: ".title())
        self.matris1_liste_entry = QLineEdit()

        matris2_rows = QLabel("İkinci matrisin satır sayısını girin: ".title())
        self.matris2_rows_entry = QLineEdit()
        matris2_columns = QLabel("İkinci matrisin sütun sayısını girin: ".title())
        self.matris2_columns_entry = QLineEdit()
        matris2_liste = QLabel("İkinci matrisi boşluklarla şu şekilde '2 3 4 5 6 7' giriniz:".title())
        self.matris2_liste_entry = QLineEdit()
        matris_button = QPushButton("Matris Çarpımları Gör")
        matris_button.clicked.connect(self.matris_carpimi_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(matris1_rows)
        layout.addWidget(self.matris1_rows_entry)
        layout.addWidget(matris1_columns)
        layout.addWidget(self.matris1_columns_entry)
        layout.addWidget(matris1_liste)
        layout.addWidget(self.matris1_liste_entry)

        layout.addWidget(matris2_rows)
        layout.addWidget(self.matris2_rows_entry)
        layout.addWidget(matris2_columns)
        layout.addWidget(self.matris2_columns_entry)
        layout.addWidget(matris2_liste)
        layout.addWidget(self.matris2_liste_entry)
        layout.addWidget(matris_button)

        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def matris_carpimi_calistir(self):
        try:

            girdi1 = list(map(int, self.matris1_liste_entry.text().split()))
            girdi2 = list(map(int, self.matris2_liste_entry.text().split()))
            row1 = int(self.matris2_rows_entry.text())
            column1 = int(self.matris1_columns_entry.text())
            row2 = int(self.matris2_rows_entry.text())
            column2 = int(self.matris2_columns_entry.text())

            if column1 != row2:
                self.sonuc_text.setPlainText("Matris Çarpımı için matrislerin boyutları uyumsuz.")
                return

            # matris1 = []
            # for i in range(0, len(girdi1), column1):
            #     matris1.append([girdi1[i:i+column1]])
            #
            # matris2 = []
            # for i in range(0, len(girdi2), column2):
            #     matris2.append(girdi2[i:i+column2])  bu satırlarla olmadı nedenini bende bilmiyorum ben de lish comprehsion şeklinde denedim

            matris1 = [girdi1[i:i + column1] for i in range(0, len(girdi1), column1)]
            matris2 = [girdi2[i:i + column2] for i in range(0, len(girdi2), column2)]

            result = self.matris_carpimi(matris1, matris2)
            self.sonuc_text.setPlainText(f"Matris Çarpımımın Sonucu: ")
            for i in result:
                self.sonuc_text.append(" ".join(map(str, i)))

        except ValueError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText("Hatalı Giriş! Lütfen doğru bir giriş yapın.")
            error_box.exec_()

    def matris_carpimi(self, matris1, matris2):

        result = [[sum(a * b for a, b in zip(matris1_satir, matris2_sutun)) for matris2_sutun in zip(*matris2)] for
                  matris1_satir in matris1]
        # bu satırı direk internetten aldım aldığım yerin linki ise burda
        # https://forum.yazbel.com/t/python-ile-matris-carpimi/15324/2

        matris_carpimi = [i for i in result]
        return matris_carpimi




class Text_Dosyasi_Kelime_Frekansi(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
        self.setGeometry(100, 100, 400, 300)

        kelime_frekans = QLabel("Lütfen dosya yolunu girin:".title())
        self.kelime_frekans_entry = QLineEdit()
        kelime_frekans_buton = QPushButton("Kelime Frekanslarını Gör")
        kelime_frekans_buton.clicked.connect(self.kelime_frekans_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(kelime_frekans)
        layout.addWidget(self.kelime_frekans_entry)
        layout.addWidget(kelime_frekans_buton)
        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def kelime_frekans_calistir(self):
        try:
            dosya_yolu = self.kelime_frekans_entry.text().strip()
            result = self.kelime_frekans(dosya_yolu)
            for kelime, sayi in result.items():
                self.sonuc_text.append(f"{kelime} = {sayi}")

        except Exception as err:
            # self.sonuc_text.setPlainText(f"Hata oluştu: {str(err)}")
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText(f"Hatalı Giriş! Hata oluştu: {str(err)}.Lütfen doğru bir giriş yapın.")
            error_box.exec_()

    def kelime_frekans(self, strr):
        with open(strr, "r", encoding="utf-8") as file:
            okunan_dosya = file.read().split()  # dosyamızı okuduk

        def sayac(sonuc, eleman):
            ''' Bir kelimenin frekansını hesaplamak için kullanılacak işlev tanımlanıyor.'''
            sonuc[eleman] = sonuc.get(eleman, 0) + 1
            # Her kelimenin frekansını artırmak için get() yöntemi kullanılıyor.
            return sonuc

        # Kelime frekansları, reduce() fonksiyonu kullanılarak hesaplanıyor.
        kelime_sayisi = dict(reduce(sayac, okunan_dosya, {}))

        return kelime_sayisi



class Liste_En_Kucuk_Deger(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liste İçinde En Küçük Değeri Bulma")
        self.setGeometry(100, 100, 400, 300)

        en_kucuk_liste_label = QLabel("Listeyi şu şekilde 1,2,3,4,5 Giriniz:".title())
        self.en_kucuk_liste_entry = QLineEdit()
        en_kucuk_liste_buton = QPushButton("Listedeki en küçük değeri gör".title())
        en_kucuk_liste_buton.clicked.connect(self.en_kucuk_liste_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(en_kucuk_liste_label)
        layout.addWidget(self.en_kucuk_liste_entry)
        layout.addWidget(en_kucuk_liste_buton)
        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def en_kucuk_liste_calistir(self):
        try:
            liste = self.en_kucuk_liste_entry.text().split(",")
            liste = [int(x) for x in liste]
            result = self.en_kucuk_deger(liste, len(liste))
            self.sonuc_text.setPlainText(f"En küçük değer {result}".title())

        except ValueError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText("Hatalı Giriş! Lütfen doğru bir liste girin.")
            error_box.exec_()

    def en_kucuk_deger(self, listt, liste_uzunluk):
        '''Kısmi bir bubble sort yapılmıştır'''
        # temel durum: dizi sadece bir elemanlı ise zaten sıralıdır
        if liste_uzunluk == 1:
            return listt[0]

        for i in range(liste_uzunluk - 1):
            if listt[i] > listt[i + 1]:
                listt[i], listt[i + 1] = listt[i + 1], listt[i]

        return self.en_kucuk_deger(listt, liste_uzunluk - 1)


class Karekok_Sinifi(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Karekök Fonksiyonu")
        self.setGeometry(100, 100, 400, 300)

        karekok_int = QLabel("Lütfen karekökü alınacak sayıyı giriniz: ".title())
        self.karekok_int_entry = QLineEdit()
        karekok_first_guess = QLabel("Lütfen karekök için tahmin değerinizi giriniz: ".title())
        self.karekok_guess_entry = QLineEdit()
        karekok_maximiter = QLabel("Varsayılan olarak 10 atanan bir değerdir.\nDeğiştirmek isterseniz"
                                   "değiştirin değiştirmek istemezseniz 10 olarak giriş yapınız: ".title())
        self.karekok_maximiter_entry = QLineEdit()
        karekok_button = QPushButton("Karekök Fonksiyonu Hesapla")
        karekok_button.clicked.connect(self.karekok_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(karekok_int)
        layout.addWidget(self.karekok_int_entry)
        layout.addWidget(karekok_first_guess)
        layout.addWidget(self.karekok_guess_entry)
        layout.addWidget(karekok_maximiter)
        layout.addWidget(self.karekok_maximiter_entry)
        layout.addWidget(karekok_button)
        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def karekok_calistir(self):
        try:
            first_input = int(self.karekok_int_entry.text())
            second_input = float(self.karekok_guess_entry.text())
            maxiter_input = int(self.karekok_maximiter_entry.text())
            tol_input= 10 ** (-10)
            result = self.karekok(first_input, second_input,tol_input,maxiter_input)
            self.sonuc_text.setPlainText(f"{result}")

        except ValueError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText("Hatalı Giriş! Lütfen doğru bir giriş yapın.")
            error_box.exec_()

    def karekok(self, N, x0, tol=10 ** (-10), maxiter=10, iteration=0):

        x0 = 0.5 * (x0 + (N / x0))  # yeni tahmin
        error = abs(x0 ** 2 - N)  # hata değerini bulma

        if error < tol:
            return x0
        if iteration >= maxiter:
            # self.sonuc_text.setPlainText(f"{iteration} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin")
            return f"{iteration} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin\n{x0}"

        return self.karekok(N, x0, tol, maxiter, iteration + 1)  # recursive çağrı


class En_Buyuk_Ortak_Bolen(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("En Büyük Ortak Bölen")
        self.setGeometry(100, 100, 400, 300)

        ebob_int = QLabel("Lütfen en büyük ortak böleni alınacak ilk sayıyı giriniz: ".title())
        self.ebob_int_entry = QLineEdit()
        ebob_int1 = QLabel("Lütfen en büyük ortak böleni alınacak ikinci sayıyı giriniz: ".title())
        self.ebob_int1_entry = QLineEdit()
        ebob_button = QPushButton("Girilen iki sayının ebobunu Hesapla".title())
        ebob_button.clicked.connect(self.eb_ortak_bolen_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(ebob_int)
        layout.addWidget(self.ebob_int_entry)
        layout.addWidget(ebob_int1)
        layout.addWidget(self.ebob_int1_entry)
        layout.addWidget(ebob_button)
        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def eb_ortak_bolen_calistir(self):
        try:
            first_input = int(self.ebob_int_entry.text())
            second_input = int(self.ebob_int1_entry.text())
            result = self.eb_ortak_bolen(first_input, second_input)
            self.sonuc_text.setPlainText(f"{result}")
        except ValueError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText("Hatalı Giriş! Lütfen doğru bir giriş yapın.")
            error_box.exec_()

    def eb_ortak_bolen(self, int1, int2):
        if int2 == 0:  # temel durum: girilen herhangi bir sayının 0 olması
            return int1
        elif int1 == 0:
            return int2
        elif int1 == int2:  # temel durum: girilen sayıların aynı olması
            return int1
        else:
            return self.eb_ortak_bolen(int2, int1 % int2)


class Asallik_Testi(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Karekök Fonksiyonu")
        self.setGeometry(100, 100, 400, 300)

        asal_number = QLabel("Lütfen asal olup olmadığını merak ettiğiniz sayıyı giriniz:".title())
        self.asal_number_entry = QLineEdit()
        asal_number_button = QPushButton("Asallık hesapla ".title())
        asal_number_button.clicked.connect(self.asal_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(asal_number)
        layout.addWidget(self.asal_number_entry)
        layout.addWidget(asal_number_button)
        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def asal_calistir(self):
        try:
            first_input = int(self.asal_number_entry.text())
            result = self.asal_veya_degil(first_input)
            self.sonuc_text.setPlainText(f"{result}")
        except ValueError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText("Hatalı Giriş! Lütfen doğru bir giriş yapın.")
            error_box.exec_()

    def asal_veya_degil(self, int, i=2):
        if int == 2:  # temel durum: girilen sayının 2 olması
            return True
        elif int % i == 0:
            return False
        elif i * i > int:  # bir sayının böleninin karesi kendisinden
            # büyükse ondan sonraya bakamya gerek kalmaz
            return True  # zaten kontrol edilmiş olur
        else:
            return self.asal_veya_degil(int, i + 1)


class Daha_Hizli_Fibonacci(QDialog):
    def __init__(self):
        super().__init__()

        self.liste = []

        self.setWindowTitle("Karekök Fonksiyonu")
        self.setGeometry(100, 100, 400, 400)

        hesaplanacak_terim = QLabel("Hesaplanacak fibonacci terimini giriniz: ".title())
        self.hesaplanacak_terim_entry = QLineEdit()
        baslangic_degeri = QLabel("Başlangıç Değerini giriniz: ".title())
        self.baslangic_degeri_entry = QLineEdit()
        ilk_terim = QLabel("İlk fibonacci terimi:".title())
        self.ilk_terim_entry = QLineEdit()
        ikinci_terim = QLabel("İkinci fibonacci terimi:".title())
        self.ikinci_terim_entry = QLineEdit()
        fibonacci_button = QPushButton("Fibonacci Değerlerini Hesapla".title())
        fibonacci_button.clicked.connect(self.hizlandirici_calistir)

        self.sonuc_text = QTextEdit()
        self.sonuc_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(hesaplanacak_terim)
        layout.addWidget(self.hesaplanacak_terim_entry)
        layout.addWidget(baslangic_degeri)
        layout.addWidget(self.baslangic_degeri_entry)
        layout.addWidget(ilk_terim)
        layout.addWidget(self.ilk_terim_entry)
        layout.addWidget(ikinci_terim)
        layout.addWidget(self.ikinci_terim_entry)
        layout.addWidget(fibonacci_button)
        layout.addWidget(self.sonuc_text)

        self.setLayout(layout)

    def hizlandirici_calistir(self):
        try:
            hesaplanacak_terim_girdi = int(self.hesaplanacak_terim_entry.text())
            baslangic_degeri_girdi = int(self.baslangic_degeri_entry.text())
            ilk_terim_girdi = int(self.ilk_terim_entry.text())
            ikinci_terim_girdi = int(self.ikinci_terim_entry.text())
            result = self.hizlandirici(hesaplanacak_terim_girdi, baslangic_degeri_girdi, ilk_terim_girdi,
                                       ikinci_terim_girdi)
            for i in self.liste:
                self.sonuc_text.append(i)
            self.sonuc_text.append(f"Fonksiyonun Sonucu:{result}")

        except ValueError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Hata")
            error_box.setText("Hatalı Giriş! Lütfen doğru bir giriş yapın.")
            error_box.exec_()

    def hizlandirici(self, n, k, fibk, fibk1):

        if k == 1:
            self.liste += [f"n,k,fibk,fibk1\n{n} {k} {fibk} {fibk1}"]

        if (n != k):
            k += 1

            fibk = fibk + fibk1
            fibk1 = fibk - fibk1
            self.liste.append(f"{n} {k} {fibk} {fibk1}")
            return self.hizlandirici(n, k, fibk, fibk1)
        else:
            return fibk


class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ödev1 Menü Arayüzü")
        self.setGeometry(100, 100, 400, 600)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(0, 0, 100, 100)

        self.text_edit.setPlainText("""
                                            CONSOLE MENU
        1. k’nıncı En Küçük Elemanı Bulma
        2. En Yakın Çifti Bulma
        3. Bir Listenin Tekrar Eden Elemanlarını Bulma
        4. Matris Çarpımı
        5. Bir Text Dosyasındaki Kelimelerin Frekansını Bulma
        6. Liste İçinde En Küçük Değeri Bulma
        7. Karekök Fonksiyonu
        8. En Büyük Ortak Bölen
        9. Asallık Testi
        10. Daha Hızlı Fibonacci Hesabı

        Aşağıdaki butonlarımıza tıklayarak istediğiniz fonksiyonu çalıştırıp işlemlerinizi yapabilirsiniz.

        """)

        self.text_edit.setReadOnly(True)

        k_kucuk_buton = QPushButton("k’nıncı En Küçük Elemanı Bulma")
        k_kucuk_buton.clicked.connect(self.open_k_kucuk_window)

        en_yakin_cift_buton = QPushButton("En Yakın Çifti Bulma")
        en_yakin_cift_buton.clicked.connect(self.open_en_yakin_cift_window)

        tekrar_eden_eleman_buton = QPushButton("Bir Listenin Tekrar Eden Elemanlarını Bulma")
        tekrar_eden_eleman_buton.clicked.connect(self.open_tekrar_eden_eleman_window)

        matris_carpimi_buton = QPushButton("Matris Çarpımı")
        matris_carpimi_buton.clicked.connect(self.open_matris_carpimi_window)

        kelime_frekans_buton = QPushButton("Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
        kelime_frekans_buton.clicked.connect(self.open_kelime_frekans_window)

        en_kucuk_deger_buton = QPushButton("Liste İçinde En Küçük Değeri Bulma")
        en_kucuk_deger_buton.clicked.connect(self.open_en_kucuk_deger_window)

        karekok_buton = QPushButton("Karekök Fonskiyon")
        karekok_buton.clicked.connect(self.open_karekok_func_window)

        ebob_buton = QPushButton("En Büyük Ortak Bölen")
        ebob_buton.clicked.connect(self.open_ebob_window)

        asal_buton = QPushButton("Asallık Testi")
        asal_buton.clicked.connect(self.open_asallik_window)

        fibonacci_buton = QPushButton("Daha Hızlı Fibonacci Hesabı")
        fibonacci_buton.clicked.connect(self.open_fibonacci_window)

        buton_quit = QPushButton("Çıkış")
        buton_quit.clicked.connect(self.quit)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(k_kucuk_buton)
        layout.addWidget(en_yakin_cift_buton)
        layout.addWidget(tekrar_eden_eleman_buton)
        layout.addWidget(matris_carpimi_buton)
        layout.addWidget(kelime_frekans_buton)
        layout.addWidget(en_kucuk_deger_buton)
        layout.addWidget(karekok_buton)
        layout.addWidget(ebob_buton)
        layout.addWidget(asal_buton)
        layout.addWidget(fibonacci_buton)
        layout.addWidget(buton_quit)

        self.setLayout(layout)

    def open_k_kucuk_window(self):
        second_window = K_Kucuk()
        second_window.exec_()

    def open_en_yakin_cift_window(self):
        third_window = En_Yakin_Cift()
        third_window.exec_()

    def open_tekrar_eden_eleman_window(self):
        fourth_window = Tekrar_Eden_Eleman()
        fourth_window.exec_()

    def open_matris_carpimi_window(self):
        fifth_window = Matris_Carpimi()
        fifth_window.exec_()

    def open_kelime_frekans_window(self):
        kelime_frekans = Text_Dosyasi_Kelime_Frekansi()
        kelime_frekans.exec_()

    def open_en_kucuk_deger_window(self):
        en_kucuk_deger = Liste_En_Kucuk_Deger()
        en_kucuk_deger.exec_()

    def open_karekok_func_window(self):
        karekok_func = Karekok_Sinifi()
        karekok_func.exec_()

    def open_ebob_window(self):
        ebob_func = En_Buyuk_Ortak_Bolen()
        ebob_func.exec_()

    def open_asallik_window(self):
        asallik_func = Asallik_Testi()
        asallik_func.exec_()

    def open_fibonacci_window(self):
        fibonacci_func = Daha_Hizli_Fibonacci()
        fibonacci_func.exec_()

    def quit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = FirstWindow()
    main_window.show()
    sys.exit(app.exec_())
