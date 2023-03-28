class MediaCetak:
    def cetak(self):
        pass

class Koran(MediaCetak):
    def cetak(self):
        print("Koran dicetak menggunakan mesin cetak offset")

class Majalah(MediaCetak):
    def cetak(self):
        print("Majalah dicetak menggunakan mesin cetak rotogravure")

class Buku(MediaCetak):
    def cetak(self):
        print("Buku dicetak menggunakan mesin cetak digital")

def cetak_media(media):
    media.cetak()

koran = Koran()
majalah = Majalah()
buku = Buku()

cetak_media(koran)
cetak_media(majalah)
cetak_media(buku)
