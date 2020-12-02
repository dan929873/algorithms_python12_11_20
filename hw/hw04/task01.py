# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

import cProfile

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
# в том числе написанных самостоятельно.

import random
import math
# def m_fun(s):
#     SIZE = s
#     mtx = [[random.randint(0,100)for _ in range(SIZE)] for _ in range(SIZE)]
#     max_min = - math.inf
#     for i in range(SIZE):
#         m_min = math.inf
#         for j in range(SIZE):
#             if m_min > mtx[j][i]:
#                 m_min = mtx[j][i]
#         if max_min < m_min:
#             max_min = m_min

def m_fun2(s):
    SIZE = s
    mtx = [[random.randint(0,100)for _ in range(SIZE)] for _ in range(SIZE)]
    for line in mtx:
        print(*line, sep = '\t')
    max_min = min(mtx[0])

    for i in range(SIZE):
        if max_min < min(mtx[i]): #смотрит в строке, нужно в столбце
            max_min = min(mtx[i])
    print(max_min)
m_fun2(5)
# "task01.m_fun(5)" 5
# 1000 loops, best of 3: 33.5 usec per loop
# "task01.m_fun(100)" 100
# 1000 loops, best of 3: 11.4 msec per loop

# "task01.m_fun2(100)"
# 1000 loops, best of 3: 11.5 msec per loop

