import argparse
import math

def get_coefficient(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Некорректное значение. Пожалуйста, введите число.")

def solve_biquadratic(a, b, c):
    if a == 0:
        print("Коэффициент A не может быть равен нулю для биквадратного уравнения.")
        return

    print(f"Решаем уравнение: {a}x^4 + {b}x^2 + {c} = 0")
    # Решаем квадратное уравнение At^2 + Bt + C = 0
    discriminant = b**2 - 4 * a * c
    print(f"Дискриминант (D) = {discriminant}")

    if discriminant < 0:
        print("Действительных корней нет.")
        return

    # Вычисляем корни t
    t1 = (-b + math.sqrt(discriminant)) / (2 * a) if discriminant >= 0 else None
    t2 = (-b - math.sqrt(discriminant)) / (2 * a) if discriminant >= 0 else None

    roots = []
    for t in (t1, t2):
        if t is not None and t >= 0:
            roots.append(math.sqrt(t))  # x = sqrt(t)
            roots.append(-math.sqrt(t))  # x = -sqrt(t)

    if roots:
        print(f"Действительные корни уравнения: {sorted(roots)}")
    else:
        print("Действительных корней нет.")

def main():
    parser = argparse.ArgumentParser(description="Решение биквадратного уравнения.")
    parser.add_argument("-a", type=float, help="Коэффициент A")
    parser.add_argument("-b", type=float, help="Коэффициент B")
    parser.add_argument("-c", type=float, help="Коэффициент C")
    args = parser.parse_args()

    # Получаем коэффициенты из аргументов командной строки или вводим с клавиатуры
    a = args.a if args.a is not None else get_coefficient("Введите коэффициент A: ")
    b = args.b if args.b is not None else get_coefficient("Введите коэффициент B: ")
    c = args.c if args.c is not None else get_coefficient("Введите коэффициент C: ")

    solve_biquadratic(a, b, c)1

if __name__ == "__main__":
    main()
