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
