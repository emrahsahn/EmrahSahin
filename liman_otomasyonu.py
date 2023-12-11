import chardet
import pandas as pd


class Truck:
    # tır nesnesini oluşturur
    def __init__(self, gelis_zamani, plaka, ulke, ton20, ton30, yuk_miktari, maliyet):
        self.arrival_time = gelis_zamani
        self.plaque = plaka
        self.country = ulke
        self.ton20 = ton20
        self.ton30 = ton30
        self.load_quantity = yuk_miktari
        self.cost = maliyet

        self.info = {
            "country": self.country,
            "ton20": self.ton20,
            "ton30": self.ton30,
            "load_quantity": self.load_quantity,
            "cost": self.cost,
        }

    def get_info(self):
        return self.info


truck = Truck


class Ship:
    # gemi nesnesini oluşturur
    def __init__(self, gelis_zamani, gemi_adi, kapasite, gidilecek_ulke):
        self.arrival_time = gelis_zamani
        self.name_ship = gemi_adi
        self.capacity = kapasite
        self.destination_country = gidilecek_ulke
        self.load = 0

        self.info = {
            "arrival_time": self.arrival_time,
            "name_ship": self.name_ship,
            "capacity": self.capacity,
            "destination_country": self.destination_country,
            "load_list": self.load
        }

    def load_update(self, load):
        if self.load + load <= self.capacity:
            self.load += load
            return True
        else:
            return False

    def get_info(self):
        return self.info


def chardet_encoding(file_path):
    with open(file_path, "rb") as file:  # rb dosyayı ikili modda okuyacağı anlamına gelir
        result = chardet.detect(file.read())  # dosya içeriğini analiz edip kodlamasını tespit eder
    return result["encoding"]


def time_and_plaque_sort_of_truck(truck):
    # Dosyayı geliş zamanının palakasına göre sıralama yapan fonksiyon
    arrival_time = truck[0]
    plaque = truck[1]
    number_part = plaque.split("_")[-1]
    # plakayı ayırıp son 4 hanesine göre sıralama yapıldı
    return (arrival_time, int(number_part))


greatest_value = 0
'''bu değeri fonksiyon dışında kullanacağım için dışarda tanımladık 
ve fonksiyon içinde kullanacağımız zaman global değişkeniyle çağırdık'''


def read_file_truck():
    # Olaylar dosyasını okuma fonksiyonu
    global greatest_value
    encodings = chardet_encoding("olaylar.csv")
    data = pd.read_csv("olaylar.csv", encoding=f"{encodings}")
    titles = data.columns
    greatest_value = data[titles[0]].max()

    # aynı zamanda gelen tırları plaka sırasına göre sıralama yaptık
    data[titles[1]] = data[titles[1]]
    data = data.sort_values(by=[titles[0], titles[1]])
    data = sorted(data.values.tolist(), key=time_and_plaque_sort_of_truck)
    return [Truck(*row) for row in data]  # bu satır bir for iteration satırıdır


def read_file_ship():
    # Gemiler dosyasını okuma fonksiyonu
    encodings = chardet_encoding("gemiler.csv")
    data = pd.read_csv("gemiler.csv", encoding=encodings)
    titles = data.columns

    data = data.to_dict(orient='records')  # bu sayede her satırı temsil eden bir sözlüğün listesini olur
    return [Ship(ship[titles[0]], ship[titles[1]], int(ship[titles[2]]), ship[titles[3]]) for ship in data]


# gemiler_objeleri = [Ship(ship["geliþ_zamaný"], ship["gemi_adý"], int(ship["kapasite"]), ship["gidecek_ülke"])
#                     for ship in load_list]

max_capacity = 750

stack_area_capacity1 = []
stack_area_capacity2 = []
current_load1 = 0
current_load2 = 0


# fonksiyonların içinde kullanılacağı için fonksiyonların dışında tanımlanan değişkenler

def load_download(truck):
    global current_load1
    # Tır dan yükü indirip istif alanı 1 e yığın olarak ekliyorum.
    if current_load1 + truck.load_quantity <= max_capacity:
        stack_area_capacity1.append(truck.get_info())
        current_load1 += truck.load_quantity
        print(f"İstif alanı 1'e {truck.load_quantity} ton yük {truck.country} ülkesine gidecek şekilde eklendi")
    else:
        # sadece tek bir istif alanına yük koyuluyor diğer istif alanı ilk istif alanı yığın olduğu için
        # onun gereksinimlerini sağlıyor.
        print("İstif alanı 1 kapasite dolu, yük eklenemiyor.")


