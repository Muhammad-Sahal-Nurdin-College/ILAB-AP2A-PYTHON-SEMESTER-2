# NOMOR 1
# Program ini menuliskan teks "Bandung", "Jakarta", "Depok" masing-masing dalam satu baris ke file kota.txt
def main():
    # [1] Tuliskan statement untuk membuka file kota.txt untuk ditulis dan referensikan object file ke variabel output_file
    dim = open('kota.txt', 'w')
    # [2] Tuliskan statement-statement untuk menulis teks 'Bandung', 'Jakarta', 'Depok'
    # masing-masing dalam satu baris ke file kota.txt denga method write.
    dim.write('Bandung\n')
    dim.write('Jakarta\n')
    dim.write('Depok\n')
    # [3] Tuliskan statement untuk menutup file kota.txt
    dim.close()
# Panggil fungsi main
main()

# NOMOR 2
# Program ini membaca keseluruhan isi file kota.txt
def main():
    # Tuliskan kode Anda di bawah.
    # [1] Tuliskan statement buka file kota.txt untuk dibaca
    dim = open('kota.txt', 'r')

    # [2] Tuliskan statement untuk membaca keseluruhan isi file kota.txt dan simpan isi file dalam variabel isi_file
    isi_dim = dim.read()

    # [3] Tuliskan statement untuk menutup file kota.txt
    dim.close()

    # [4] Tuliskan statement untuk mencetak nilai dari variabel isi_file yang menyimpan isi file kota.txt
    print(isi_dim)


# Panggil fungsi main
main()

# NOMOR 4
# Program ini menambahkan teks 'Surabaya' dan 'Medan'
# masing-masing dalam satu baris ke file kota.txt
def main():
    # [1] Tuliskan statement untuk membuka file kota.txt untuk ditulis dengan modus 'a'
    dim = open('kota.txt', 'a')

    # [2] Tuliskan statement untuk menambahkan teks 'Surabaya' dan 'Medan' ke file kota.txt
    dim.write('Surabaya\n')
    dim.write('Medan\n')

    # [3] Tuliskan statement untuk menutup file kota.txt
    dim.close()


# Panggil fungsi main
main()

# NOMOR 6
# Program ini meminta pengguna memasukkan sebuah nama kota
# dan menambahkan nama kota yang dimasukkan tersebut ke file kota.txt
def main():
    # [1] Tuliskan staement untuk meminta nama kota ke pengguna dengan prompt: "Masukkan nama kota: "
    dim = input('Masukkan nama kota: ')

    # [2] Tuliskan statement untuk membuka file kota.txt untuk ditulis dengan modus 'a' dan referensikan object file ke variabel output_file
    dima = open('kota.txt', 'a')

    # [3] Tuliskan statement untuk menulis nama kota yang dimasukkan pengguna dalam baris baru
    dima.write(dim + '\n')

    # [4] Tuliskan statement untuk menutup file
    dima.close()

    # [5] Tuliskan statement yang menampilkan pesan "Data telah ditambahkan ke file kota.txt."
    print('Data telah ditambahkan ke file kota.txt.')


# Panggil fungsi main
main()

# NOMOR 7
# Program ini membaca file menggunakan statement with
def main():
    # [1] Buka file kota.txt untuk dibaca dan tugaskan object file ke variabel input_file
    # dengan statement with. Lalu simpan seluruh isi file ke sebuah variabel bernama isi_file.
    with open('kota.txt', 'r') as input_dim:
        d1 = input_dim.readline()
        d2 = input_dim.readline()
        d3 = input_dim.readline()
        d4 = input_dim.readline()
    d = d1.rstrip(\n)
    i = d2.rstrip(\n)
    m = d3.rstrip(\n)
    a = d4.rstrip(\n)


    # [2] Tampilkan isi file dengan print
    print(d)
    print(i)
    print(m)
    print(a)


# Panggil fungsi main
main()


