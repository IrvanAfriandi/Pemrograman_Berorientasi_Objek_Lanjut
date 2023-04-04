class Makanan:
    def __init__(self, nama_makanan, harga):
        self.nama_makanan = nama_makanan
        self.harga = harga
        
    def tampilkan_info(self):
        print(f"{self.nama_makanan:<20}Rp{self.harga:>10}")

class Menu:
    def __init__(self, nama_menu):
        self.nama_menu = nama_menu
        self.makanan = []
        
    def tambah_makanan(self, nama_makanan, harga):
        makanan = Makanan(nama_makanan, harga)
        self.makanan.append(makanan)
        print(f"{nama_makanan} telah ditambahkan ke dalam menu {self.nama_menu}\n")
        
    def tampilkan_menu(self):
        print(f"{'-'*45}")
        print(f"{'Menu Berbuka Puasa':^45}")
        print(f"{'-'*45}")
        print(f"{'Makanan':<20}Harga")
        print(f"{'-'*30}")
        for makanan in self.makanan:
            makanan.tampilkan_info()
        print(f"{'-'*30}")

menu_berbuka = Menu("Berbuka Puasa")
menu_berbuka.tambah_makanan("Kolak Pisang", 10000)
menu_berbuka.tambah_makanan("Es Kelapa Muda", 15000)
menu_berbuka.tambah_makanan("Bubur Sumsum", 8000)
menu_berbuka.tambah_makanan("Lumpia Semarang", 12000)
menu_berbuka.tampilkan_menu()
