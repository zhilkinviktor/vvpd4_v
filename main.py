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
