# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.


string = input('Введите строку: ')


def rabin_karp(s, subs):
    answer = 0
    len_subs = len(subs)
    h_subs = hash(subs)
    for i in range(len(s) - len_subs + 1):
        if h_subs == hash(s[i:i + len_subs]):
            answer += 1
    return answer


sub = 0


d = 0
while d <= (len(string) - 1):
    sub += rabin_karp(string, string[d:])
    d += 1
d = 1
while d <= (len(string) - 1):
    sub += rabin_karp(string, string[:d])
    d += 1
print(sub)
