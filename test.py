import statistik



def main():
    data = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]
    num1 = statistik.mean(data)
    print(f'Mean dari data:{num1:.2f}')
    num2 = statistik.var(data)
    print(f'Variansi dari data:{num2:.2f}')
    num3 = statistik.std(data)
    print(f'Standar Deviasi dari data:{ num3:.2f}')
    num4 = statistik.median(data)
    print(f'Median dari data:{num4:.2f}')

main()