def load_upload(ship):
    global current_load1, current_load2
    while stack_area_capacity1 and ship.load < ship.capacity:

        # İlk olarak yığın olarak sıralanan kargoların en üstündeki elemanı alıyoruz
        top_load = stack_area_capacity1.pop()
        current_load1 -= top_load["load_quantity"]
        # Sonra o anki istif alanı 1 deki toplam kapasiteden azaltıyoruz.

        if ship.load_update(top_load["load_quantity"]):
            print(f"Gemi {ship.name_ship} yüklendi: {top_load['load_quantity']} ton ")
            if ship.capacity * 0.95 <= ship.load:
                print(f"Gemi {ship.name_ship} yeterli doluluk düzeyine ulaştı ve gitti.")
            else:
                print(f"Gemi {ship.name_ship} beklemede")
        else:
            # Gemi doluysa yükü istif alanı 2'ye aktar.
            if current_load2 + top_load["load_quantity"] <= max_capacity:
                stack_area_capacity2.append(top_load)
                current_load2 += top_load["load_quantity"]
                print(f"Gemi {ship.name_ship} dolu. Yük istif alanı 2'ye aktarıldı.")
            else:
                print("İstif alanı 2 kapasite dolu, yük eklenemiyor.")


def total_price():
    encodings = chardet_encoding("olaylar.csv")
    data = pd.read_csv("olaylar.csv",encoding=encodings)
    titles = data.columns

    total = data[titles[-1]].sum()
    return f"Şuana kadarki toplam maliyet bu kadar {total}"

total_cost = total_price()

def simulation(trucks, ships):
    global stack_area_capacity1, stack_area_capacity2, current_load1, current_load2
    ships_waiting = {}  # Ülkelere göre bekleyen gemileri tutacak sözlük

    for time in range(greatest_value + 1):
        print(f"Zaman {time}")

        # O anki zamanda gelen tırları bul
        arriving_trucks = []
        for truck in trucks:
            if truck.arrival_time == time:
                arriving_trucks.append(truck)
        # O anki zamanda gelen tırlardan yükleri indirme
        for truck in arriving_trucks:
            load_download(truck)

        # O anki zamanda gelen gemileri bul ve bekleyen gemilere ekle
        arriving_ships = []
        for ship in ships:
            if ship.arrival_time == time:
                arriving_ships.append(ship)

        # Gelen gemileri bekleyen gemiler listesine yükle
        for ship in arriving_ships:
            if ship.destination_country not in ships_waiting:
                ships_waiting[ship.destination_country] = []
            ships_waiting[ship.destination_country].append(ship)

        # İstif alanı 1'deki yükleri uygun gemilere yükle
        for country, waiting_ships in list(ships_waiting.items()):
            for ship in waiting_ships:
                while stack_area_capacity1 and ship.load < ship.capacity:
                    # İstif alanı 1'den yük almadan önce kontrol et
                    if not stack_area_capacity1:
                        break  # İstif alanı 1 boşsa döngüyü kır

                    top_load = stack_area_capacity1[-1]
                    if top_load["country"] == country:
                        # İstenen ülkeye göre arama yap
                        if ship.load_update(top_load["load_quantity"]):
                            stack_area_capacity1.pop()  # Yükü yığından çıkar
                            current_load1 -= top_load["load_quantity"]
                            print(f"Gemi {ship.name_ship} yüklendi: {top_load['load_quantity']} ton")

                            if ship.capacity * 0.95 <= ship.load:
                                # Gemi yeterli doluluk düzeyine ulaştıysa gönder, yeni gemiye geç ve eski gemiyi listeden sil
                                print(f"Gemi {ship.name_ship} yeterli doluluk düzeyine ulaştı ve gitti.")
                                waiting_ships.remove(ship)
                                break  # Diğer gemilere geç
                        else:
                            # Gemi doluysa veya yüklenemiyorsa döngüyü kır ve yei döngüye başla
                            break
                    else:
                        # Aranan yük değilse, yükü geçici yığına taşı
                        stack_area_capacity2.append(stack_area_capacity1.pop())
                        current_load1 -= top_load["load_quantity"]
                        # print(f"İstif alanı 2'ye {top_load['load_quantity']} yük eklendi")

                while stack_area_capacity2:
                    # Geçici yığını istif alanı 1'e geri yükle
                    load = stack_area_capacity2.pop()
                    stack_area_capacity1.append(load)
                    current_load1 += load["load_quantity"]

        # Yükleme yapılmayan gemileri temizle
        new_ships_waiting = {}
        for country, ship_list in ships_waiting.items():
            if ship_list:
                new_ships_waiting[country] = ship_list

    # Sonuçları yazdırma
    print("İstif alanı 1: ", stack_area_capacity1)
    print("İstif alanı 2: ", stack_area_capacity2)
    for ship in ships:
        print(f"Gemi {ship.name_ship}: {ship.load} ton yüklendi")
    print("Toplam Maliyet: ",total_cost)

trucks = read_file_truck()
ships = read_file_ship()
simulation(trucks, ships)
