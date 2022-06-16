import pet

kitty = pet.Pet('Kitty', 'Kucing', '3')
print('Nama:', kitty.get_nama())
print('Jenis:', kitty.get_jenis())
print('Umur (tahun):', kitty.get_umur())
print()
print('Set nama, jenis, dan umur berbeda.')
kitty.set_nama('Zara')
kitty.set_jenis('Kucing Persia')
kitty.set_umur('4')
print('Nama:', kitty.get_nama())
print('Jenis:', kitty.get_jenis())
print('Umur (tahun):', kitty.get_umur())