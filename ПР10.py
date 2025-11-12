with open('СтоянцевНикита_УБ-42_vvod.txt', 'r') as file:
    n = int(file.readline().strip())
    a = []
    for i in range(n):
        line = file.readline().strip().split()
        b = []
        for j in range(n):
            b.append(int(line[j]))
        a.append(b)
print("Матрица:")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
summa = 0
for j in range(n):
    summa = summa + a[0][j]

magic = True
for i in range(n):
    temp = 0
    for j in range(n):
        temp = temp + a[i][j]
    if temp != summa:
        magic = False
        break
if magic:
    for j in range(n):
        temp = 0
        for i in range(n):
            temp = temp + a[i][j]
        if temp != summa:
            magic = False
            break
with open('СтоянцевНикита_УБ-42_vivod.txt', 'w') as file:
    file.write("Матрица:\n")
    for i in range(n):
        for j in range(n):
            file.write(str(a[i][j]) + ' ')
        file.write('\n')
    if magic:
        file.write('Матрица является магическим квадратом\n')
        file.write(f'Магическая сумма: {summa}')
    else:
        file.write('Матрица не является магическим квадратом')

print("Результат записан в файл")