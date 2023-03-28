# Membuat kelas induk
class Benda:
  def __init__(self, nama):
    self.nama = nama
  
  def get_nama(self):
    return self.nama

class Tanaman(Benda):
  def __init__(self, nama, jenis):
    super().__init__(nama)
    self.jenis = jenis
  
  def info(self):
    print("Ini adalah", self.get_nama(), "jenis", self.jenis)

class Hewan(Benda):
  def __init__(self, nama, habitat):
    super().__init__(nama)
    self.habitat = habitat
  
  def info(self):
    print("Ini adalah", self.get_nama(), "yang hidup di", self.habitat)

tanaman1 = Tanaman("Pohon Mangga", "Buah-buahan")
hewan1 = Hewan("Singa", "Hutan Rimba")
tanaman1.info()
hewan1.info()
