# Program ini mendemonstrasikan class Sedan, Pickup, dan SUV import kendaraan
def main():
    # Buat object Sedan
    sedan = kendaraan.Sedan('BMW', '323', 500000000, 4)
    # Buat object Pickup
    pickup = kendaraan.Pickup('Toyota', 'Hilux', 350000000, '4WD')
    # Buat object SUV
    suv = kendaraan.SUV('Hyundai', 'Santa Fe', 550000000, 6)
    print('Data Kendaraan')    print('=================')
    # Tampilkan data Sedan
    print('Merek:', sedan.get_merek())
    print('Model:', sedan.get_model())
    print('Jumlah Pintu:', sedan.get_pintu())
    print()
    # Tampilkan data Pickup
    print('Merek:', pickup.get_merek())
    print('Model:', pickup.get_model())
    print(f'Harga: Rp.{pickup.get_harga(): ,.2f}')
    print('Tipe Penggerak:', pickup.get_tipe_penggerak())
    print()    
    # Tampilkan data SUV
    print('Merek:', suv.get_merek())
    print('Model:', suv.get_model())
    print(f'Harga: Rp.{suv.get_harga(): ,.2f}')
    print('Kapasitas Penumpang:', suv.get_kap_penumpang())
    print()
# Panggil fungsi main
main()