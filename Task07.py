# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def simple_number(number: int) -> int:
    for i in range(2, number + 1):
        simple = True
        for j in range(2, i):
            if i % j == 0:
                simple = False
        if simple:
            yield i

