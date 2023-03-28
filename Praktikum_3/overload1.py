class Shape:
    def hitung_luas(self):
        pass

class PersegiPanjang(Shape):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

class Lingkaran(Shape):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return 3.14 * (self.jari_jari ** 2)

def hitung_luas_benda(benda):
    print("Luas benda tersebut adalah:", benda.hitung_luas())

persegi_panjang = PersegiPanjang(5, 10)
lingkaran = Lingkaran(7)

hitung_luas_benda(persegi_panjang)
hitung_luas_benda(lingkaran)
