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