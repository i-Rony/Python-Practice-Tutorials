# calculator.py

from typing import Literal, overload, Union

ARABIC_TO_ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                   (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                   (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def _convert_to_roman_numeral(number: int) -> str:
    """Convert number to a roman numeral string"""
    result = list()
    for arabic, roman in ARABIC_TO_ROMAN:
        count, number = divmod(number, arabic)
        result.append(roman * count)
    return "".join(result)

@overload
def add(num_1: int, num_2: int, to_roman: Literal[True]) -> str: ...
@overload
def add(num_1: int, num_2: int, to_roman: Literal[False]) -> int: ...

def add(num_1: int, num_2: int, to_roman: bool = True) -> Union[str, int]:
    """Add two numbers"""
    result = num_1 + num_2

    if to_roman:
        return _convert_to_roman_numeral(result)
    else:
        return result
