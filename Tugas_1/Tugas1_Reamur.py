#Nama    : Irvan Afriandi
#NIM     : 200511099
#Kelas   : R4/D

class Reamur:
    def __init__(self, rea):
        self.rea = rea
    def Celcius(self):
        r = self.rea
        KelToCel = r / 0.8
        KelToCel = int(KelToCel)
        return KelToCel
    def Fahrenheit(self):
        r = self.rea
        KelToFah = (r * 2.25) + 32
        KelToFah = int(KelToFah)
        return KelToFah
    def Kelvin(self):
        r = self.rea
        KelToRea = (r / 0.8) + 273.15
        KelToRea = int(KelToRea)
        return KelToRea
    
print("-"*45)
print("Konversi Nilai Reamur ke Satuan Lainnya")
print("-"*45)
input = int(input("Masukkan Nilai Reamur : "))
reamur = Reamur(input)
print("="*45)
print("Jika dikonversikan kedalam satuan Celcius, hasilnya adalah     :", reamur.Celcius(), "Derajat")
print("Jika dikonversikan kedalam satuan Fahrenhite, hasilnya adalah  :", reamur.Fahrenheit(), "Derajat")
print("Jika dikonversikan kedalam satuan Kelvin, hasilnya adalah      :", reamur.Kelvin(), "Derajat")