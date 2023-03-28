class Kendaraan:
    def nyalakan_mesin(self):
        pass

class Mobil(Kendaraan):
    def nyalakan_mesin(self):
        print("Mobil dinyalakan mesinnya")

class Motor(Kendaraan):
    def nyalakan_mesin(self):
        print("Motor dinyalakan mesinnya")

class Kapal(Kendaraan):
    def nyalakan_mesin(self):
        print("Kapal dinyalakan mesinnya")

def nyalakan_mesin_kendaraan(kendaraan):
    kendaraan.nyalakan_mesin()

mobil = Mobil()
motor = Motor()
kapal = Kapal()

nyalakan_mesin_kendaraan(mobil)
nyalakan_mesin_kendaraan(motor)
nyalakan_mesin_kendaraan(kapal)
