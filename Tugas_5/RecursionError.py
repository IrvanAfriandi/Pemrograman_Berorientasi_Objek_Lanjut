def count(n):
    if n == 0:
        return
    else:
        print(n)
        count(n-1)

try:
    count(10000)
except RecursionError as e:
    print("Terjadi kesalahan rekursi: ", e)
