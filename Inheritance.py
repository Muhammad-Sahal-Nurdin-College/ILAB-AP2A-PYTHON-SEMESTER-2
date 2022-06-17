# Program ini mendemonstrasikan class Sedan, Pickup, dan SUV import kendaraan
import kendaraan

def main():
    # Buat object Sedan
    sedan = kendaraan.Sedan('BMW', '323', 500000000, 4)
    # Buat object Pickup
    pickup = kendaraan.Pickup('Toyota', 'Hilux', 350000000, '4WD')
    # Buat object SUV
    suv = kendaraan.SUV('Hyundai', 'Santa Fe', 550000000, 6)
    print('Data Kendaraan')
    print('=================')
    # Tampilkan data Sedan
    print('Merek:', sedan.get_merek())
    print('Model:', sedan.get_model())
    print('Jumlah Pintu:', sedan.get_pintu())
    print()
    # Tampilkan data Pickup
    print('Merek:', pickup.get_merek())
    print('Model:', pickup.get_model())
    print(f'Harga: Rp.{pickup.get_harga(): ,.2f}')
    print('Tipe Penggerak:', pickup.get_tipe_penggerak())
    print()
    # Tampilkan data SUV
    print('Merek:', suv.get_merek())
    print('Model:', suv.get_model())
    print(f'Harga: Rp.{suv.get_harga(): ,.2f}')
    print('Kapasitas Penumpang:', suv.get_kap_penumpang())
    print()
# Panggil fungsi main
main()



# Soal Nomor 1
class Orang:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur

    def set_tampilkan_nama(self, nama):
        self.__nama = nama

    def set_tampilkan_umur(self, umur):
        self.__umur = umur

    def tampilkan_nama(self):
        return print('Nama saya adalah', self.__nama)

    def tampilkan_umur(self):
        return print('Umur saya adalah', self.__umur)


class Siswa(Orang):
    def __init__(self, nama, umur, tingkat):
        Orang.__init__(self, nama, umur)
        self.__tingkat = tingkat

    def set_tampilkan_tingkat(self, tingkat):
        self.__tingkat = tingkat

    def tampilkan_tingkat(self):
        return print('Saya tingkat', self.__tingkat)


class Pekerja(Orang):
    def __init__(self, nama, umur, pekerjaan):
        Orang.__init__(self, nama, umur)
        self.__pekerjaan = pekerjaan

    def set_tampilkan_pekerjaan(self, pekerjaan):
        self.__pekerjaan = pekerjaan

    def tampilkan_pekerjaan(self):
        return print('Pekerjaan saya', self.__pekerjaan)

orang1 = Orang('Budi Susilo', 33)
siswa1 = Siswa('Andi Geledek', 17, '12')
pekerja1 = Pekerja('Tomi Gunawan', 32, 'Wiraswasta')

print('Informasi orang 1:')
print('Nama saya adalah', orang1.tampilkan_nama())
print('Umur saya adalah', orang1.tampilkan_umur())
print()

print('Informasi siswa 1:')
print('Nama saya adalah', siswa1.tampilkan_nama())
print('Umur saya adalah', siswa1.tampilkan_umur())
print('Saya tingkat', siswa1.tampilkan_tingkat())
print()

print('Informasi pekerja 1:')
print('Nama saya adalah', pekerja1.tampilkan_nama())
print('Umur saya adalah', pekerja1.tampilkan_umur())
print('Pekerjaan saya', pekerja1.tampilkan_pekerjaan())


