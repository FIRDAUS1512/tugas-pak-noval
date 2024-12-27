# Class 
class Headset:
    # Instance
    def __init__(self, jenis):
        self.jenis = jenis
        self.Merk = ""
        self.Warna = ""
        self.DayaTahanBaterai = ""

    # Method 1
    def printHeadset(self):
        print("Merk Headset : ", self.Merk)
        print("Warna Headset : ", self.Warna)
        print("Daya Tahan Baterai : ", self.DayaTahanBaterai if self.jenis == "Wireless" else "Tidak menggunakan baterai")
        print("Jenis Headset : ", self.jenis)
    
    # Method 2
    def statusPenggunaan(self, kondisi):
        print("Headset siap digunakan")
        print(kondisi)

# Objek
headset1 = Headset("Wireless")
headset2 = Headset("Dengan Kabel")

# Value
headset1.Merk = "Sony WH-1000XM5"
headset1.Warna = "Hitam"
headset1.DayaTahanBaterai = "30 jam"

headset2.Merk = "Sennheiser HD 660S"
headset2.Warna = "Silver"
headset2.DayaTahanBaterai = ""  # Tidak relevan untuk headset kabel

# Pemanggilan Method
headset1.printHeadset()
headset1.statusPenggunaan("Headset Wireless siap dipakai tanpa kabel")
headset2.printHeadset()
headset2.statusPenggunaan("Headset dengan kabel siap dipakai untuk audio berkualitas tinggi")
