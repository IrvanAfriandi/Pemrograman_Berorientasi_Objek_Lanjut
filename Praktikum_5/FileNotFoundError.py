import os

filename = "file.txt"
if os.path.isfile(filename):
    with open(filename) as f:
        print(f.read())
else:
    print("File tidak ditemukan!")
