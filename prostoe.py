import cProfile
# import random  # для задания из предыдущего дз
# arr = [random.randint(-100, 100) for _ in range(60)]
# print(arr)


def prime_numbers_er(n):
    primes = []
    k = 0
    start = 2
    end = n + 1

    while len(primes) < n:
        for i in range(start, end):
            for j in range(2, i):
                if i % j == 0:
                    k = k + 1
            if k == 0:
                primes.append(i)
            else:
                k = 0
        start = int(primes[-1]) + 1
        end += 2
    return primes[-1]


# prime_numbers_er(10)
# 100 loops, best of 3: 43.3 usec per loop
# prime_numbers_er(15)
# 100 loops, best of 3: 74.6 usec per loop
# prime numbers_er(100)
# 100 loops, best of 3: 15.3 msec per loop
# cProfile.run('prime_numbers_er(10)') 1    0.000    0.000    0.000    0.000 prostoe.py:4(prime_numbers_er)
# cProfile.run('prime_numbers_er(15)') 1    0.000    0.000    0.000    0.000 prostoe.py:4(prime_numbers_er)
# O(f(N))

def prime_noerat(n):

    def isprime(n1):
        counter = 0
        if n1 == 1:
            return False
        if n1 == 2:
            return True
        for x in range(2, n1 - 1):
            if n1 % x == 0:
                counter += 1
        if counter == 0:
            return True
        return False
    count = 0
    num = 2
    while count < n:
        if isprime(num):
            count += 1
            prime = num
            num += 1
        else:
            num += 1
    return prime


# prime_noerat(10)
# 100 loops, best of 3: 21.7 usec per loop
# prime_noerat(15)
# 100 loops, best of 3: 49 usec per loop
# prime_noerat(100)
# 100 loops, best of 3: 4.99 msec per loop
# cProfile.run('prime_noerat(10)') 1    0.000    0.000    0.000    0.000 prostoe.py:37(prime_noerat)
# cProfile.run('prime_noerat(15)') 1    0.000    0.000    0.000    0.000 prostoe.py:37(prime_noerat)
# O(f(N))


# № 5. Урок 3.  В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.


def mas_neg(args):
    j = 0
    while args[j] >= 0:
        j += 1
    max_min_el = args[j]
    max_mie_el_idx = j

    for i in range(j, len(args)-1):
        if arr[i] < 0:
            min_el = arr[i]
            if min_el > max_min_el:
                max_min_el = min_el
                max_mie_el_idx = i

    return max_min_el, max_mie_el_idx


# test_arr length = 20
# 100 loops, best of 3: 1.57 usec per loop
# test_arr length = 40
# 100 loops, best of 3: 2.58 usec per loop
# test_arr length = 60
# 100 loops, best of 3: 3.65 usec per loop
# cProfile.run('mas_neg([-46, 16, 42, -13, 38, -20, -68, -63, 69, -17, -74, 33, -97, 2, 76, -69, -52, 87, -30, 69])')
# 1    0.000    0.000    0.000    0.000 prostoe.py:80(mas_neg)
# O(N)

# Написать еще одну реализацию этого алгоритма не смог, т.к. все варианты которые я пробовал
# были по сути такими же как и изначальный вариант