# NOMOR 8
# Program ini membaca file kota.txt dan menampilkan isi file
# dengan format: Baris <n>: <isi_file_baris_ke_n>
def main():
    # [1] Tuliskan statement untuk membuka file kota.txt untuk dibaca dan tugaskan object file ke sebuah variabel
    with open('kota.txt', 'r') as dima:
        # [2] Tuliskan tiga statement untuk membaca tiga baris dari file kota.txt dan menyimpan isinya ke sebuah variabel
        d1 = dima.readline()
        d2 = dima.readline()
        d3 = dima.readline()

    # [4] Hilangkan karakter baris baru pada masing-masing isi baris
    dim1 = d1.rstrip('\n')
    dim2 = d2.rstrip('\n')
    dim3 = d3.rstrip('\n')
    # [3] Tampikan isi per baris dengan format: Baris <n>: <isi_file_baris_ke_n>
    print('Baris {}: {}'.format(1, dim1))
    print('Baris {}: {}'.format(2, dim2))
    print('Baris {}: {}'.format(3, dim3))


# Panggil fungsi main
main()

# 5.2
# nomor 1
# Program ini meminta pengguna memasukkan tiga buah angka float
# dan menuliskan keduanya, masing-masing dalam satu baris,
# ke file angka.txt
def main():
    # [1] Minta pengguna memasukkan tiga buah angka desimal
    # Gunakan prompt "Masukkan sebuah angka desimal: " untuk angka pertama
    # dan prompt "Masukkan sebuah angka desimal lainnya: " untuk angka kedua dan ketiga
    num1 = float(input('Masukkan sebuah angka desimal: '))
    num2 = float(input('Masukkan sebuah angka desimal lainnya: '))
    num3 = float(input('Masukkan sebuah angka desimal lainnya: '))

    # [2] Buka file angka.txt untuk ditulis dan tuliskan angka-angka yang didapat
    # dari pengguna ke file tersebut masing-masing dalam baris baru.
    x = open('angka.txt', 'w')
    x.write(str(num1) + '\n')
    x.write(str(num2) + '\n')
    x.write(str(num3) + '\n')

    # [3] Tampilkan pesan "Data telah berhasil disimpan dalam file angka.txt."
    x.close()
    print('Data telah berhasil disimpan dalam file angka.txt.')


# Panggil fungsi main
main()

# Nomor 2

# Program ini membaca isi file angka_float.txt
# dan mengalikan angka yang terdapat dalam file tersebut
def main():
    # [1] Buka file dengan statement with atau 3 langkah menggunakan file: buka, proses, tutup.
    # Lalu ambil angka pertama pada baris pertama dan angka kedua pada baris kedua, simpan
    # angka pada setiap baris isi file masing-masing ke sebuah variabel
    x = open('angka_float.txt', 'r')
    a = float(x.readline())
    b = float(x.readline())
    x.close()

    # [2] Hitung hasi kali dan tampikan sesuai dengan ketentuan program yang diminta
    total = a * b
    print(f'Baris 1 file angka_float.txt berisi: {a}')
    print(f'Baris 2 file angka_float.txt berisi: {b}')
    print(f'Hasil kali baris 1 dan baris 2 = {total:.2f}')


# Panggil fungsi main
main()

# 5.3
# NOMOR 1
# Program ini menuliskan angka 1 s.d 100
# ke file daftar_angka.txt

# [1] Import module random
import random


# Definisi fungsi main
def main():
    # [2] Tuliskan kode untuk membuka file daftar_angka.txt untuk ditulis
    # Generasi angka acak antara 1 s.d 100 sebanyak 100 angka dengan fungsi randint
    # dan tulis masing-masing angka ke masing-masing baris pada file daftar_angka.txt.
    x = open('daftar_angka.txt', 'w')
    for i in range(1, 101):
        x.write(str(i) + '\n')
    x.close()

# [3] Panggil fungsi main

