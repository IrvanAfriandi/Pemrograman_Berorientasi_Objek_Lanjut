class Hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def makan(self):
        print(f"{self.nama} sedang makan")

class HewanDarat(Hewan):
    def berjalan(self):
        print(f"{self.nama} sedang berjalan di darat")

class HewanAir(Hewan):
    def berenang(self):
        print(f"{self.nama} sedang berenang di air")

class KudaNil(HewanDarat, HewanAir):
    def __init__(self, nama):
        super().__init__(nama)

kuda_nil = KudaNil("Kuda Nil")
kuda_nil.makan()
kuda_nil.berjalan()
kuda_nil.berenang()
