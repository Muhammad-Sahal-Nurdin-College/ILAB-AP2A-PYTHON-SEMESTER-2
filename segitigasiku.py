import math
# segitigasiku.py
# Module segitigasiku berisi fungsi-fungsi yang melakukan
# kalkulasi terkait persegipanjang

# Fungsi luas menerima alas dan tinggi sebagai argumen
# dan mengembalikan luas persegi panjang


def luas(alas, tinggi):
    return (alas * tinggi)/2


# Fungsi keliling menerima alas dan tinggi sebagai argumen
# dan mengembalikan keliling persegi panjang


def keliling(alas, tinggi):
    sisimiring = math.sqrt(pow(alas, 2) + pow(tinggi, 2))
    return alas + tinggi + sisimiring
