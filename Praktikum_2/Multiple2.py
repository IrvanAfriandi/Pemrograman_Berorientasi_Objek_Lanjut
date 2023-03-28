class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama\t\t: {self.nama}")
        print(f"Umur\t\t: {self.umur}")
class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji
    def display_info(self):
        print(f"Pekerjaan\t: {self.pekerjaan}")
        print(f"Penghasilan\t: {self.gaji}")
class Designer:
    def __init__(self, kontak, email):
        self.kontak = kontak
        self.email = email
    def display_info(self):
        print(f"Kontak Person\t: {self.kontak}")
        print(f"Email\t\t: {self.email}")
class DesignerPekerja(Orang, Pekerja, Designer):
    def __init__(self, nama, umur, pekerjaan, gaji, kontak, email):
        Orang.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Designer.__init__(self, kontak, email)
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan\t: {self.pekerjaan}")
        print(f"Penghasilan\t: {self.gaji}")
        print(f"Kontak Person\t: {self.kontak}")
        print(f"Email\t\t: {self.email}")
# contoh penggunaan
desidn_pekerjaC = DesignerPekerja("Muhammad Ilham Ashari", 27, "Designer", "1 juta sampai 5 juta rupiah", "085552227779", "ashariilham374@gmail.com")
desidn_pekerjaC.display_info()
