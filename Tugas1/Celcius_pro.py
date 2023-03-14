#Nama    : Irvan Afriandi
#NIM     : 200511099
#Kelas   : R4/D


class Celcius:
    @staticmethod
    def Fahrenheit(Cel):
        C = Cel
        return (9/5) * C + 32
    @staticmethod
    def Kelvin(Cel):
        C = Cel
        return C + 273
    @staticmethod
    def Reamur(Cel):
        C = Cel
        return 4/5 * C
    
CF = 75
CR = 60
CK = 90


fahrenheit = Celcius.Fahrenheit(CF)
reamur = Celcius.Reamur(CR) 
kelvin = Celcius.Kelvin(CK)
print("")
print("Konversi Celcius dengan PRO")
print("")
print("Konversi ",CF, "derajat Celcius adalah ",fahrenheit, "derajat Fahrenheit")
print("Konversi ",CR, "derajat Celcius adalah ",reamur, "derajat Reamur")
print("Konversi ",CK, "derajat Celcius adalah ",kelvin, "derajat Kelvin")

