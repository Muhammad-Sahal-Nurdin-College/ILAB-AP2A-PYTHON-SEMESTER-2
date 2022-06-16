# Definisi class Mobil
# Attribute: __pabrikan, __model, dan __kecepatan
# Method: akselerasi(), rem(), get_kecepatan()
class Mobil:
    def __init__(self, pabrikan, model, kecepatan=0):
        self.__pabrikan = pabrikan
        self.__model = model
        self.__kecepatan = kecepatan

    def akselerasi(self):
        self.__kecepatan += 5

    def rem(self):

        if self.__kecepatan > 0:
            self.__kecepatan -= 5
        else:
            self.__kecepatan = 0

    def get_kecepatan(self):
        return self.__kecepatan

# [1] Tuliskan method __init__ yang menerima argumen pabrikan dan model
# dan menugaskannya ke attribute __pabrikan dan __model.
# Method __init__ juga menginisialisasi attribute __kecepatan dengan nilai 0


# [2] Tuliskan method akselerasi yang menambahkan attribute __kecepatan dengan nilai 5


# [3] Tuliskan method rem yang mengurangi attribute __kecepatan dengan nilai 5.
# Tambahkan kondisi yang mencegah __kecepatan bernilai negatif


# [4] Tuliskan method accessor get_kecepatan yang mengembalikan nilai attribute
# __kecepatan

def main():
    mobil = Mobil('Toyota', 'Agya')

    # Akselerasi lima kali dan tampilkan kecepatan terkini setiap kali akselerasi
    mobil.akselerasi()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.akselerasi()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.akselerasi()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.akselerasi()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.akselerasi()
    print('Kecepatan:', mobil.get_kecepatan())

    # Rem tujuh kali dan tampilkan kecepatan terkini setiap kali rem
    mobil.rem()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.rem()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.rem()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.rem()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.rem()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.rem()
    print('Kecepatan:', mobil.get_kecepatan())

    mobil.rem()
    print('Kecepatan:', mobil.get_kecepatan())

main()


