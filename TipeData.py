# 4.2
buah = ['apel', 'anggur', 'mangga', 'jeruk']
print(buah[2])

angka = [1, 2, 3, 4, 5, 6, 7, 8]
print(angka[2])
print(angka[1:3])
print(angka[5:])
print(angka[-4:])
print(angka[::2])


nama = ['Budi', 'Johan', 'Wati', 'Anisa', 'Joko']
print(len(nama))

angka = [1, 2, 3, 4, 5]
angka[0] = 99
print(angka)

ids = [4353, 2314, 2956, 3382, 9362, 3900]
ids.append(5566)
print(ids)

ids2 = [4353, 2314, 2956, 3382, 9362, 3900]
ids2.insert(5, 4499)
print(ids2)

my_tuple = ('apel', 'mangga', 'jambu')
my_list = list(my_tuple)
print(my_list)


def main():
    nama_mhs = ('Budi', 'Dodi', 'Cindi', 'Kiki', 'Beti')
    # Tuliskan kode Anda di bawah.
    print(nama_mhs[0])
    print(nama_mhs[1])
    print(nama_mhs[2])
    print(nama_mhs[3])
    print(nama_mhs[4])


# Panggil fungsi main
main()


# Fungsi ini menerima sebuah list dan mengembalikan
# list baru yang elemen-elemennya adalah nilai kuadrat dari elemen-elemen list argumen
def kuadrat_list(input_list):
    # Tuliskan kode Anda di bawah.
    # List kosong untuk list yang dikembalikan
    output_list = []

    # [1] Tuliskan struktur loop yang mengiterasi input_list dan menambahkan elemen yang telah dikuadratkan ke output_list
    # Gunakan method append untuk menambahkan elemen ke list
    for i in input_list:
        output_list.append(i * i)

    # Kembalikan sebuah list yang elemen-elemennya adalah kuadrat dari elemen-elemen input_list
    return output_list


def jumlah_list(input_list):
    # Tuliskan kode Anda di bawah.
    # [1] Buat dua variabel akumulator untuk menyimpan jumlah elemen-elemen genap dan jumlah elemen-elemen ganjil
    total_ganjil = 0
    total_genap = 0
    b=[]

    # [2] Gunakan struktur loop untuk mengiterasi indeks dari input_list
    # Gunakan juga struktur seleksi dengan modulus untuk menguji indeks genap dan ganjil dan akumulasikan
    # elemen dengan indeks tersebut ke variabel akumulator yang sesuai
    for i in input_list:
        b.append(i)
        total_ganjil = int(sum(b[1::2]))
        total_genap = int(sum(b[::2]))
    # [3] Tampilkan jumlah elemen-elemen tersebut dengan teks:
    # "Total elemen indeks ganjil: <total_ganjil>"
    # "Total elemen indeks genap: <total_genap>"
    print('Total elemen indeks ganjil: ', total_ganjil)
    print('Total elemen indeks genap: ', total_genap)


"""my_string = 'Hello world!'
my_string[15]
print(my_string[15])"""

mystr = 'yes'
mystr += 'no'
mystr += 'yes'
print(mystr)


# Fungsi ini menghitung banyaknya huruf besar dari argumen yang diberikan dan mengembalikan
# jumlah huruf besar.
def banyak_huruf_besar(input_string):
    # [1] Buat sebuah variabel penghitung yang digunakan untuk menghitung banyak_huruf_besar dan inisialisasi dengan 0
    x = 0

    # [2] Tuliskan loop yang mengiterasi karakter-karakter dalam input_string dan uji apakah karakter tersebut adalah
    # huruf besar
    # dengan method isupper(). Jika ya, inkrementasi variabel penghitung.
    penghitung = sum(1 for  penghitung in input_string if  penghitung.isupper())

    # [3] Kembalikan variabel penghitung
    return penghitung


# Fungsi in melakukan validasi password
def validasi_password(passwd):
    spesial_karakter = ['$', '@', '#', '%']

    # Variabel-variabel untuk menyimpan hasil pengujian ketentuan. Inisialisasi dengan False.
    panjang_benar = False
    ada_digit = False
    ada_huruf_besar = False
    ada_huruf_kecil = False
    ada_spesial_karakter = False

    # [1] Mulai validasi dengan uji panjang karakter
    # Untuk menguji adanya digit, huruf besar, huruf kecil, dan spesial karakter, gunakan loop yang mengiterasi passwd
    if len(passwd) >= 6 and len(passwd) <= 20:
        for i in passwd:
            if i in spesial_karakter:
                ada_spesial_karakter = True
            elif i.isnumeric():
                ada_digit = True
            elif i.isupper():
                ada_huruf_besar = True
            elif i.islower():
                ada_huruf_kecil = True
            else:
                return False

    # [2] Jika semua ketentuan terpenuhi tetapkan sebuah varibel untuk nilai kembali dengan True
    # dan selain itu tetapkan dengan False
    else:
        return False

    # [3] Kembalikan variabel nilai kembali yang didapatrkan dari [2]
    return ada_spesial_karakter and ada_digit and ada_huruf_besar and ada_huruf_kecil

