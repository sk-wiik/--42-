N = int(input("Введите количество элементов: "))
print("Введите элементы списка:")
numbers = []
for i in range(N):
    num = int(input(f"Элемент {i+1}: "))
    numbers.append(num)
min_element = numbers[0]
min_index = 0
for i in range(1, N):
    if numbers[i] < min_element:
        min_element = numbers[i]
        min_index = i
print(f"Минимальный элемент: {min_element}")
print(f"Индекс минимального элемента: {min_index}")