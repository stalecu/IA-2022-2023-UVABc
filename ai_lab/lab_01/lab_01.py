#!/usr/bin/env python3

from typing import Any, List
import inspect
import colorama as cl


cl.init(autoreset=True)


def print_type(var: Any, var_name: str) -> str:
    return f"{var_name} = {repr(var)} (type is {cl.Fore.GREEN + type(var).__name__ + cl.Style.RESET_ALL})"


def python_is(adjective: str) -> str:
    return f"Python is {cl.Fore.RED + adjective + cl.Style.RESET_ALL}!"


def concat(strA: str = "", strB: str = "") -> str:
    return strA + strB


# Taken from https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
def make_ordinal(n: int) -> str:
    """
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    """
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    return f"{str(n)}{suffix}"


def readNElements(n: int) -> list[int]:
    number_list: list[int] = []
    if n < 0:
        raise ValueError("n should be a positive integer")

    for i in range(0, n):
        print(f"Enter the {make_ordinal(i + 1)} integer: ", end="")
        number_list.append(int(input()))

    return number_list
