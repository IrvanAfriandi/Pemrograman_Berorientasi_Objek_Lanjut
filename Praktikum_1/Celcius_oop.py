#Nama    : Irvan Afriandi
#NIM     : 200511099
#Kelas   : R4/D

class Celcius:
    def __init__(self, Cel):
        self.cel = Cel
    def Fahrenheit(self):
        C = self.cel
        CF = (9/5) * C + 32
        CF = int(CF)
        return CF
    def Kelvin(self):
        C = self.cel
        CK = C + 273
        CK = int(CK)
        return CK
    def Reamur(self):
        C = self.cel
        CR = 4/5 * C
        CR = int(CR)
        return CR
    
CelToFah = 75
CelToKel = 90
CelToRea = 60

    
Cel1 = Celcius(CelToFah)
Cel2 = Celcius(CelToKel)
Cel3 = Celcius(CelToRea)

print("")
print("Konversi Celcius dengan Object Oriented Programming")
print("")
print(f"Konversi dari",CelToFah, "derajat Celcius ke Fahrenheit adalah : ",Cel1.Fahrenheit(), "derajat ")
print(f"Konversi dari",CelToKel, "derajat Celcius ke Kelvin adalah     : ",Cel2.Kelvin(), "derajat ")
print(f"Konversi dari",CelToRea, "derajat Celcius ke Reamur adalah     : ",Cel3.Reamur(), "derajat ")