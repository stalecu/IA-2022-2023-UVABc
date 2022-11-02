#!/usr/bin/env python3

import numpy as np
import numpy.typing as npt
from scipy import stats
from typing import Union
import math

from collections.abc import Callable


Real = Union[int, float]
RealArray = list[Union[int, float]]
NumpyFunction = Callable[[npt.NDArray], Real]


def np_apply_fun(arr: RealArray, fun: NumpyFunction):
    """
    Applies the Numpy function `fun` to `arr`. It is essentially a generic
    (sort of) abstraction over the Numpy functions you can do on lists of real
    numbers.
    """
    return fun(np.array(arr))


def mean(arr: RealArray) -> Real:
    """
    Calculates the mean of a list of real numbers.
    """
    return np_apply_fun(arr, np.mean)


def median(arr: RealArray) -> Real:
    """
    Calculates the mean of a list of real numbers.
    """
    return np_apply_fun(arr, np.median)


def mode(arr: RealArray) -> Real:
    """
    Calculates the mode of a list of real numbers.
    """
    return stats.mode(np.array(arr), keepdims=False).mode


def variance_naive(arr: RealArray) -> Real:
    """
    Calculates the variance of a list of real numbers in a naive way.
    """
    arr_mean = mean(arr)
    variance_arr = [(n - arr_mean) ** 2 for n in arr]
    return mean(variance_arr)


def std_dev_naive(arr: RealArray) -> Real:
    """
    Calculates the standard deviation of a list of real numbers in a naive way.
    """
    return math.sqrt(variance_naive(arr))


def std_dev(arr: RealArray) -> Real:
    """
    Calculates the standard deviation of a list of real numbers.
    """
    return np_apply_fun(arr, np.std)


def variance(arr: RealArray) -> Real:
    """
    Calculates the variance of a list of real numbers.
    """
    return np_apply_fun(arr, np.var)


def percentile(arr: RealArray, percentiles: RealArray) -> npt.NDArray:
    """
    Return the n-th percentile (or a list of percentiles) in a list of real numbers.
    """
    return np.percentile(np.array(arr), np.array(percentiles))


def generate_random_array(size: int, min: Real = 0.0, max: Real = 0.0) -> npt.NDArray:
    """
    Return a random array of floats between min and max and a given size.
    The default interval is [0.0, 1.0).
    """
    return np.random.default_rng().uniform(min, max, size)
