# [1] Impor module statistik yang Anda upload
import statistik


# Fungsi main menggunakan module statistik
# dan menampilkan statistik dari data dalam sebuah file
def main():
    # [2] Minta user memasukkan nama file yang berisi data
    # dengan prompt: 'Masukkan nama file: '
    x = float(input('Masukkan nama file: '))

    # [3] Struktur try/except untuk error file tidak ditemukan
    # dan file berisi data non numerik
    # Baca isi file dan gunakan fungsi-fungsi pada module yang Anda tulis
    # untuk mendapatkan nilai mean, variansi, standard deviasi, median dan modus.
    # Dan tampilkan nilai-nilai tersebut dengan presisi dua desimal.
    try:
        dim = open(x, 'r')
        for i in dim:
            y = float(i)
            data.append(y)


    except FileNotFoundError:
        print('File tidak ditemukan.')
    except ValueError:
        print('Terdapat data non numerik dalam file.')
    else:
        print(f'Mean dari data:{}')
        print(f'Variansi dari data:{}')
        print(f'Standar Deviasi dari data:{}')
        print(f'Median dari data:{}')


# Panggil fungsi main
main()






