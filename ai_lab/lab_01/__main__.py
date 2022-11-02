#!/usr/bin/env python3

import sys
import warnings

if not sys.warnoptions:  # allow overriding with `-W` option
    warnings.filterwarnings("ignore", category=RuntimeWarning, module="runpy")


from .lab_01 import *


def main():
    x: int = 10
    print_type(x, "x")
    y: str = "John"
    print_type(y, "y")

    print()

    print_type(str(3), "3 (string)")
    print_type(int(3), "3 (int)")
    print_type(float(3), "3 (float)")

    print()

    print(python_is("awesome"))

    a, b, c = "Red", "Green", "Blue"

    print()

    print(f"a, b, c = {(a, b, c)}")

    print()

    fruits = ["apple", "pear", "cherry"]
    a, b, c = fruits
    print(f"fruits = {fruits}")
    print(f"a, b, c = {(a, b, c)}")

    print()

    print("Enter the number of elements: ", end="")
    n: int = int(input())
    number_list: list[int] = readNElements(n)

    print(
        f"The list of integers is: {cl.Fore.BLUE + str(number_list) + cl.Style.RESET_ALL}"
    )

    print()

    str_a: str = "String1"
    str_b: str = "String2"
    print(f"{str_a} + {str_b} = {concat(str_a, str_b)}")

    print()

    number_list.sort()
    print(f"The sorted number array above is: {str(number_list)}")
    print(f"The biggest element is: {max(number_list)}")
    print(f"The smallest element is: {min(number_list)}")
    string_list = ["String", "List", "Dict"]
    print(f"String list: {string_list}")
    print(f"Removing last element from {number_list}...")
    number_list.pop(-1)
    print(f"The list is now {number_list}")
    print("Removing all even numbers...")
    for i in number_list:
        if i % 2 == 0:
            number_list.remove(i)

    print(f"The list with only odd numbers: {number_list}")

    print(f"Original fruits array: {fruits}")
    print("Fruits with r in their name: ", end="")
    print([fruit for fruit in fruits if "r" in fruit])


if __name__ == "__main__":
    main()
