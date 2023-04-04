class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.sks = 0
        self.matakuliah = []

    def tambah_matakuliah(self, matakuliah, sks):
        self.matakuliah.append({"nama": matakuliah, "sks": sks})
        self.sks += sks
        print(f"{sks} SKS telah ditambahkan untuk matakuliah {matakuliah}.")

    def tampilkan_info(self):
        print(f"{'-'*45}")
        print(f"{'Kartu Rencana Studi':^45}")
        print(f"{'-'*45}")
        print(f"NIM\t\t: {self.nim}")
        print(f"Nama\t\t: {self.nama}")
        print(f"Jurusan\t\t: {self.jurusan}")
        print(f"Total SKS\t: {self.sks}")
        print(f"{'-'*45}")
        print(f"{'Matakuliah':<30}SKS")
        print(f"{'-'*30}")
        for matakuliah in self.matakuliah:
            print(f"{matakuliah['nama']:<30}{matakuliah['sks']}")

mahasiswa = Mahasiswa("Budi", "123456789", "Teknik Informatika")
mahasiswa.tambah_matakuliah("Algoritma Pemrograman", 4)
mahasiswa.tambah_matakuliah("PBO", 3)
mahasiswa.tambah_matakuliah("Struktur Data", 3)
mahasiswa.tampilkan_info()
