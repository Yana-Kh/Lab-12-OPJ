#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def permutations(line):
    """creating permutations"""
    if len(line) == 1:
        return [line]  # базовая рекурсия
    else:
        # создаем массив для записи перестановок
        all = []
        # первый элемент списка помещаем в а
        a = line[0]
        # все перестановки, для последовательности без 1-го эл
        per = permutations(line[1:])
        # перестановки
        for p in per:
            # использовала enumerate, чтоб не брать range(len)
            for i, item in enumerate(p):
                # создаем комбинации с разным положением а (1-ый эл.)
                tmp = p[0:i] + [a] + p[i:]
                all.append(tmp)
            all.append(p + [a])
        return all


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(permutations([i for i in range(1, n + 1)]))
