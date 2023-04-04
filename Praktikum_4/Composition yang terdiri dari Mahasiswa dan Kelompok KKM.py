class Kelompok_KKM:
    def __init__(self, nama_kelompok):
        self.nama_kelompok = nama_kelompok
        self.anggota = []
        
    def tambah_anggota(self, mahasiswa):
        self.anggota.append(mahasiswa)
        print(f"Mahasiswa {mahasiswa.nama} telah ditambahkan ke dalam Kelompok KKM {self.nama_kelompok}")
        
    def tampilkan_anggota(self):
        print(f"Anggota Kelompok KKM {self.nama_kelompok}:")
        for mahasiswa in self.anggota:
            print(mahasiswa.nama)
            
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok = None
        
    def bergabung_kelompok(self, kelompok):
        self.kelompok = kelompok
        kelompok.tambah_anggota(self)
        
    def tampilkan_informasi(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        if self.kelompok:
            print(f"Kelompok KKM: {self.kelompok.nama_kelompok}")
        else:
            print("Belum bergabung dengan kelompok KKM")
            
kelompok1 = Kelompok_KKM("Kelompok KKM 3")
mahasiswa1 = Mahasiswa("Agus", "210511001")
mahasiswa2 = Mahasiswa("Budi", "210511002")
mahasiswa1.bergabung_kelompok(kelompok1)
mahasiswa2.bergabung_kelompok(kelompok1)
kelompok1.tampilkan_anggota()
mahasiswa1.tampilkan_informasi()
mahasiswa2.tampilkan_informasi()
