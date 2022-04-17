# Ekspresi Boolean
# Soal No 1
a = 5
b = 4
print(b * 2 == a * b / 2)
# Soal No 4
print(89.0 == 89)
print()
# Struktur Seleksi
# Soal No 1
nilai = 145
if nilai >= 130:
    print('Bisa menaiki wahana')
# Soal No 2
a = 10
b = 5
if a > b:
    print("Nilai a lebih besar dari b")
# Soal No 3
nilai = int(input("Masukkan bilangan:"))
if (nilai % 2) == 0:
    print("Ini bilangan genap")
else:
    print("Ini bilangan ganjil")
# Soal No 4
"""
Tuliskan statement if di kotak jawaban yang menugaskan 20 ke variabel y dan menugaskan 40 ke variabel z jika x lebih 
besar dari 100.

Catatan. Hanya tuliskan statement if dalam kotak jawaban.
"""
# Jawab:
"""
if x > 100:
    y = 20
    z = 40"""

# Soal No5
def main():
    x = int(input("Masukkan banyak pembelian:"))
    harga = 990000
    a = harga*x*20/100
    b = harga*x*30/100
    c = harga*x*40/100
    d = harga*x*50/100
    total1 = harga *x - a
    total2 = harga *x - b
    total3 = harga *x - c
    total4 = harga *x - d
    if x >= 10 and x < 20:
        print(f'Diskon = Rp.{a:12,.2f}')
        print(f'Total = Rp.{total1:12,.2f}')
    elif x >= 20 and x < 50:
        print(f'Diskon = Rp.{b:12,.2f}')
        print(f'Total = Rp.{total2:12,.2f}')
    elif x >= 50 and x < 100:
        print(f'Diskon = Rp.{c:12,.2f}')
        print(f'Total = Rp.{total3:12,.2f}')
    elif x >= 100:
        print(f'Diskon = Rp.{d:12,.2f}')
        print(f'Total = Rp.{total4:12,.2f}')
    else:
        print(f'Total = Rp.{harga*x:12,.2f}')
main()
print()
# Operator Logis
# Soal No 2
a = 2
b = 4
c = 6
print(a == 4 or b > 2)
print(6 <= c and a > 3)
print(1 != b and c != 3)
print(a >= -1 or a <= b)
print(not (a > 2))
# Soal No 3
"""
Buat sebuah fungsi dengan nama cek_kecepatan yang menerima sebuah argumen berupa integer yang merepresentasikan 
kecepatan dari suatu kendaraan. Fungsi ini menguji apakah kecepatan berada di dalam rentang kecepatan 20 km/jam sampai 
dengan 60 km/jam. Jika argumen berada di dalam rentang, tampilkan pesan "Kecepatan normal", dan jika berada di luar 
rentang tampilkan pesan "Kecepatan tidak normal".
"""
# Jawab:
def cek_kecepatan(kecepatan):
    # Tuliskan kode Anda di bawah.
    if kecepatan >= 20 and kecepatan <= 60:
        print('Kecepatan normal')
    else:
        print('Kecepatan tidak normal')

# No 4
"""
Tuliskan sebuah program yang menghitung angka terbesar dari tiga angka yang dimasukkan pengguna. Program meminta tiga 
angka ke pengguna lalu menampilkan angka terbesar dari ketiga angka tersebut."""
# Jawab:
def main():
    angka1 = int(input("Masukkan angka 1: "))
    angka2 = int(input("Masukkan angka 2: "))
    angka3 = int(input("Masukkan angka 3: "))
    if angka1 > angka2 and angka1 > angka3:
        print("Angka terbesar = ", angka1)
    elif angka2 > angka1 and angka2 > angka3:
        print("Angka terbesar = ", angka2)
    elif angka3 > angka1 and angka3 > angka2:
        print("Angka terbesar = ", angka3)
    elif angka1 == angka2 or angka1 == angka3:
        print("Angka terbesar = ", angka3)
    elif angka2 == angka1 or angka2 == angka3:
        print("Angka terbesar = ", angka3)
    elif angka3 == angka1 or angka3 == angka2:
        print("Angka terbesar = ", angka3)
    else:
        print('Angka tidak dapat dihitung!')
main()
# Soal No 5
"""
MIsalkan sebuah bank memberikan pinjaman ke nasabahnya berdasarkan besar gaji dan lama kerja. Untuk terkualifikasi 
sebagai penerima pinjaman, nasabah harus memiliki minimum gaji Rp. 3.000.000,- dan minimum lama kerja 2 tahun. 
Tuliskan sebuah program yang meminta pengguna memasukkan gaji dan lama kerja lalu menampilkan apakah pengguna 
terkualifikasi untuk menerima pinjaman atau tidak."""
# Jawab:
def main():
    gaji = int(input("Masukkan gaji Anda: "))
    tahun = int(input("Lama bekerja (tahun): "))
    if gaji >= 3000000 and tahun >= 2:
        print("Anda terkualifikasi untuk menerima pinjaman!")
    else:
        print("Anda tidak terkualifikasi untuk menerima pinjaman!")
main()

print()
# Struktur Iterasi
# Soal No 3
"""
Lengkapi statement while di kotak jawaban sehingga menampilkan bilangan genap antara 2 s.d 100. """
# Jawab:
i = 0
while i < 100:
    i = i + 2
    print(i)
