def remainder(a, b):
    """
    Рекурсивная функция для вычисления остатка от деления a на b
    """
    if a < b:
        return a
    return remainder(a - b, b)
print("Вычисление остатка от деления")
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
result = remainder(a, b)
print(f"Остаток от деления {a} на {b} = {result}")