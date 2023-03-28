class Kendaraan:
  def __init__(self, merek, tahun, warna):
    self.merek = merek
    self.tahun = tahun
    self.warna = warna
  
  def info(self):
    print("Merek:", self.merek)
    print("Tahun:", self.tahun)
    print("Warna:", self.warna)

class Harga:
  def __init__(self, harga):
    self.harga = harga
  
  def info_harga(self):
    print("Harga:", self.harga)

class Mobil(Kendaraan, Harga):
  def __init__(self, merek, tahun, warna, harga):
    Kendaraan.__init__(self, merek, tahun, warna)
    Harga.__init__(self, harga)

  def info_mobil(self):
    self.info()
    self.info_harga()

mobil1 = Mobil("Toyota", 2021, "Merah", 250000000)
mobil1.info_mobil()
