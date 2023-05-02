try:
    with open("file.txt") as file:
        data = file.read(1000)
        if not data:
            raise EOFError("Tidak dapat membaca data dari file")
except EOFError as error:
    print(error)
