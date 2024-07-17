import re
from typing import Callable, Generator


def generator_numbers(text: str): # функція яка використовує регулярний вираз для знаходження всіх чисел у тексті, які оточені пробілами.
    pattern = re.compile(r'\b\d+\.\d+\b|\b\d+\b')
    matches = pattern.findall(text)

    for match in matches:
        yield float(match)


def sum_profit(text: str, func) -> float: # викликає функцію-генератор, передану як аргумент, для отримання всіх чисел з тексту.
    return sum(func(text))


# приклад користування
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
print(sum_profit(text, generator_numbers))
