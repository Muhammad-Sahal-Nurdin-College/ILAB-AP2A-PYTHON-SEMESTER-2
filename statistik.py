import math

# Fungsi mean(data)
""" Fungsi mean(data): menerima sebuah argumen bertipe list dan mengembalikan rata-rata dari nilai-nilai pada list 
    tersebut.
"""


def mean(data):
    return sum(data)/len(data)


# Fungsi var(data)
""" Fungsi var(data): menerima sebuah argumen bertipe list dan mengembalikan variansi dari nilai-nilai pada list 
    tersebut. 
"""


def var(data):
    avg = sum(data) / len(data)
    return sum((x - avg) ** 2 for x in data) / len(data)


# Fungsi std(data)
""" Fungsi std(data): menerima sebuah argumen bertipe list dan mengembalikan standard deviasi (simpangan baku) 
    dari nilai-nilai pada list tersebut. Standard deviasi adalah akar kuadrat dari variansi:
"""


def std(data):
    avg = sum(data) / len(data)
    return math.sqrt(sum((x - avg) ** 2 for x in data) / len(data))


# Fungsi median(data)
""" Fungsi median(data): menerima sebuah argumen bertipe list dan mengembalikan median dari nilai-nilai pada list 
    tersebut.
"""


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


def median(data):
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
