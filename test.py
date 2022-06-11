import statistik


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num1 = statistik.mean(data)
    print(f'Mean dari data:{num1:.2f}')
    num2 = statistik.var(data)
    print(f'Variansi dari data:{num2:.2f}')
    num3 = statistik.std(data)
    print(f'Standar Deviasi dari data:{ num3:.2f}')
    num4 = statistik.median(data)
    print(f'Median dari data:{num4:.2f}')

main()


