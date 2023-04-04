class Penulis:
    def __init__(self, nama_penulis):
        self.nama_penulis = nama_penulis
        self.daftar_buku = []
        
    def tambah_buku(self, judul_buku, tahun_terbit):
        buku = Buku(judul_buku, tahun_terbit, self)
        self.daftar_buku.append(buku)
        print(f"Buku '{judul_buku}' telah ditambahkan ke daftar buku penulis {self.nama_penulis}")
        
    def tampilkan_daftar_buku(self):
        print(f"Daftar buku penulis {self.nama_penulis}:")
        for buku in self.daftar_buku:
            print(f"{buku.judul} ({buku.tahun_terbit})")
            

class Buku:
    def __init__(self, judul, tahun_terbit, penulis):
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penulis = penulis
        
    def tampilkan_informasi(self):
        print(f"Judul buku: {self.judul}")
        print(f"Tahun terbit: {self.tahun_terbit}")
        print(f"Penulis: {self.penulis.nama_penulis}")
     
raditya_dika = Penulis("Raditya Dika")
raditya_dika.tambah_buku("Kambing Jantan", 2005)
raditya_dika.tambah_buku("Cinta Brontosaurus", 2012)
raditya_dika.tambah_buku("Marmut Merah Jambu", 2010)
raditya_dika.tampilkan_daftar_buku()
