class PesawatTerbang:
    def __init__(self, maskapai, tujuan):
        self.maskapai = maskapai
        self.tujuan = tujuan
    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}")

pesawatA = PesawatTerbang("Batik Air", "Bandung - Makassar")
pesawatA.info()
