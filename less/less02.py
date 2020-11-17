import sys

sys.setrecursionlimit(30000)

def akk(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return akk(m-1,1)
    return akk(m-1,akk(m, n-1))

# print(akk(4,4))

def gcm(m,n):
    if n == 0:
        return m
    return gcm(n, m % n)


def gcm3(m,n):
    while n != 0:
        m, n = n, m % n
    return m
#
# print(gcm3(540, 21678678))

# решето Эратосфера
n = 10000
sieve = [i for i in range(n)]
sieve[1] = 0
for i in range(2, n):
    if sieve[i] != 0:
        j = i + i

        while j < n:
            sieve[j] = 0
            j += i

result = [i for i in sieve if i != 0]
# print(result)

def binary(num):
    s = ''
    while num > 0:
        s = (f'{num % 2}{s}')
        num //= 2
    return s

print(binary(1024))
