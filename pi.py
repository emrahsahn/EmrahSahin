# Herhangi bir hazır metot kullanmadan Pi sayısı programı
# E.Sahin

tarih = input("Lütfen doğum tarihinizi 'GÜN/AY'(14/03) şeklinde giriniz: ").split("/")
# print(tarih)


metin = ""
for i in tarih:
    metin += i
uzunluk = len(metin)
print(metin)

pi = open("pi.txt","r")
yeni_metin = ""
for i in pi:
    yeni_metin +=str(i)
uzunluk1 = len(yeni_metin)

def sayi_bulma():
    for i in range(uzunluk1):
        if yeni_metin[i:i + uzunluk] == metin:
            print(f'{metin} tarihi sayıların içinde bulundu ve indeksi {i}')
            x = 0
            yeni_metin2 = ""
            while x - 3 <= i:
                yeni_metin2 += yeni_metin[x]
                x += 1
            print(yeni_metin2)
            break
        else:
            # print(f'{metin} tarihi sayıların içinde bulunamadı.')
            pass


sayi_bulma()