print()
# Soal No 4
"""
Lengkapi statement for di kotak jawaban sehingga menampilkan nilai kuadrat dari 1 sampai dengan 10.
"""
# Jawab:
for i in range(1, 11):
    print(i**2)
# Soal No 5
"""
Lengkapi statement loop for di kotak jawaban sehingga menampilkan barisan bilangan genap antara 2 dan 10 dengan urutan 
terbalik: 50,48,46,44,...,4,2."""
# Jawab:
for i in range(50, 0, -2):
    print(i)
print()
# Pola-Pola Loop
# Soal No 3
"""
Tuliskan sebuah program yang meminta pengguna memasukkan 10 angka integer satu per satu dan menghitung total jumlah 
angka yang dimasukkan."""
# Jawab:
maks = 10
def main():
    total = 0
    for counter in range (maks):
        num= int(input("Masukkan angka: "))
        total += num
    print('Total =',total)

main()
# Soal No 4
"""
Sentinel adalah karakter khusus yang digunakan untuk menandakan akhir dari rangkaian input.
Buat sebuah program yang menerapkan sentinel yang meminta pengguna berulang kali untuk memasukkan angka-angka integer 
positif sampai dengan pengguna memasukkan sebuah angka negatif. Setelah semua angka positif dimasukkan pengguna, 
program menampilkan rata-rata dari angka-angka yang dimasukkan pengguna.
"""
# Jawab:
# Program ini menghitung rata-rata dari rangkaian input yang dimasukkan pengguna
# Program ini menghitung rata-rata dari rangkaian input yang dimasukkan pengguna
def main():
    total = 0
    counter = 0
    rata = 0
    num = int(input('Masukkan angka positif (akhiri dengan memasukkan angka negatif): '))
    while num != -1:
        counter += 1
        total += int(num)
        rata = total / counter
        num = int(input('Masukkan angka positif (akhiri dengan memasukkan angka negatif): '))
    print('Rata-rata angka yang dimasukkan:', rata)


# Panggil fungsi main
main()

# Soal No 5
"""
Tuliskan program yang meminta pengguna memasukkan sebuah angka integer lalu menampilkan pola segitiga sikut terbalik.
 Misalkan pengguna memasukkan 5, maka program menampilkan pola segitiga berikut:"""
# Jawab:
def main():
    a = int(input('Masukkan sebuah angka: '))
    for i in range (0, a+1):
        for j in range(0, a):
            print('*', end= "")
        a -= 1
        print("")
main()

print()
# Lab Activity
# Soal No 1
"""
Tuliskan sebuah program yang meminta pengguna memasukkan jumlah detik, dan bekerja seperti berikut:

Terdapat 60 detik dalam 1 menit. Jika jumlah detik yang dimasukkan pengguna lebih besar atau sama dengan 60, program 
menampilkan jumlah menit dan detik dari jumlah detik yang dimasukkan. Misalkan pengguna memasukkan 80 detik maka program 
menampilkan: 1 menit 20 detik.
Terdapat 3600 detik dalam 1 jam. Jika jumlah detik yang dimasukkan pengguna lebih besar atau sama dengan 3600, program
menampilkan jumlah jam, menit, dan detik.
Terdapat 86400 detik dalam 1 hari. Jika jumlah detik yang dimasukkan pengguna lebih besar atau sama dengan 86400 program 
menampilkan jumlah hari, jam, menit, dan detik."""
# Jawab:
def main():
    dtk = int(input('Masukkan jumlah detik: '))
    if dtk >= 60 and dtk < 3600:
        menit = dtk // 60
        detik = dtk % 60
        print(f'{menit} menit {detik} detik')
    elif dtk >= 3600 and dtk < 86400:
        jam = dtk // 3600
        menit = (dtk % 3600 ) // 60
        detik = (dtk % 3600 ) % 60
        print(f'{jam} jam {menit} menit {detik} detik')
    elif dtk >= 86400:
        hari = dtk // 86400
        jam = (dtk % 86400) // 3600
        menit = ((dtk % 86400) % 3600 ) // 60
        detik = (((dtk % 86400) % 3600)  % 60)
        print(f'{hari} hari {jam} jam {menit} menit {detik} detik')
    else:
        print('')

main()

# Soal No 2
"""
Tuliskan sebuah program yang meminta pengguna memasukkan dua angka integer lalu menghitung jumlah kedua angka tersebut. 
Program kemudian menanyakan pengguna apakah ingin melanjutkan atau keluar (dengan meminta pengguna memasukkan karakter 
'y' untuk melanjutkan dan memasukkan karakter lain untuk keluar). Jika pengguna ingin melanjutkan (memasukkan 'y'), maka
 program kembali meminta pengguna memasukkan dua angka integer dan kemudian menghitung jumlahnya. Proses ini berulang 
 sampai pengguna memasukkan karakter selain 'y'.
"""
# Jawab:
def main():
    angka1 = int(input('Masukkan angka 1: '))
    angka2 = int(input('Masukkan angka 2: '))
    print('Jumlah =', angka1 + angka2)
    ulang()


def ulang():
    jika_ulang = input('Masukkan y untuk melanjutkan: ')
    if jika_ulang == 'y':
        main()
    elif jika_ulang == 'n' or 't':
        print('')
    else:
        ulang()
main()

