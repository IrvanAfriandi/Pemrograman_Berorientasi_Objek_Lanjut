try:
    f = open('file_ghoib.txt')
except RuntimeError as e:
    print("Terjadi kesalahan: ", e)
