# hewan.py
# Class mamalia merepresentasikan mamalia generik
class Mamalia:
    # Method __init__ menerima sebuah argumen untuk    # spesies mamalia
    def __init__(self, spesies):
        self.__spesies = spesies
    # Method tampilkan_spesies menampilkan sebuah pesan
    # yang menunjukkan spesies dari mamalia.


def tampilkan_spesies(self):
    print('Saya adalah seekor', self.__spesies)
    # Method buat_suara menampilkan suara generik dari mamalia


def buat_suara(self):
    print('Grrrr')



# SOAN NOMOR 1

class Burung:
    def __init__(self, spesies):
        self.__spesies = spesies


    def tampilkan_spesies(self):
        return print('Saya adalah seekor ', self.__spesies)


    def buat_suara(self):
        print('Ciut... Ciut...')


class Ayam(Burung):
    def __init__(self):
        Burung.__init__(self, 'ayam')


    def buat_suara(self):
        print('Kukuruyuuuk...')


class Bebek(Burung):
    def __init__(self):
        Burung.__init__(self, 'bebek')


    def buat_suara(self):
        print('Kwek! Kwek!')

burung = Burung('burung generik')
ayam = Ayam()
bebek = Bebek()

burung.tampilkan_spesies()
burung.buat_suara()
print()

ayam.tampilkan_spesies()
ayam.buat_suara()
print()

bebek.tampilkan_spesies()
bebek.buat_suara()


# Soal Nomor 2
class Sayuran:
    def __init__(self, jenis_sayuran):
        self.__jenis_sayuran = jenis_sayuran

    def pesan(self):
        print('Saya adalah sayuran.')

class Kentang(Sayuran):
    def __init__(self):
        Sayuran.__init__(self, 'kentang')

    def pesan(self):
        print('Saya adalah kentang.')

k = Kentang()
k.pesan()

