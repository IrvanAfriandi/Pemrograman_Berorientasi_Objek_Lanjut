class Hari:
    def __init__(self, hari1, hari2):
        self.hari1 = hari1
        self.hari2 = hari2
    def sekarang(self):
        print(f"Hari ini adalah hari {self.hari2}")
class Esok(Hari):
    def __init__(self, hari1, hari2, hari3):
        super().__init__(hari1, hari2)
        self.hari3 = hari3
    def besok(self):
        print(f"Kemarin adalah hari {self.hari1} dan besok adalah hari {self.hari3}, maka sekarang adalah hari {self.hari2}.")
Hr = Esok("Senin", "Selasa", "Rabu")
Hr.sekarang() 
Hr.besok() 
