# hesap makinesi programı

import time

title = "Bu bir örnek hesap makinesi uygulamasıdır."
entry = '''
(1) topla işlemi
(2) fark işlemi
(3) çarpım işlemi
(4) bölme işlemi
(5) karesini hesaplama işlemi
(6) kare kök hesaplama işlemi
Çıkış için bu rakamlardan farklı bir tuşa basın!
'''

writing = {
    "1": "Toplama-Toplanacak değerlerin ilkini girin:",
    "11": "Toplanacak değerlerin ikincisini girin:",
    "2": "Fark-Çıkarılacak değerlerin ilkini girin:",
    "22": "Çıkarılacak değerlerin ikincisini girin:",
    "3": "Çarpım-Çarpılacak değerlerin ilkini girin:",
    "33": "Çarpılacak değerlerin ikincisini girin:",
    "4": "Bölme-Bölünen değeri girin:",
    "44": "Bölen değeri girin:",
    "5": "Üs Alma-Üssü alınacak değeri girin:",
    "55": "Üs değerini girin:",
    "6": "Kare Kök Alm-Kökü alınacak değeri girin:",
    "66": "Kök derecesini girin:"
}

print(title, entry, sep="\n")

while True:

    choosing = input("Yapmak istediğiniz işlemin numarasını giriniz : ")

    try:
        if choosing in ["1", "2", "3", "4", "5", "6"]:
            number1 = int(input("{}".format(writing[choosing].split("-")[1])))
            if (choosing + choosing) in writing:
                number2 = float(input("{}".format(writing.get(choosing + choosing))))
            # get yerine [] kullansaydık islemislem olmadığında hata alırdık. Şimdi hata almayacağız
            # Sadece null değeri geri dönecek
    except:
        print("Bir tamsayı girilmedi. Tekrar deneyin!\n")
        continue

    if choosing == "1":
        result = number1 + number2
    elif choosing == "2":
        result = number1 - number2
    elif choosing == "3":
        result = number1 * number2
    elif choosing == "4":
        result = number1 / number2
    elif choosing == "5":
        result = number1 ** number2
    elif choosing == "6":
        result = number1 ** (1/number2)
    else:
        print("Kabul edilen bir işlem numarası girmediniz! Program kapatılıyor ")
        time.sleep(4)
        break

    print("{} işleminin sonucu olarak {} değeri bulunmuştur.\n".format(writing[choosing].split("-")[0], result))
"""
"""
# sayı tahmin oyunu
import random,time

class number_guessing_game():

    def __init__(self):
        self.explains()

    def explains(self):
        print("0-100 arasında bir sayıyı seçiniz.\n"
              "Oyundan çıkmak için '-1'e bas")

    def generate_number(self):
        return random.randint(0,101)

    def guessing(self):
        number = self.generate_number()
        guess_count = 0
        nmb_of_rmnng_forecast = 10 # number of remaining forecast


        while True:
            try:
                inputt = int(input("Tahmininizi giriniz: "))
                if inputt == -1 or "":
                    break
                guess_count += 1
                nmb_of_rmnng_forecast -= 1

                if number == inputt:
                    print("Tebrikler {} sayısını {}. tahmininizde buldunuz. {} tahmininiz kaldı"
                          "".format(number, guess_count, nmb_of_rmnng_forecast))
                    print("\nYeni bir sayı tuttum. Hadi Tahmin Et!")
                    number = self.generate_number()
                    guess_count = 0
                    nmb_of_rmnng_forecast = 10
                    inpt = input("Devam etmek istiyorsanız 'E' tıklayın yoksa 'H' ye tıklayın: ").lower()
                    if inpt == 'e':
                        continue
                    else:
                        break

                elif inputt < 0 or inputt > 100:
                    print("Girdiğiniz {} sayısı, 0 ile 100 arasında bir sayı değil!"
                          "Ve tahmin hakkınız {} kaldı".format(inputt,nmb_of_rmnng_forecast))
                    inpt = input("Devam etmek istiyorsanız 'E' tıklayın yoksa 'H' ye tıklayın: ").lower()
                    if inpt == 'e':
                        continue
                    else:
                        break

                elif number < inputt:
                    print("Girdiğin {} sayısı aklımda tuttuğum sayıdan büyük!".format(inputt))
                    print("{} tahminiz kaldı".format(nmb_of_rmnng_forecast))

                elif number > inputt:
                    print("Girdiğin {} sayısı aklımda tuttuğum sayıdan küçük!".format(inputt))
                    print("{} tahminiz kaldı".format(nmb_of_rmnng_forecast))

                elif nmb_of_rmnng_forecast == 0:
                    print("Tahmin hakkınız bitti.Sayımız {}.".format(number))
                    inpt = input("Devam etmek istiyorsanız 'E' tıklayın yoksa 'H' ye tıklayın: ").lower()
                    if inpt == 'e':
                        continue
                    else:
                        break

            except:
                print("Oyundan çıkış isteğiniz alındı.")
                break


if __name__ == "__main__":
    s = number_guessing_game()
    s.guessing()
    print("Program Kapatılıyor. Bekleyiniz...")
    time.sleep(2)