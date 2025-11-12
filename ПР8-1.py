n = 3
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
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
if magic:
    print('Матрица является магическим квадратом')
else:
    print('Матрица не является магическим квадратом')