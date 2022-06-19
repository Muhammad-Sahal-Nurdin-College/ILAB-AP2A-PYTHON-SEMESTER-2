# [1] Import module yang telah anda buat
import mahasiswa


# Fungsi main untuk menguji class Mahasiswa
def main():

    # [2] Buat tiga object mahasiswa dari class Mahasiswa sesuai dengan data pada tabel
    object1 = mahasiswa.Mahasiswa('Budi Susilo', 11223344, 'Teknik Informatika', '0811-1234-7896')
    object2 = mahasiswa.Mahasiswa('Inggrid Wijaya', 11286755, 'Sistem Informasi', '0819-0086-9978')
    object3 = mahasiswa.Mahasiswa('Amelia', 11245645, 'Ilmu Komunikasi', '0838-7765-0987')

    # [3] Tampilkan Data Mahasiswa 1
    print('Nama:', object1.get_nama())
    print('NPM:', object1.get_npm())
    print('Jurusan:', object1.get_jurusan())
    print('Nomor Telepon:', object1.get_no_telepon())
    print()

    # [4] Tampilkan Data Mahasiswa 2
    print('Nama:', object2.get_nama())
    print('NPM:', object2.get_npm())
    print('Jurusan:', object2.get_jurusan())
    print('Nomor Telepon:', object2.get_no_telepon())
    print()

    # [5] Tampilkan Data Mahasiswa 3
    print('Nama:', object3.get_nama())
    print('NPM:', object3.get_npm())
    print('Jurusan:', object3.get_jurusan())
    print('Nomor Telepon:', object3.get_no_telepon())
    print()


# Panggil fungsi main
main()

