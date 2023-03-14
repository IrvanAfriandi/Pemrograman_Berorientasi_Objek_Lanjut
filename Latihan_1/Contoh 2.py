class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    def info(self):
        print(f"Nama: {self.nama}\nNPM: {self.npm}")

mahasiswaB = Mahasiswa("Joko Wijayanto", "31003313")
mahasiswaB.info()
