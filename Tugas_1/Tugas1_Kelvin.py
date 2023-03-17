#Nama    : Irvan Afriandi
#NIM     : 200511099
#Kelas   : R4/D

class Kelvin:
    def __init__(self, kel):
        self.kel = kel
    def Celcius(self):
        k = self.kel
        KelToCel = k - 273.15
        KelToCel = int(KelToCel)
        return KelToCel
    def Fahrenheit(self):
        k = self.kel
        KelToFah = (k * 9/5) - 459.67
        KelToFah = int(KelToFah)
        return KelToFah
    def Reamur(self):
        k = self.kel
        KelToRea = 4/5 * (k - 273)
        KelToRea = int(KelToRea)
        return KelToRea
    
print("-"*45)
print("Konversi Nilai kelvin ke Satuan Lainnya")
print("-"*45)
input = int(input("Masukkan Nilai Kelvin : "))
kelvin = Kelvin(input)
print("="*45)
print("Jika dikonversikan kedalam satuan Celcius, hasilnya adalah     :", kelvin.Celcius(), "Derajat")
print("Jika dikonversikan kedalam satuan Fahrenhite, hasilnya adalah  :", kelvin.Fahrenheit(), "Derajat")
print("Jika dikonversikan kedalam satuan Reamur, hasilnya adalah      :", kelvin.Reamur(), "Derajat")