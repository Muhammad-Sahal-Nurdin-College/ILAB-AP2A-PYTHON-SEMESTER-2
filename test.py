# [1] import module yang Anda tulis
import segitigasiku

# Fungsi main menguji module


def main():
    # [2] Minta pengguna untuk memasukkan alas dan tinggi
    lebar = float(input('Masukkan panjang alas (cm): '))
    panjang = float(input('Masukkan tinggi (cm): '))
    num1 = segitigasiku.luas(lebar, panjang)
    print(f'Luas segitiga: {num1:.2f} cm2')
    num2 = segitigasiku.keliling(lebar, panjang)
    print(f'Keliling segitiga: {num2:.2f} cm')

    # [3] Hitung luas dan keliling dengan menggunakan fungsi pada module
    # [4] Tampilkan luas dan keliling dengan presisi 2 desimal

# Panggil fungsi main
main()







