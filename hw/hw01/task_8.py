# Вводятся три разных числа. Найти, какое из них является средним(больше одного, но меньше другого).

a = float(input("Введите число а: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

m_max = max(a, b, c)
m_min = min(a, b, c)

if a != m_max and a != m_min:
    average = a
elif b != m_max and b != m_min:
    average = b
else:
    average = c
