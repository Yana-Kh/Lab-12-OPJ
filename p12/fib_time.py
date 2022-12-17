import timeit
from functools import lru_cache


@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def fib_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n - 2) + fib(n - 1)


def fib_w(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


setup_code_1 = """
from __main__ import fib
n = 6
"""

setup_code_2 = """
from __main__ import fib_r
n = 6
"""

setup_code_3 = """
from __main__ import fib_w
n = 6
"""

if __name__ == "__main__":
    print("Рекурсивная функция:")
    print(timeit.timeit(stmt="fib_r(n)", setup=setup_code_2, number=10000))
    print("Итеративная функция:")
    print(timeit.timeit(stmt="fib_w(n)", setup=setup_code_3, number=10000))
    print("Рекурсивная функция с lru_cache:")
    print(timeit.timeit(stmt="fib(n)", setup=setup_code_1, number=10000))
