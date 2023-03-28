class Orang:
    def __init__(self, nama):
        self.nama = nama
    def skill(self):
        print(f"{self.nama}")
class Kelas(Orang):
    def __init__(self, nama, kelas):
        super().__init__(nama)
        self.kelas = kelas
    def kelass(self):
        print(f"{self.nama} adalah siswa kelas {self.kelas}")
class Ketrampilan(Kelas):
    def __init__(self, nama, kelas, skil):
        super().__init__(nama, kelas)
        self.skil = skil
    def skill(self):
        print(f"Walaupun masih kelas {self.kelas}, {self.nama} sudah mahir berbahasa {self.skil}")
siswa = Ketrampilan("Udin", 12, "Jerman dan Belanda")
siswa.kelass()
siswa.skill()