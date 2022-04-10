# PRELAB 2.2 input

# Soal No.4
"""
ujian = int(input('Masukkan nilai ujian:'))"""
# Soal No. 5
"""Tuliskan tiga statement yang meminta pengguna memasukkan angka sebanyak tiga kali dan menyimpannya dengan tipe data 
integer.
Gunakan urutan prompt dan nama variabel berikut:

Nilai pertama yang dimasukkan pengguna dengan prompt 'Masukkan nilai ujian 1: ' ditugaskan ke variabel ujian1.
Nilai kedua yang dimasukkan pengguna dengan prompt 'Masukkan nilai ujian 2: ' ditugaskan ke variabel ujian2.
Nilai ketiga yang dimasukkan pengguna dengan prompt 'Masukkan nilai ujian 3: ' ditugaskan ke variabel ujian3.
Statement-statement Anda jika dijalankan harus menampilkan prompt seperti berikut (nilai setelah prompt adalah nilai 
yang dimasukkan pengguna):
Masukkan nilai ujian 1: 67
Masukkan nilai ujian 2: 77
Masukkan nilai ujian 3: 87
"""
"""
ujian1 = int(input('Masukkan nilai ujian 1:'))
ujian2 = int(input('Masukkan nilai ujian 2:'))
ujian3 = int(input('Masukkan nilai ujian 3:'))"""

# PRELAB 2.3 Output
# Soal No. 1
# Apa yang ditampilkan oleh statement berikut?
print('Budi', 'Susi', 'Jodi', 'Dodi', sep='@')
# Jawab: Budi@Susi@Jodi@Dodi
# Soal No. 3
# Tuliskan statement yang menampilkan teks seperti berikut:
# Gunakan path: C:\temp\data.
print('Gunakan path: C:\\temp\\data.')
# Soal No. 4
"""Misalkan terdapat potongan kode seperti berikut:
stok = 2014
harga_satuan = 10500
Tambahkan statement yang menampilkan teks seperti berikut:
Terdapat stok buah sebanyak 2,014 dengan harga satuan Rp. 10,500.00.
Petunjuk:
Gunakan fungsi print dengan f-string
Gunakan format specifier untuk memisahkan ribuan dan dua angka desimal
Catatan. Untuk mendapatkan nilai Anda harus menggunakan variabel-variabel pada potongan kode di atas"""
# Jawab:
stok = 2014
harga_satuan = 10500
print(f'Terdapat stok buah sebanyak {stok:4,} dengan harga satuan Rp. {harga_satuan:9,.2f}.')
# Soal No. 5
"""Misalkan terdapat potongan kode seperti berikut:
str1 = 'Universitas'
str2 = 'Gunadarma'
Tambahkan statement yang menampilkan teks seperti berikut:
Universitas*Gunadarma
Petunjuk:
Gunakan fungsi print
Gunakan keyword argument sep pada fungsi print
Catatan. Untuk mendapatkan nilai Anda harus menggunakan variabel str1 dan str2 dalam statement Anda."""
# Jawab:
str1 = 'Universitas'
str2 = 'Gunadarma'
print(str1, str2, sep='*')

