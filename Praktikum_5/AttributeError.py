class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

anjing = Hewan("Doggy", "Anjing")
try:
    usia = anjing.usia
except AttributeError:
    print("Atribut 'usia' tidak ditemukan pada objek!")
