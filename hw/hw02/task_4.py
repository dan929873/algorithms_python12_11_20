# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def num_max(a,b):
    sum1 = 0
    sum2 = 0
    for i in a:
        sum1 += int(i)
    for i in b:
        sum2 += int(i)
    if sum1 > sum2:
        return f'{a}: {sum1}'
    else:
        return f'{b}: {sum2}'

a = input('num1: ')
b = input('num2: ')
print(num_max(a, b))

