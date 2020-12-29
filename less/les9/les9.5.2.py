import hashlib

def Rabin_Karp(s: str, subs: str)-> int:
    assert len(s) > 0 and len(subs) > 0, "Строки пустые"
    assert len(s) >= len(subs), "подстрока длинее"

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s)- len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            if s[i:i + len_sub] == subs:
                return i
    return -1



s_1 = input('Введите строку: ')
s_2 = input('Введите часть строки: ')
pos = Rabin_Karp(s_1,s_2)
print(f'Найдена на позиции {pos}' if pos != -1 else 'ненайдена')
