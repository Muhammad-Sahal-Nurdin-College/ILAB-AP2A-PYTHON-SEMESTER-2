# Soal nomor 2
# Fungsi ini mengalikan x dan y secara rekursif
def kali(x, y):
    # [1] Base Case

    # [2] Recursive Case
    return x if y == 1 else x + kali(x, y - 1)

# Soal nomor 4
# Fungsi ini mencari nilai maksimum dari sebuah list secara rekursif
def maksimum_rekursif(data):
    # Tuliskan kode Anda di bawah.
    if len(data) == 1:
        return data[0]
    else:
        s = maksimum_rekursif(data[1:])
        if s > data[0]:
            return s
        else:
            return data[0]
    # [1] Gunakan statement if bersarang untuk mencari nilai maksimum
    # [2] Statement if bagian pertama memastikan jumlah data ada lebih dari 1 elemen
    # [3] Statement if bagian kedua (didalam if bagian pertama) menentukan apakah
    # elemen pertama list lebih besar dari elemen lainnya


# Pencarian data
# Fungsi binary search rekursif menerapkan
# algoritma binary search secara rekursif
def binary_search_rekursif(num, data):
    # [1] Base Cases
    # Jika data kosong (panjang = 0) tidak ada yang bisa dicari
    # kembalikan -1
    low = 0
    high = len(data) - 1

    # [2] Recursive Cases
    while low <= high:
        mid = (low + high) // 2
        if num == data[mid]:
            return mid
        elif num < data[mid]:
            high = mid - 1
        else:
            low = mid - 1
            return -1
    # Jika data tidak kosong, dapatkan indeks tengah dari data
    # Struktur seleksi:
    # 1. Jika elemen tengah sama dengan num kembalikan indeks tengah
    # 2. Jika elemen tengah lebih besar, lakukan pemanggilan rekursif terhadap paruh atas data
    # 3. Jika elemen tengah lebih kecil, lakukan pemanggilan rekursif terhadap paruh bawah data

# Penyortiran data
# Selection Sort
# selection_sort.py
# Program ini mendemonstrasikan selection sort
# Fungsi yang mencari indeks minimun dari data dalam list


def indeks_minimum(data):
    indeks_min = 0
    min = data[indeks_min]
    for indeks in range(1, len(data)):
        if data[indeks] <= min:
            indeks_min = indeks
            min = data[indeks_min]
    return indeks_min

# Fungsi yang mengimplementasikan algoritma selection sort


def selection_sort(data):
    data_tersortir = []
    for i in range(len(data)):
        indeks_min = indeks_minimum(data)
        data_tersortir.append(data[indeks_min])
        data.pop(indeks_min)
        return data_tersortir
# Fungsi main untuk menguji selection sort


def main():
    data = [35, 73, 90, 65, 23, 86, 43, 81, 34, 58]
    data_tersortir = selection_sort(data)
    print(data_tersortir)
main()

# Penyortiran quicksort
# Quicksort


def quicksort(list):
    # Base Cases
    if len(list) < 2:
        return list
    # Recursive Cases
    else:
        pivot = list[0]
        lebih_kecil = []
        lebih_besar = []
        # Buat list dengan elemen-elemen <= Pivot
        # dan list dengan elemen-elemen > pivot
        for elm in list[1:]:
            if elm <= pivot:
                lebih_kecil.append(elm)
            else:
                lebih_besar.append(elm)
        return quicksort(lebih_kecil) + [pivot] + quicksort(lebih_besar)


def main():
    data = [35, 73, 90, 65, 23, 86, 43, 81, 34, 58]
    data_tersortir = quicksort(data)
    print(data_tersortir)
main()


# Soal Nomor 2
# Fungsi bantu untuk mencari indeks dari nilai minimum dalam data
# Fungsi ini mengembalikan indeks nilai minimum dari data
def indeks_minimum(data):
    # [1] Tuliskan kode untuk mencari indeks nilai minimum
    # dan kembalikan indeks tersebut.
    indeks_min = 0
    min1 = data[indeks_min]
    for indeks in range(1, len(data)):
        if data[indeks] <= min1:
            indeks_min = indeks
            min1 = data[indeks_min]
    return indeks_min


# Fungsi penyortiran seleksi secara rekursif
def selection_sort_rekursif(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        lebih_kecil = []
        lebih_besar = []
        for elm in data[1:]:
            if elm <= pivot:
                lebih_kecil.append(elm)
            else:
                lebih_besar.append(elm)
        return selection_sort_rekursif(lebih_kecil) + [pivot] + selection_sort_rekursif(lebih_besar)


def main():
    data = [97, 23, 45, 88, 12, 76]
    data_tersortir = selection_sort_rekursif(data)


main()

# [2] Base Case: Data kosong atau hanya mempunyai satu elemen
# Tidak perlu sortir, kembalikan data apa adanya

# [3] Recursive Case: Data dengan dua atau lebih elemen
# Cari indeks nilai minimum dan dapatkan nilai minimum
# Konkatenasi list berisi nilai minimum dengan list berisi data dengan nilai minimum dihilangkan



# Nomor 1
# Fungsi sortir menerima argumen list dan
# mengembalikan list yang tersortir
def sortir(data):
    # [1] Tuliskan kode algoritma penyortiran di bawah
    # Base Cases
    if len(data) < 2:
        return data
    # Recursive Cases
    else:
        pivot = data[0]
        lebih_kecil = []
        lebih_besar = []
        # Buat list dengan elemen-elemen <= Pivot
        # dan list dengan elemen-elemen > pivot
        for elm in data[1:]:
            if elm <= pivot:
                lebih_kecil.append(elm)
            else:
                lebih_besar.append(elm)
        return sortir(lebih_kecil) + [pivot] + sortir(lebih_besar)

# Fungsi median menerima argumen sebuah list
# dan mengembalikan nilai median dari data dalam list tersebut


def median(data):
    # [2] Gunakan fungsi sortir untuk menyortir data
    sortir(data)
    # [3] Hitung median dengan dua kondisi untuk jumlah data genap dan jumlah data ganjil
    # lalu kembalikan nilai median
    if len(data) % 2 != 0:
        # total number of values are odd
        # subtract 1 since indexing starts at 0
        m = int((len(data) + 1) / 2 - 1)
        return data[m]
    else:
        m1 = int(len(data) / 2 - 1)
        m2 = int(len(data) / 2)
        return (data[m1] + data[m2]) / 2

# Module

# [1] import module yang Anda tulis



# Fungsi main menguji module
def main():

# [2] Minta pengguna untuk memasukkan alas dan tinggi


# [3] Hitung luas dan keliling dengan menggunakan fungsi pada module


# [4] Tampilkan luas dan keliling dengan presisi 2 desimal


# Panggil fungsi main


