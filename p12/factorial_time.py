#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_r(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_r(n - 1)


def factorial_w(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


setup_code_1 = """
from __main__ import factorial
n = 6
"""

setup_code_2 = """
from __main__ import factorial_r
n = 6
"""

setup_code_3 = """
from __main__ import factorial_w
n = 6
"""

if __name__ == "__main__":
    print("Рекурсивная функция:")
    print(timeit.timeit(stmt="factorial_r(n)", setup=setup_code_2, number=10000))
    print("Итеративная функция:")
    print(timeit.timeit(stmt="factorial_w(n)", setup=setup_code_3, number=10000))
    print("Рекурсивная функция с lru_cache:")
    print(timeit.timeit(stmt="factorial(n)", setup=setup_code_1, number=10000))
