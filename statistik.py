import math
import statistics

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


def median(data):
    return statistics.median(data)
