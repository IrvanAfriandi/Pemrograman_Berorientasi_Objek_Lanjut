class Perusahaan:
    def __init__(self, nama_perusahaan, pendiri):
        self.nama_perusahaan = nama_perusahaan
        self.pendiri = pendiri
        self.karyawan = []
        
    def tambah_karyawan(self, nama_karyawan):
        karyawan = Karyawan(nama_karyawan, self)
        self.karyawan.append(karyawan)
        print(f"Karyawan '{nama_karyawan}' telah ditambahkan ke daftar karyawan di perusahaan {self.nama_perusahaan}\n")
        
    def tampilkan_daftar_karyawan(self):
        print(f"Daftar karyawan di perusahaan {self.nama_perusahaan}:")
        for karyawan in self.karyawan:
            print(f"- {karyawan.nama_karyawan}")
        print()
            

class Pendiri:
    def __init__(self, nama_pendiri):
        self.nama_pendiri = nama_pendiri
        self.perusahaan = []
        
    def tambah_perusahaan(self, nama_perusahaan):
        perusahaan = Perusahaan(nama_perusahaan, self)
        self.perusahaan.append(perusahaan)
        print(f"Perusahaan '{nama_perusahaan}' telah ditambahkan ke daftar perusahaan {self.nama_pendiri}\n")
        
    def tampilkan_daftar_perusahaan(self):
        print(f"Daftar perusahaan yang didirikan oleh {self.nama_pendiri}:")
        for perusahaan in self.perusahaan:
            print(f"- {perusahaan.nama_perusahaan}")
        print()
        

class Karyawan:
    def __init__(self, nama_karyawan, perusahaan):
        self.nama_karyawan = nama_karyawan
        self.perusahaan = perusahaan
        
    def tampilkan_perusahaan(self):
        print(f"{self.nama_karyawan} bekerja di perusahaan {self.perusahaan.nama_perusahaan}\n")

elon = Pendiri("Elon Musk")
tesla = Perusahaan("Tesla", elon)
spacex = Perusahaan("SpaceX", elon)
boring_company = Perusahaan("The Boring Company", elon)

tesla.tambah_karyawan("Sarah")
tesla.tambah_karyawan("John")
spacex.tambah_karyawan("Lisa")
tesla.tampilkan_daftar_karyawan()
spacex.tampilkan_daftar_karyawan()
elon.tambah_perusahaan("Neuralink")
elon.tambah_perusahaan("OpenAI")
elon.tampilkan_daftar_perusahaan()
