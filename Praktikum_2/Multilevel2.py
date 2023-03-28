class Person:
    def __init__(self, nama, merk):
        self.nama = nama
        self.merk = merk
    def detail(self):
        print(f"Nama\t\t: {self.nama} \nMerk\t\t: {self.merk}")
class Fisik(Person):
    def __init__(self, nama, merk, jenis, keluaran):
        super().__init__(nama, merk)
        self.jenis = jenis
        self.keluaran = keluaran
    def detail(self):
        super().detail()
        print(f"Jenis\t\t: {self.jenis} \nKeluaran\t: {self.keluaran}")
class Warna(Fisik):
    def __init__(self, nama, merk, jenis, keluaran, warna):
        super().__init__(nama, merk, jenis, keluaran)
        self.warna = warna
    def detail(self):
        super().detail()
        print(f"Warna\t\t: {self.warna}")

motor = Warna("Supra X", "Honda", "X 125 cc", "2014", "Merah")
motor.detail()