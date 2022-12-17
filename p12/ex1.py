#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


def recursion(n):
    if n == 1:
        return 1

    return n + recursion(n - 1)


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


setup_code_1 = """
from __main__ import fib
n = 6
"""

if __name__ == "__main__":
    print(recursion(7))
    print(factorial(4))

    print(timeit.timeit(stmt="fib(n)", setup=setup_code_1, number=10000))