# NOMOR 2
# Program ini menghitung rata-rata penjualan
# dengan data yang terdapat dalam file sales.txt
def main():
    # Ikuti petunjuk pada komentar di bawah.
    # Petunjuk pada kerangka program ini menggunakan 3 langkah menggunakan file: buka, proses, tutup.
    # Anda diperbolehkan menggunakan statement with, namun kode Anda akan sedikit berbeda dengan petunjuk di bawah

    # [1] Buat dua buah variabel: variabel penghitung baris untuk menghitung banyak baris (untuk digunakan sebagai banyak penjualan)
    # dan variabel akumulator untuk menghitung total penjualan
    a = 0.0
    b = 0.0

    # [2] Buka file sales.txt untuk dibaca dan simpan object file ke suatu variabel
    x = open('sales.txt', 'r')

    # [3] Baca baris pertama isi file dan simpan ke suatu variabel
    baris = x.readline()

    # [4] Tuliskan loop while untuk mengiterasi isi file setiap barisnya dan lakukan hal berikut pada setiap iterasi:
    # - akumulasikan isi_baris ke variabel akumulator (jangan lupa konversi ke tipe numerik)
    # - inkrementasi variabel penghitung baris
    while baris != '':
        a = a + float(baris)
        b = b + 1
        baris = x.readline()
        avg = a / b

    # [5] Hitung rata-rata dengan membagi total penjualan dan banyak penjualan (variabel akumulator / variabel penghitung baris)
    # dan tampilkan hasilnya.
    print(f'Rata-rata penjualan: {avg:,.2f}')


# Panggil fungsi main
main()

# NOMOR 3
# Program ini menghitung rata-rata penjualan
# dengan data yang terdapat dalam file sales.txt
def main():
    # Ikuti petunjuk pada komentar di bawah.
    # Petunjuk pada kerangka program ini menggunakan 3 langkah menggunakan file: buka, proses, tutup.
    # Anda diperbolehkan menggunakan statement with, namun kode Anda akan sedikit berbeda dengan petunjuk di bawah

    # [1] Buat dua buah variabel: variabel penghitung baris untuk menghitung banyak baris (untuk digunakan sebagai banyak penjualan)
    # dan variabel akumulator untuk menghitung total penjualan
    a = 0.0
    b = 0

    # [2] Buka file sales.txt untuk dibaca dan simpan object file ke suatu variabel
    x = open('sales.txt', 'r')

    # [3] Tuliskan loop for untuk mengiterasi isi file setiap barisnya dan lakukan hal berikut pada setiap iterasi:
    # - akumulasikan isi_baris ke variabel akumulator (jangan lupa konversi ke tipe numerik)
    # - inkrementasi variabel penghitung baris
    for baris in x:
        a = a + float(baris)
        b = b + 1
        avg = a / b

    # [4] Hitung rata-rata dengan membagi total penjualan dan banyak penjualan (variabel akumulator / variabel penghitung baris)
    # dan tampilkan hasilnya.
    print(f'Rata-rata penjualan: {avg:,.2f}')


# Panggil fungsi main
main()

# 5.4
# NOMOR 3
# Program ini menuliskan sebuah list ke file list_angka.txt
def main():
    angka = [234, 694, 123, 789, 923, 674, 534]

    # [1] Tuliskan kode untuk menuliskan list yang direferensikan oleh variabel angka
    # ke file list_angka.txt
    with open('list_angka.txt', 'w') as x:
        for a in angka:
            x.write(str(a) + '\n')


# Panggil fungsi main
main()

# NOMOR 4
# Program ini membaca file daftar_nilai.txt yang berisi data nilai ujian
# dari 30 mahasiswa dan mencari nilai rata-rata, nilai tertinggi, dan nilai terenda
def main():
    # Buat variabel untuk menyimpan hasil perhitungan dan inisialisasi dengan 0.0 (float)
    rata_rata = 0.0
    nilai_tertinggi = 0.0
    nilai_terendah = 0.0

    # [1] Tuliskan statement untuk membuka file daftar_nilai.txt untuk dibaca
    # dan simpan isinya ke sebuah list
    number_list = []

    # [2] Tuliskan struktur loop untuk menghapus karakter baris baru pada setiap elemen
    # dari list
    with open('daftar_nilai.txt', 'r') as fp:
        number_list = [float(item) for item in fp.readlines()]

    # [3] Cari nilai rata-rata, nilai tertinggi, dan terendah. Gunakan loop.
    nilai_terendah = min(number_list)
    nilai_tertinggi = max(number_list)
    rata_rata = sum(number_list) / len(number_list)
    x = "{:.2f}".format(rata_rata)

    # [4] Tampilkan rata-rata, nilai tertinggi, dan nilai terendah.
    print('Rata-rata nilai ujian: ', x)
    print('Nilai ujian tertinggi: ', nilai_tertinggi)
    print('Nilai ujian terendah: ', nilai_terendah)


