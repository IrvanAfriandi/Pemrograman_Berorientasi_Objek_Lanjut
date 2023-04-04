class Peneliti:
    def __init__(self, nama, institusi):
        self.nama = nama
        self.institusi = institusi
        self.jurnal_terpublikasi = []
        
    def tambah_jurnal(self, judul):
        self.jurnal_terpublikasi.append(judul)
        print(f"Jurnal '{judul}' telah ditambahkan ke dalam daftar jurnal terpublikasi {self.nama}")
        
    def tampilkan_jurnal_terpublikasi(self):
        print(f"Daftar jurnal terpublikasi oleh {self.nama}:")
        for judul in self.jurnal_terpublikasi:
            print(judul)
            
class Jurnal:
    def __init__(self, judul, tahun_terbit, penulis):
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penulis = penulis
        
    def tampilkan_informasi(self):
        print(f"Judul: {self.judul}")
        print(f"Tahun terbit: {self.tahun_terbit}")
        print(f"Penulis: {self.penulis}")
        
peneliti1 = Peneliti("Dr. Burhan", "Universitas Muhammadiyah Cirebon")
jurnal1 = Jurnal("Penelitian Terbaru tentang COVID-19", 2022, "Mukidi")
peneliti1.tambah_jurnal(jurnal1.judul)
peneliti1.tampilkan_jurnal_terpublikasi()
jurnal1.tampilkan_informasi()