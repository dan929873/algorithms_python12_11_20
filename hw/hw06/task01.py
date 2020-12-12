# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
# первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
#    проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
#    Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

import sys
import random

def size_fun(*args):
    memory = 0
    for i in args:
        memory += sys.getsizeof(i)
    return memory

# a
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

# b
# 1

# m_max = 1000
# m_min = -1000
# numbers = 10
# my_list = [random.randint(m_min, m_max) for i in range(numbers)]
# # print(my_list)
# max_min = m_min
#
# for i in my_list:
#     if max_min < i and i < 0:
#         max_min = i
# # print(my_list.index(max_min), max_min)
# print(size_fun(my_list, m_max, m_min, max_min))


# 2
numbers = 10
my_list = [random.randint(numbers * -10, numbers * 10) for i in range(numbers)]

i = 0
index= -1

while i < numbers:
    if my_list[i] < 0 and index == -1:
        index = i
    elif my_list[i]<0 and my_list[i] > my_list[index]:
        index = i
    i += 1
print(size_fun(numbers, my_list, i, index))

# c
print(sys.version, sys.platform)
# 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] win32
#
# 1: byte - 142
# 2: byte - 142

# d
# Нет вывода  - оба варианта схожи, не нашел интресного варианта по модернизации

