class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama\t\t: {self.nama}")
        print(f"Umur\t\t: {self.umur}")
class Asal(Person):
    def __init__(self, asal):
        self.asal = asal
    def display_info(self):
        super().display_info()
        print(f"Asal\t\t: {self.asal}")
class Pekerjaan(Person):
    def __init__(self, nama, umur, pekerjaan):
        super().__init__(nama, umur)
        self.pekerjaan = pekerjaan
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan\t: {self.pekerjaan}")
class Biodata(Asal, Pekerjaan):
    def __init__(self, nama, umur, asal, pekerjaan):
        Asal.__init__(self, asal)
        Pekerjaan.__init__(self, nama, umur, pekerjaan)
bio = Biodata("Sutedjo Hassan", 35, "Malang", "Masinis")
bio.display_info()
