# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

size = 10
array = [random.random() * 50 for i in range(size)]
random.shuffle(array)
print(array)

def Merge (a, b):
    res = []
    j = i = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res += a[i:] + b[j:]
    return res

def MergeSort(array):
    if len(array) <= 1:
        return array
    else:
        l = array[:len(array) // 2]
        r = array[len(array) // 2:]
    return Merge(MergeSort(l), MergeSort(r))

print(MergeSort(array))

