from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def hitung_kecepatan(self, jarak, waktu):
        pass

    @abstractmethod
    def jenis_kendaraan(self):
        pass

class Mobil(Kendaraan):
    def hitung_kecepatan(self, jarak, waktu):
        return jarak / waktu

    def jenis_kendaraan(self):
        return "Mobil"

class SepedaMotor(Kendaraan):
    def hitung_kecepatan(self, jarak, waktu):
        return jarak / waktu

    def jenis_kendaraan(self):
        return "Sepeda Motor"

# Membuat objek dari subclass
mobil = Mobil()
motor = SepedaMotor()

# Menghitung kecepatan
jarak = 120  # km
waktu = 2    # jam

print(f"Jenis Kendaraan: {mobil.jenis_kendaraan()}")
print(f"Kecepatan Mobil: {mobil.hitung_kecepatan(jarak, waktu)} km/jam")

print(f"\nJenis Kendaraan: {motor.jenis_kendaraan()}")
print(f"Kecepatan Sepeda Motor: {motor.hitung_kecepatan(jarak, waktu)} km/jam")