# Program ini menghitung jumlah digit-digit dari angka yang dimasukkan pengguna
def main():
    # [1] Minta input ke pengguna
    a = str(input('Masukkan sebuah angka: '))
    # [2] Buat sebuah variabel akumulator
    b = 0
    # [3] Iterasi karakter-karakter (digit-digit) dalam string angka yang dimasukkan pengguna
    # dan konversi ke integer untuk mendapatkan representasi integer dari digit
    for i in str(a):
        b += int(i)
    # [4] Tampilkan jumlah digit dengan teks: "Jumlah digit-digit dari <input_angka_pengguna> = <jumlah_digit>"
    print(f'Jumlah digit-digit dari {a} =', b)
# Panggil fungsi main
main()


# Program ini mencari karakter yang terbanyak muncul dalam input
def main():
    # Variabel untuk menyimpan karakter-karakter yang terdapat dapat string yang diinput pengguna
    karakter_list = []
    # Variabel untuk menyimpan banyaknya karakter yang terdapat dalam string yang diinput pengguna
    banyak_karakter = []

    # Catatan untuk dua variabel di atas:
    # Misalkan pengguna memasukkan 'ada', maka
    # karakter_list akan berisi ['a', 'd']
    # banyak_karakter akan berisi [2, 1]
    # Yang berarti terdapat 'a' sebanyak 2 dan terdapat 'd' sebanyak 1

    # [1] Minta pengguna masukkan sebuah teks dengan prompt 'Masukkan sebuah teks: ' dan simpan dalam sebuah variabel
    s = input('Masukkan sebuah teks: ')

    # [2] Gunakan method lower untuk konversi semua karakter ke huruf kecil. Karena string immutable, Anda harus menugaskan
    # kembali nilai kembali method ke variabel pada [1]
    m = s.lower()

    # [3] Gunakan struktur loop untuk mengterasi string input mulai dari indeks 0 sampai dengan terakhir.
    # Di dalam loop ini juga terdapat loop yang mengiterasi karakter_list dan menguji masing-masing karakter dalam karakter_list dengan
    # karakter dari input_string
    for j in m:
        for i in m:
            i = m[0]

    # [4] Cari jumlah terbanyak pada banyak_karakter dan simpan indeksnya
    print('Karakter terbanyak: ', i)

    # [5] Tampilkan karakter terbanyak. Gunakan indeks yang didapat pada [4]
    print()


# Panggil fungsi main
main()


# Program ini memroses nilai tiga ujian dari mahasiswa dalam sebuah kelas
# Program meminta pengguna memasukkan jumlah mahasiswa, meminta pengguna memasukkan
# nilai-nilai tiga ujian setiap mahasiswa, dan menampilkan rata-rata dari tiga nilai ujian dari setiap mahasiswa
def main():
    # Variabel JUMLAH_UJIAN
    JUMLAH_UJIAN = 3
    # Variabel untuk menyimpan nilai-nilai ujian
    nilai_ujian = []

    # Tuliskan kode Anda di bawah
    # [1] Minta pengguna memasukkan jumlah mahasiswa
    jml = int(input('Masukkan jumlah mahasiswa: '))
    print('=' * 50)

    # [2] Gunakan nested loop untuk meminta pengguna memasukkan tiga nilai ujian dari masing-masing mahasiswa
    for i in range(jml):
        total = 0.0
        print(f'Masukkan nilai ujian untuk mahasiswa {i + 1}')
        print('-' * 50)
        for i in range(JUMLAH_UJIAN):
            nilai = float(input(f'Masukkan nilai ujian ke-{i + 1}: '))
            total += nilai
        nilai_ujian.append(total / JUMLAH_UJIAN):
        print('=' * 50)

    # [3] Gunakan nested loop untuk menghitung dan menampilkan rata-rata nilai ujian
    for i in range(len(nilai_ujian)):
        print(f'Rata-rata ujian mahasiswa {i + 1}: {nilai_ujian[i]:,.2f}')


# Panggil fungsi main
main()
