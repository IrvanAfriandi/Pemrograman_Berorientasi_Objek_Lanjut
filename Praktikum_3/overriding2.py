class Makanan:
    def __init__(self, nama):
        self.nama = nama

    def resep(self):
        pass

class NasiGoreng(Makanan):
    def resep(self):
        print("Bahan-bahan nasi goreng:\n- Nasi\n- Bumbu nasi goreng\n- Telur\n- Kecap manis\n- Sayuran (wortel, buncis, dsb.)\n- Daging atau ayam\n- Minyak goreng\n\nCara membuat nasi goreng:\n1. Panaskan minyak goreng di wajan.\n2. Tumis bumbu nasi goreng hingga harum.\n3. Tambahkan daging atau ayam dan masak hingga matang.\n4. Masukkan sayuran dan aduk rata.\n5. Pecahkan telur dan masukkan ke wajan, aduk hingga setengah matang.\n6. Tambahkan nasi dan kecap manis, aduk hingga semua bahan tercampur rata.\n7. Angkat dan sajikan nasi goreng.\n")

class MieGoreng(Makanan):
    def resep(self):
        print("Bahan-bahan mie goreng:\n- Mie instan\n- Bumbu mie goreng\n- Telur\n- Sayuran (wortel, buncis, dsb.)\n- Daging atau ayam\n- Minyak goreng\n\nCara membuat mie goreng:\n1. Rebus mie instan dan tiriskan.\n2. Panaskan minyak goreng di wajan.\n3. Tumis bumbu mie goreng hingga harum.\n4. Tambahkan daging atau ayam dan masak hingga matang.\n5. Masukkan sayuran dan aduk rata.\n6. Pecahkan telur dan masukkan ke wajan, aduk hingga setengah matang.\n7. Tambahkan mie instan dan aduk hingga semua bahan tercampur rata.\n8. Angkat dan sajikan mie goreng.\n")

class Sate(Makanan):
    def resep(self):
        print("Bahan-bahan sate:\n- Daging (ayam, sapi, atau kambing)\n- Bumbu sate\n- Kecap manis\n- Sambal\n\nCara membuat sate:\n1. Iris daging tipis-tipis.\n2. Tusuk daging di tusukan sate.\n3. Lumuri daging dengan bumbu sate dan kecap manis.\n4. Panggang sate di atas panggangan hingga matang.\n5. Sajikan sate dengan sambal.")

def tampilkan_resep(makanan):
    makanan.resep()

nasi_goreng = NasiGoreng("Nasi Goreng")
mie_goreng = MieGoreng("Mie Goreng")
sate = Sate("Sate")

tampilkan_resep(nasi_goreng)
tampilkan_resep(mie_goreng)
tampilkan_resep(sate)
