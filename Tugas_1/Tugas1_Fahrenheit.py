#Nama    : Irvan Afriandi
#NIM     : 200511099
#Kelas   : R4/D

class Fahrenheit:
    def __init__(self, fah):
        self.fah = fah
    def Celcius(self):
        f = self.fah
        FahToCel = (f - 32) * 5/9
        FahToCel = int(FahToCel)
        return FahToCel
    def Kelvin(self):
        f = self.fah
        FahToKel = (f + 459.67) * 5/9
        FahToKel = int(FahToKel)
        return FahToKel
    def Reamur(self):
        f = self.fah
        FahToRea = 4/9 * (f - 32)
        FahToRea = int(FahToRea)
        return FahToRea
    
print("-"*45)
print("Konversi Nilai Fahrenheit ke Satuan Lainnya")
print("-"*45)
input = int(input("Masukkan Nilai Fahrenheit : "))
fahren = Fahrenheit(input)
print("="*45)
print("Jika dikonversikan kedalam satuan Celcius, hasilnya adalah :", fahren.Celcius(), "Derajat")
print("Jika dikonversikan kedalam satuan Reamur, hasilnya adalah  :", fahren.Reamur(), "Derajat")
print("Jika dikonversikan kedalam satuan Kelvin, hasilnya adalah  :", fahren.Kelvin(), "Derajat")