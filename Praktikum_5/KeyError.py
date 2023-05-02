person = {"Nama": "Budi", "Umur": 30}

try:
    print(person["Alamat"])
except KeyError:
    print("Key yang diminta tidak tersedia pada dictionary!")
