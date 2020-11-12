""""
Алгоритм это совокупность четко определенных действий выполнения которых ведет к решению задач
"""

""""
псевдокод
начало 
вывод "Введите число"
ввод первое 
ввод второе 
если второе число <> 0
то частное = первое / второе 
    вывод результат = частное
иначе вывод нет решения
конец
"""

""""
блок схема
овал     вход  из внешней среды или выход (начало и конец)
квадрат  выполнение одной или нескольких операций
ромб     отображение решения, влияние на дальнейшее выполнение алгоритма 
....
линейный, развлетвляющийся, циклический
"""
#
# print('Ввести два числа')
# a = int(input('Введите а: '))
# b = int(input('Введите b: '))
# if b != 0:
#     print(f'c = {a/b}')
# else:
#     print('решений нет')

""""Линейный"""
# n = int(input('ввод числа а '))
# a = n // 100
# b = n % 100 // 10
# c = n % 10
# summa = a + b + c
# mult = a * b * c
# print(f'Сумма = {summa}, произведение = {mult}')

"""алгоритмы с условиям"""
x = int(input('x = '))
if x > 0:
    y = 2 * x - 10
elif x == 0:
    y = 0
else:
    y = 2 * abs(x) - 1
print(f'y = {y}')



