# [1] import module yang anda buat
import pet


# Fungsi main menguji module
def main():
    # [2] Minta pengguna menginput nama, jenis dan umur
    x = input('Siapa nama hewan peliharaan Anda?', )
    Y = input('Jenis hewan apa peliharaan Anda?', )
    Z = input('Berapa umur hewan peliharaan Anda?', )

    # [3] Buat objek hewan
    hewan = pet.Pet()

    # [4] Tampilkan nama,jenis dan umur
    print('Nama: ', )
    print('Jenis hewan: ', )
    print('Umur (tahun): ', )


# Panggil fungsi main
main()

