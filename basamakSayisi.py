# 1- basamak sayısını bulma programı

title ="Basamak sayısını bulan program"
print("-"*len(title),title,"-"*len(title),sep="\n",end="\n\n")

try:
    number = input("Bir sayı giriniz: ")
    #sayi = int(input("Bir tam sayı giriniz :")) şeklinde olursa
    #except kısmında sayi değişkeni tanımlanmadı deyip hata veriyor.
    #Hata alınmadan önce sayi değişkeni oluşturulyor.
    #Ardından dönüşüm yapılıyor. Dönüşümde hata olunca bu sefer sayi değişkeni önceden tanımlandığı
    #için except kısmında sıkıntı çıkmıyor.

    if "." in number:
        number = float(number)
        place = []
        for i in str(number):
            place.append(i)

        if number < 0:
            print(number, " girilen sayı negatif bir ondalık sayıdır", place," ve basamak asyısı =>", len(place) - 2, end="\n\n")
        else:
            print(number, " girilen sayı poziti bir ondalık sayıdır", place,"ve basamak sayısı =>", len(place) - 1, end="\n\n")

    else:
        number = int(number)
        place = []
        for i in str(number):
            place.append(i)

        if number < 0:
            print(number," girilen sayı negatif bir tam sayıdır ve basamak asyısı =>",len(place)-1, end="\n\n")
        else:
            print(number, " girilen sayı pozitif bir tam sayıdır ve basamak sayısı =>",len(place), end="\n\n")

except:
    print("\"{}\"bir sayı değil!".format(number))