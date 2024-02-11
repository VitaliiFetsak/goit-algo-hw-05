import re
from typing import Callable

some_text = """Загальний дохід працівника складається з декількох частин: 
            1000.01 як основний дохід, доповнений додатковими надходженнями 
            27.45 і 324.00 доларів."""

def generator_numbers(text: str):
    regis = re.compile(r'-?\d+(?:\.\d+)?')
    numbers = regis.findall(text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    sum = 0
    numbers = func(text)    
    for number in numbers:
        sum+=number
    return sum

total_income = sum_profit(some_text, generator_numbers)
print(f"Загальний дохід: {total_income}")