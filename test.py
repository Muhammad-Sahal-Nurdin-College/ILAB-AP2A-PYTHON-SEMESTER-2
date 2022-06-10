# test
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


print(median([1, 3, 3, 6, 7, 8, 9]))
print(median([1, 2, 3, 4, 5, 6, 8, 9]))






