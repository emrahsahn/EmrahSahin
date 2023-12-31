# sayısal loto oyunu

import random
import time


class SayisalLoto():
    __baslik = "Sayısal Loto Kolonu Dolduran Program"

    def __init__(self):
        self.giris()

    def determining_number_of_columns(self):
        while True:
            try:
                number_of_column = int(input("Kaç tane kolon üretelim? : "))
                return number_of_column
            except:
                print("Bir tam sayı girilmedi. Tekrar deneyin...")

    def giris(self):
        print("*"*len(self.__baslik),self.__baslik,"*"*len(self.__baslik),sep="\n",end="\n")

        while True:
            request = input("Programdan çıkmak için q'e basınız\n"
                          "Devam etmek için herhangi bir tuşa basınız...")

            if request.lower() == "q":
                print("Program Kapatılıyor...")
                time.sleep(2)
                break

            nmbr = self.determining_number_of_columns()  # sayi tuple cinsinden olur.
            # print(number,type(number))
            column = []
            columns = []
            count = 0

            while count < nmbr:  # var olan bir kolon üretince onu kaydetmeyip tekrardan üretiyor.
                for s in range(0, 6):  # Bir kolonda 6 tane sayı olduğu için range(0,6)
                    number = random.randint(1, 50)  # Bir kolonda [1,50] aralığında sayı vardır.
                    while number in column:  # üretilen sayi kolonda varsa tekrardan üretilir.
                        number = random.randint(1, 50)
                    column.append(number)
                    column.sort()

                if column not in columns:  # farklı kolonların üretilmesi için
                    columns.append(column)
                    count += 1
                    print("{}. kolon = {}".format(count, column))
                else:
                    column = []


if __name__ == "__main__":
    sl = SayisalLoto()