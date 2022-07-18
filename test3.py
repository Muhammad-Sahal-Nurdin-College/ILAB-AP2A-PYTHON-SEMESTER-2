x = int(input('masukkan bilangan:'))
x = x % 2 == 0 or x % 3 == 0 and x % 2 == 1 and x % 3 == 1 and (x % 2 == 1 and x % 3 == 0)
print (x)

