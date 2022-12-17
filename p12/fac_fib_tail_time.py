#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа показыает работу декоратора, который производит оптимизацию
# хвостового вызова. Он делает это, вызывая исключение, если оно является его
# прародителем, и перехватывает исключения, чтобы вызвать стек.

import sys
import timeit


class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
Эта программа показыает работу декоратора, который производит оптимизацию
хвостового вызова. Он делает это, вызывая исключение, если оно является его
прародителем, и перехватывает исключения, чтобы подделать оптимизацию хвоста.

Эта функция не работает, если функция декоратора не использует хвостовой вызов.
"""

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func


def factorial(n, acc=1):
    "calculate a factorial"
    if n == 0:
        return acc

    return factorial(n-1, n*acc)


def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)


# o - оптимизированный
#@tail_call_optimized
def factorial_o(n, acc=1):
    "calculate a factorial"
    if n == 0:
        return acc

    return factorial_o(n-1, n*acc)


#@tail_call_optimized
def fib_o(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib_o(i - 1, next, current + next)


setup_code_1 = """
from __main__ import factorial
n = 100
"""

setup_code_2 = """
from __main__ import factorial_o
n = 100
"""

setup_code_3 = """
from __main__ import fib
n = 100
"""

setup_code_4 = """
from __main__ import fib_o
n = 100
"""

if __name__ == '__main__':
    print("Рекурсивная функция (fac):")
    print(timeit.timeit(stmt="factorial(n)", setup=setup_code_1, number=10000))
    print("Оптимизированная функция (fac):")
    print(timeit.timeit(stmt="factorial_o(n)", setup=setup_code_2, number=10000))
    print("Рекурсивная функция (fib):")
    print(timeit.timeit(stmt="fib(n)", setup=setup_code_3, number=10000))
    print("Оптимизированная функция (fib):")
    print(timeit.timeit(stmt="fib_o(n)", setup=setup_code_4, number=10000))