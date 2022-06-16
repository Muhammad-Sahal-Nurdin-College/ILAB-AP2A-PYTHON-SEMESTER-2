# [1] import module yang anda buat
import pet


# Fungsi main menguji module
def main():
    # [2] Minta pengguna menginput nama, jenis dan umur
    x = input('Siapa nama hewan peliharaan Anda? ')
    y = input('Jenis hewan apa peliharaan Anda? ')
    z = int(input('Berapa umur hewan peliharaan Anda? '))

    s = pet.Pet(x, y, z)

    # [3] Buat objek hewan
    s.nama = x
    s.jenis = y
    s.umur = z
    nama2 = s.nama
    jenis2 = s.jenis
    umur2 = s.umur
    print()

    # [4] Tampilkan nama,jenis dan umur
    print('Nama:', nama2)
    print('Jenis hewan:', jenis2)
    print('Umur (tahun):', umur2)


# Panggil fungsi main
main()
