import math


def maclaurin_sinh(x: float, iterations: int = 10) -> float:
    """
    Вычисляет гиперболический синус (sinh(x)) через ряд Маклорена.

    Аргументы:
        x (float): значение, для которого вычисляется гиперболический синус.
        iterations (int): количество итераций для точности вычислений.

    Возвращаемое значение:
        float: значение гиперболического синуса.

    Исключения:
        ValueError: если iterations <= 0.
    """
    if iterations <= 0:
        raise ValueError("Количество итераций должно быть больше 0.")

    result = 0
    for n in range(iterations):
        term = (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        result += term
    return result


def maclaurin_ln(x: float, iterations: int = 10) -> float:
    """
    Вычисляет натуральный логарифм (ln(x - 1)) через ряд Маклорена.

    Аргументы:
        x (float): значение, для которого вычисляется натуральный логарифм.
        iterations (int): количество итераций для точности вычислений.

    Возвращаемое значение:
        float: значение ln(x - 1).

    Исключения:
        ValueError: если x <= 1 или iterations <= 0.
    """
    if x <= 1:
        raise ValueError("x должно быть больше 1.")
    if iterations <= 0:
        raise ValueError("Количество итераций должно быть больше 0.")

    result = 0
    for n in range(1, iterations + 1):
        term = ((-1) ** (n + 1)) * ((x - 1) ** n) / n
        result += term
    return result


def maclaurin_binomial(x: float, m: float, iterations: int = 10) -> float:
    """
    Вычисляет (1 + x)^m через ряд Маклорена.

    Аргументы:
        x (float): значение x.
        m (float): степень m.
        iterations (int): количество итераций для точности вычислений.

    Возвращаемое значение:
        float: значение (1 + x)^m.

    Исключения:
        ValueError: если iterations <= 0.
    """
    if iterations <= 0:
        raise ValueError("Количество итераций должно быть больше 0.")

    result = 0
    for n in range(iterations):
        term = math.comb(m, n) * (x ** n)
        result += term
    return result


def main_menu():
    """
    Главное меню программы для вычисления функций.
    """
    while True:
        print("\nМеню")
        print("1. Вычислить sinh(x)")
        print("2. Вычислить ln(x - 1)")
        print("3. Вычислить (1 + x)^m")
        print("4. Выход")

        choice = input("Введите номер операции: ")
        if choice == "1":
            try:
                x = float(input("Введите x: "))
                result = maclaurin_sinh(x)
                print(f"Результат: sinh({x}) = {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            try:
                x = float(input("Введите x (x > 1): "))
                result = maclaurin_ln(x)
                print(f"Результат: ln({x} - 1) = {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "3":
            try:
                x = float(input("Введите x: "))
                m = float(input("Введите m: "))
                result = maclaurin_binomial(x, m)
                print(f"Результат: (1 + {x})^{m} = {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

