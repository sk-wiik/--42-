N = int(input("Введите количество элементов: "))
print("Введите элементы массива:")
original_array = []
for i in range(N):
    num = int(input(f"Элемент {i+1}: "))
    original_array.append(num)
positive_numbers = []
other_numbers = []
for num in original_array:
    if num > 0:
        positive_numbers.append(num)
    else:
        other_numbers.append(num)
print("\nИсходный массив:", original_array)
print("Второй массив (положительные числа):", positive_numbers)
print("Третий массив (остальные числа):", other_numbers)