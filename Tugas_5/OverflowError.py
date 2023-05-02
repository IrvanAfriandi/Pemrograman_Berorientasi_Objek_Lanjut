try:
    a = 10 ** 1000
except OverflowError as e:
    print("Terjadi kesalahan overflow: ", e)
