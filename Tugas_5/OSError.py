try:
    f = open("file.txt", "r")
except OSError as e:
    print("Tidak dapat membuka file: ", e)
