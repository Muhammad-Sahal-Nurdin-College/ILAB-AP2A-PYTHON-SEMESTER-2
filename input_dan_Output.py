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
"""
stok = 2014
harga_satuan = 10500
print(f'Terdapat stok buah sebanyak {stok:4,} dengan harga satuan Rp. {harga_satuan:9,.2f}.')"""
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
"""
str1 = 'Universitas'
str2 = 'Gunadarma'
print(str1, str2, sep='*')
"""
# PRELAB 2.4 Menulis Program
"""Buat sebuah program yang menghitung rata-rata dari nilai tiga ujian. 
Program tersebut meminta pengguna memasukkan tiga nilai ujian, menghitung rata-rata dari ketiga ujian tersebut, dan 
menampilkan rata-rata tersebut ke layar.
Gunakan prompt berikut untuk meminta tiga nilai ujian:
Prompt untuk ujian pertama: 'Masukkan nilai ujian 1: '
Prompt untuk ujian kedua: 'Masukkan nilai ujian 2: '
Prompt untuk ujian ketiga: 'Masukkan nilai ujian 3: ' 
Asumsikan nilai yang dimasukkan bertipe floating point.
Tampilan rata-rata dari ketiga ujian haruslah seperti berikut:
Rata-rata nilai ujian: <rata-rata>."""
# Jawab:
"""
print()
ujian1 = int(input('Masukkan nilai ujian 1: '))
ujian2 = int(input('Masukkan nilai ujian 2: '))
ujian3 = int(input('Masukkan nilai ujian 3: '))
rata_rata = (ujian1 + ujian2 + ujian3)/3
print(f'Rata-rata nilai ujian: {rata_rata:.2f}')
"""
# Soal No. 2
"""Buat sebuah program yang meminta pengguna untuk memasukkan total pembelian. Program tersebut lalu menghitung Pajak 
PPN dan Service Charge. Asumsikan Pajak PPN sebesar 10% dan Service Charge sebesar 5%. Program kemudian menampilkan 
total pembelian, PPN yang harus dibayar, Service Charge yang harus dibayar, dan total yang harus dibayar 
(yang dihitung dari penjumlahan total pembelian ditambah PPN yang harus dibayar dan Service Charge yang harus dibayar)

Gunakan prompt: 'Masukkan total pembelian: ' untuk meminta jumlah total penjualan dalam setahun dan asumsikan angka 
yang dimasukkan pengguna berbentuk integer.

Tampilan program haruslah seperti berikut (misalkan pengguna memasukkan total pembelian 1000000):

Total Pembelian: Rp 1,000,000.00
PPN (10%): Rp 100,000.00
Service Charge (5%): Rp 50,000.00
Total yang harus dibayarkan: Rp 1,150,000.00
Petunjuk:

Gunakan nilai 0.1 untuk merepresentasikan 10% dan nilai 0.05 untuk merepresentasikan 5%.
Gunakan format specifier untuk menampilkan pemisah ribuan dan dua angka nilai desimal.
Contoh tampilan program dapat dilihat pada tabel di bawah.
"""
# Jawab:
"""
print()
total_Pembelian = int(input('Masukkan total pembelian: '))
print(f'Total Pembelian: Rp {total_Pembelian:,.2f}')
PPN = total_Pembelian * 0.1
print(f'PPN (10%): Rp {PPN:,.2f}')
service_Charge = total_Pembelian * 0.05
print(f'Service Charge (5%): Rp {service_Charge:,.2f}')
total_bayar = total_Pembelian + PPN + service_Charge
print(f'Total yang harus dibayarkan: Rp {total_bayar:,.2f}')
"""
# Soal No.3
"""Buat sebuah program yang meminta pengguna memasukkan panjang dan lebar (dalam cm), 
hitung luas dan keliling persegi panjang dari panjang dan lebar tersebut, lalu tampilkan luas dan keliling tersebut. 
Asumsikan panjang dan lebar dalam bilangan bulat (integer).

Program Anda harus menggunakan prompt seperti berikut:

Prompt untuk meminta panjang: 'Masukkan panjang (cm): '
Prompt untuk meminta lebar: 'Masukkan lebar (cm): '
Teks yang menampilkan luas dan keliling haruslah seperti berikut:

Persegi panjang dengan panjang = <panjang> cm dan lebar = <lebar> cm mempunyai luas = <luas> cm2 dan keliling = cm.

Catatan. Perhatikan spasi setelah titik dua pada prompt.

Contoh tampilan program dapat dilihat pada tabel di bawah."""
# Jawab:
"""
print()
p = int(input('Masukkan panjang (cm): '))
l = int(input('Masukkan lebar (cm): '))
luas = p*l
keliling = 2*(p+l)
print('Persegi panjang dengan panjang =', p, 'cm dan lebar =', l, 'cm mempunyai luas =', luas, 'cm2 dan keliling =', keliling, 'cm.')
"""

# Soal No. 4
"""Tuliskan sebuah program yang mengkonversi waktu dalam detik yang dimasukkan pengguna ke jumlah jam, jumlah menit, dan 
jumlah detik. Misalkan pengguna memasukkan 3740, program tersebut menampilkan:

Jam: 1
Menit: 2
Detik: 20
Petunjuk:

Gunakan prompt: 'Masukkan waktu dalam detik: ' untuk meminta waktu dalam detik ke pengguna.
Gunakan operator floor division ( // ) dan operator modulus ( % ) untuk menghitung jam, menit, dan detik.
"""
# Jawab:
dtk = int(input('Masukkan waktu dalam detik: '))
jam = dtk//3600
Menit = (dtk % 3600) // 60
Detik = (dtk % 3600) % 60
print('Berikut waktu dalam jam, menit, dan detik:')
print('Jam:', jam)
print('Menit:', Menit)
print('Detik:', Detik)

# Soal No.5
"""
Sebuah toko memprediksi keuntungan tokonya dalam satu tahun adalah 23% dari total penjualan setahun. Tuliskan sebuah 
program yang meminta pengguna memasukkan jumlah total penjualan dalam setahun, lalu tampilkan prediksi keuntungan yang 
didapatkan dari total penjualan tersebut.

Gunakan prompt: 'Masukkan total penjualan tahun ini: ' untuk meminta jumlah total penjualan dalam setahun.

Tampilan keuntungan haruslah seperti berikut (misalkan keuntungan sebesar 2,500,000):

Keuntungan tahun ini adalah Rp. 2,500,000.00
Catatan. Perhatikan spasi setelah titik dua pada prompt.

Petunjuk:

Gunakan nilai 0.23 untuk merepresentasikan 23%.
Gunakan format specifier untuk menampilkan keuntungan dalam rupiah."""
# Jawab:
total_Penjualan = int(input('Masukkan total penjualan tahun ini: '))
prediksi = total_Penjualan * 0.23
print(f'Keuntungan tahun ini adalah Rp. {prediksi:,.2f}')

