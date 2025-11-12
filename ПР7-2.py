def triangle_area(side):
    """Вычисляет площадь равностороннего треугольника"""
    s = (side ** 2 * (3 ** 0.5)) / 4
    return s
print("Вычисление площади правильного шестиугольника")
a = float(input("Введите длину стороны шестиугольника: "))
one_triangle_s = triangle_area(a)
hexagon_s = 6 * one_triangle_s
print(f"Площадь одного треугольника: {one_triangle_s:.2f}")
print(f"Площадь шестиугольника: {hexagon_s:.2f}")