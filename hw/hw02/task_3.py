# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
numbers = ''
number = ''
while numbers != 'q' or number != 'q':
    numbers = input('input numbers: ')
    number = input('input number: ')
    res = 0
    for i in numbers:
        if i == number:
            res += 1
    print(res)
