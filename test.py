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
