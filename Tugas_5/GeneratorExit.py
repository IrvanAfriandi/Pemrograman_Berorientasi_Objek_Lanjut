class MyGenerator:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > 3:
            raise StopIteration
        return self.count

    def close(self):
        print("Generator has been closed")

    def __del__(self):
        self.close()

try:
    gen = MyGenerator()
    print(next(gen)) 
    print(next(gen)) 
    gen.close()    
    print(next(gen))
except GeneratorExit:
    gen.close()
