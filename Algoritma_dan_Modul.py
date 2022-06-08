# Soal nomor 2
# Fungsi ini mengalikan x dan y secara rekursif
def kali(x, y):
    # [1] Base Case

    # [2] Recursive Case
    return x if y == 1 else x + kali(x, y - 1)

# Soal nomor 2
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




