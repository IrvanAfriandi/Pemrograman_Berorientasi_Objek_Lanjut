try:
    x = 1.0/0.0
except FloatingPointError as error:
    print("Terjadi kesalahan pada operasi pembagian:", error)