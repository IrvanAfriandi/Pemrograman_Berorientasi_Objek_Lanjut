class Motor:
    def __init__(self, merk, kecepatan):
        self.merk = merk
        self.kecepatan = kecepatan
    def merek(self):
        print("Motor", self.merk, "melaju dengan kecepatan", self.kecepatan)
class Kelas(Motor):
    def __init__(self, merk, kecepatan, jarak):
        super().__init__(merk, kecepatan)
        self.jarak = jarak
    def keterangan(self):
        print("Motor",self.merk,"berjalan sejauh",self.jarak,"dengan kecepatan",self.kecepatan)
kelasA = Kelas("Supra 125", "100 km/jam", "700 km")
kelasA.merek() 
kelasA.keterangan()