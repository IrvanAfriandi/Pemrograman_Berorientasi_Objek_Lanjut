import os

try:
    os.mkdir("my_directory")
except SystemError as e:
    print(f"Gagal membuat direktori: {e}")
