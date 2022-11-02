#!/usr/bin/env python3

import numpy as np
from . import lab_02 as lab2
from colorama import Fore, Style, init
import math
import pprint

from typing import Union

Real = lab2.Real
RealArray = lab2.RealArray


def main():
    init()
    pp: pprint.PrettyPrinter = pprint.PrettyPrinter(indent=4, width=80)

    speed: RealArray = [
        99,
        86,
        87,
        88,
        111,
        86,
        103,
        87,
        94,
        78,
        77,
        85,
        86,
    ]
    print(f"Speed array: {Fore.RED + str(speed) + Style.RESET_ALL}")
    print()
    print(f"{Style.BRIGHT + Fore.MAGENTA}===== Statistics ====={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Mean{Style.RESET_ALL}: {lab2.mean(speed)}")
    print(f"{Fore.YELLOW}Median{Style.RESET_ALL}: {lab2.median(speed)}")
    print(f"{Fore.YELLOW}Mode{Style.RESET_ALL}: {lab2.mode(speed)}")
    print(
        f"{Fore.YELLOW}Variance (naive){Style.RESET_ALL}: {lab2.variance_naive(speed)}"
    )
    print(f"{Fore.YELLOW}Variance (numpy){Style.RESET_ALL}: {lab2.variance(speed)}")
    print(
        f"{Fore.YELLOW}Standard deviation (naive){Style.RESET_ALL}: {lab2.std_dev_naive(speed)}"
    )
    print(
        f"{Fore.YELLOW}Standard deviation (numpy){Style.RESET_ALL}: {lab2.std_dev(speed)}"
    )

    print()

    ages: RealArray = [
        5,
        31,
        43,
        48,
        50,
        41,
        7,
        11,
        15,
        39,
        80,
        82,
        32,
        2,
        8,
        6,
        25,
        3,
    ]
    print(f"Ages: {Fore.GREEN + str(ages) + Style.RESET_ALL}")
    print(
        f"Percentile ranks from 0 to 100 with step 5:\n{Fore.GREEN + str(lab2.percentile(ages, [i for i in range(0, 101, 5)])) + Style.RESET_ALL}"
    )

    print()

    random_angles = [
        round(math.degrees(i))
        for i in lab2.generate_random_array(20, min=-np.pi, max=np.pi)
    ]
    print(
        f"20 random angles (in degrees, rounded):\n{Fore.CYAN + str(random_angles) + Style.RESET_ALL}"
    )


if __name__ == "__main__":
    main()