# Panggil fungsi main()
main()

# 5.5
# Program ini menambahkan record nilai mahasiswa
# ke file nilai_mahasiswa.txt
def main():
    # [1] Minta pengguna berapa banyak record yang ingin dimasukkan
    x = int(input('Berapa banyak record nilai mahasiswa yang ingin Anda tambahkan? '))




    # [2] Buka file dengan statement with, minta input masing-masing record ke pengguna, dan tulis ke file
    # nilai_mahasiswa.txt
    with open('nilai_mahasiswa.txt', 'a') as nilai:
        for i in range(1, x +1):
            print(f'Masukkan record nilai mahasiswa ke {i}')
            nama = input('Nama: ')
            Nilai = input('Nilai: ')
            nilai.write(nama + '\n')
            nilai.write(Nilai + '\n')
            print()

# Panggil fungsi main
main()

# nomor 2
# Program ini membaca record nilai mahasiswa
# dari file nilai_mahasiswa.txt
def main():

    # [1] Buka file nilai_mahasiswa.txt dengan statement with untuk dibaca
    # Pada body statement with:
    # - Gunakan loop while untuk membaca field-field dari semua record
    # - Tampilkan record dengan tampilan:
    #           Nama: <nama_mahasiswa>
    #           Nilai: <nilai_mahasiswa>
    with open('nilai_mahasiswa.txt', 'r') as d:
        data = d.readline()
        while data !='':
            Nilai = d.readline()
            nama = data.rstrip('\n')
            nilai = Nilai.rstrip('\n')
            print(f'Nama: {nama}')
            print(f'Nilai: {nilai}')
            print()
            data = d.readline()


# Panggil fungsi main
main()

# 5.6
# Program ini meminta pengguna memasukkan dua angka untuk operasi pembagian
# Program menampilkan pesan jika terjadi eksepsi
def main():
    # [1] Tuliskan statement try/except
    # Pada body klausa try:
    #     - Minta dua angka ke pengguna
    #     - Lakukan pembagian
    # Pada body klausa except untuk ValueError
    #     - Tampilkan pesan: "Nilai yang diinput salah."
    # Pada body klausa except untuk ZeroDivisionError
    #     - Tampilkan pesan: "Tidak dapat membagi dengan nol."
    try:
        x = int(input('Masukkan sebuah angka yang akan dibagi: '))
        y = int(input('Masukkan sebuah angka pembagi: '))
        print(f'{x} dibagi dengan {y} sama dengan {x/y}')
    except ValueError:
        print('Nilai yang diinput salah.')
    except ZeroDivisionError:
        print('Tidak dapat membagi dengan nol.')


# Panggil fungsi main
main()

# Nomor 4
def main():
    # List untuk menyimpan isi file
    # [1] Tuliskan statement yang meminta pengguna memasukkan nama file dengan prompt: Masukkan nama file: "
    data = []
    d = input('Masukkan nama file: ')
    # [2] Tuliskan exception handler dengan statement try/except
    # Pada body klausa try: buka file, baca isinya, dan simpan isinya ke list_angka
    # Pada body klausa except untuk FileNoFoundError tampilkan pesan "File tidak ditemukan."
    # Pada body klausa except untuk ValueError tampilkan pesan "Terdapat data non numerik dalam file."
    # Pada body klausa else: Cari rata-rata, nilai tertinggi, nilai terenda dan tampilkan hasilnya

    try:
        dim = open(d, 'r')
        for i in dim:
            y = float(i)
            data.append(y)


    except FileNotFoundError:
        print('File tidak ditemukan.')
    except ValueError:
        print('Terdapat data non numerik dalam file.')
    else:
        print('Rata-rata nilai:', round(sum(data) / len(data), 2))
        print('Nilai tertinggi:', max(data))
        print('Nilai terendah:', min(data))


# Panggil fungsi main
main()