n = 3
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    a.append(b)
print("Исходная матрица:")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(n):
    temp = a[i][0]
    a[i][0] = a[i][n-1]
    a[i][n-1] = temp
print("Матрица после перестановки:")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()