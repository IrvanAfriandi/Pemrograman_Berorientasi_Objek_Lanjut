#Nama    : Irvan Afriandi
#NIM     : 200511099
#Kelas   : R4/D

class Celcius:
    def __init__(self, cel):
        self.cel = cel
    def Fahrenheit(self):
        C = self.cel
        CF = (9/5) * C + 32
        return CF
    def Kelvin(self):
        C = self.cel
        CK = C + 273
        return CK
    def Reamur(self):
        C = self.cel
        CR = 4/5 * C
        return CR
    
CF = 75
CR = 60
CK = 90

    
CelciusA = Celcius(CF)
CelciusB = Celcius(CR)
CelciusC = Celcius(CK)

print("")
print("Konversi Celcius dengan OPP")
print("")
print(f"Konversi ",CF, "derajat Celcius adalah : ",CelciusA.Fahrenheit(), "derajat Fahrenheit")
print(f"Konversi ",CR, "derajat Celcius adalah : ",CelciusB.Kelvin(), "derajat Kelvin")
print(f"Konversi ",CK, "derajat Celcius adalah : ",CelciusC.Reamur(), "derajat Reamur")