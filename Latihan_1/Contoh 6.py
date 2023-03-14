class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def subtract(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
    
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(1, 0)) # Output: 1
print(Kalkulator.subtract(7, 5)) # Output: 2
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(10, 3)) # Output: 30
print(Kalkulator.divide(12, 3)) # Output: 4.0