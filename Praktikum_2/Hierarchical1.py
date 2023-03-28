class Hewan:
  def __init__(self, nama):
    self.nama = nama
  
  def suara(self):
    pass
class Kucing(Hewan):
  def suara(self):
    print(self.nama, "mengeong")

class Anjing(Hewan):
  def suara(self):
    print(self.nama, "menggonggong")

kucing1 = Kucing("Tom")
anjing1 = Anjing("Pluto")
kucing1.suara()
anjing1.suara()
