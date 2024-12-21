import sys
import cmath

def get_coefficients():
    while True:
        try:
            if len(sys.argv) == 4:
                A = float(sys.argv[1])
                B = float(sys.argv[2])
                C = float(sys.argv[3])
                return A, B, C
            else:
                A = float(input("Введите коэффициент A: "))
                B = float(input("Введите коэффициент B: "))
                C = float(input("Введите коэффициент C: "))
                return A, B, C
        except ValueError:
            print("Ошибка: Введены некорректные значения коэффициентов. Пожалуйста, введите действительные числа.")

def solve_biquadratic(A, B, C):

    discriminant = B**2 - 4 * A * C
    if discriminant >= 0:
        y1 = (-B + discriminant**0.5) / (2 * A)
        y2 = (-B - discriminant**0.5) / (2 * A)
    else:
        y1 = (-B + cmath.sqrt(discriminant)) / (2 * A)
        y2 = (-B - cmath.sqrt(discriminant)) / (2 * A)

    # Находим корни x из y
    roots = []
    if y1 >= 0:
        roots.append(y1**0.5)
        roots.append(-y1**0.5)
    if y2 >= 0:
        roots.append(y2**0.5)
        roots.append(-y2**0.5)

    return roots

def main():
    """Основная функция программы."""
    A, B, C = get_coefficients()
    roots = solve_biquadratic(A, B, C)

    print(f"Корни биквадратного уравнения: {roots}")

if __name__ == "__main__":
    main()

