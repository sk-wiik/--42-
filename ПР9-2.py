def find_second_max():
    """
    Рекурсивная функция для нахождения второго по величине элемента
    Не принимает параметров и не использует глобальные переменные
    """
    num = int(input())
    
    if num == 0:
        return 0, 0 
    current_max, current_second = find_second_max()
    if num > current_max:
        return num, current_max
    elif num > current_second and num != current_max:
        return current_max, num
    else:
        return current_max, current_second
print("Введите последовательность натуральных чисел (завершите 0):")
max_num, second_max = find_second_max()
print(f"Второй по величине элемент: {second_max}")