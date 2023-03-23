# Создайте функцию генератор чисел Фибоначчи
NUMBER = 20


def phoebe(number: int) -> int:
    first = 0
    if number >= 0:
        yield first
    second = 1
    if number >= 1:
        yield second
    for i in range(number-1):
        result = first + second
        first = second
        second = result
        yield result


print(*phoebe(NUMBER))

