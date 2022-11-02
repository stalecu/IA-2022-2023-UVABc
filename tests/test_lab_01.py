#!/usr/bin/env python3

import ai_lab.lab_01 as lab1
import colorama as cl


def test_print_type():
    x: int = 3
    assert (
        lab1.print_type(x, "x")
        == f"x = {repr(x)} (type is {cl.Fore.GREEN + type(x).__name__ + cl.Style.RESET_ALL})"
    )
