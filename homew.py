import sys
import ctypes
import struct
import random

# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3
# ваших программы или несколько вариантов кода
# для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.
# python 3.6, windows 10 x64


def show_size(x, level=0):
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)

# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.


arr3 = [random.randint(-100, 100) for _ in range(100)]
print(arr3)
minimum3 = arr3[0]
min_idx3 = 0
maximum3 = arr3[0]
max_idx3 = 0
for i3 in range(1, len(arr3)-1):
    if arr3[i3] < minimum3:
        minimum3 = arr3[i3]
        min_idx = i3
    elif arr3[i3] > maximum3:
        maximum3 = arr3[3]
        max_idx3 = i3
print(max_idx3, min_idx3, maximum3, minimum3)
arr3[min_idx3] = maximum3
arr3[max_idx3] = minimum3
print(arr3)


show_size(arr3)
print(sys.getsizeof(i3))
print(sys.getsizeof(maximum3))
print(sys.getsizeof(minimum3))
print(sys.getsizeof(max_idx3))
print(sys.getsizeof(min_idx3))

# type=<class 'list'>, size=912
# size(i) = 28
# size(maximum) = 28
# size(minimum) = 28
# size(max_idx) = 28
# size(min_idx) = 24
# Всего задействовано памяти: 1048 байтов


# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.


arr5 = [random.randint(-100, 100) for _ in range(100)]
print(arr5)

j5 = 0
while arr5[j5] >= 0:
    j5 += 1
max_min_el5 = arr5[j5]
max_mie_el_idx5 = j5


for i5 in range(j5, len(arr5)-1):
    if arr5[i5] < 0:
        min_el5 = arr5[i5]
        if min_el5 > max_min_el5:
            max_min_el5 = min_el5
            max_mie_el_idx = i5

print(max_min_el5, max_mie_el_idx5)


show_size(arr5)
print(sys.getsizeof(i5))
print(sys.getsizeof(j5))
print(sys.getsizeof(min_el5))
print(sys.getsizeof(max_min_el5))
print(sys.getsizeof(max_mie_el_idx5))

# type=<class 'list'>, size=912
# size(i) = 28
# size(j) = 24
# size(min_el) = 28
# size(max_min_el) = 28
# size(max_min_el_idx) = 24
# Всего задействовано памяти: 1044 байтов


# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать


arr7 = [random.randint(-100, 100) for _ in range(100)]
print(arr7)

minimum7 = arr7[0]
min_idx7 = 0
maximum7 = arr7[0]
max_idx7 = 0
sum_el7 = 0

for i7 in range(1, len(arr7)-1):

    if arr7[i7] < minimum7:
        minimum7 = arr7[i7]
        min_idx7 = i7

    elif arr7[i7] > maximum7:
        maximum7 = arr7[i7]
        max_idx7 = i7

if min_idx7 > max_idx7:
    print(arr7[max_idx7:min_idx7])
    for i7 in range(max_idx7 + 1, min_idx7 - 1):
        sum_el7 += arr7[i7]

elif max_idx7 > min_idx7:
    print(arr7[min_idx7:max_idx7])
    for i in range(min_idx + 1, max_idx7 - 1):
        sum_el7 += arr7[i]

print(min_idx7, max_idx7)
print(sum_el7)

show_size(arr7)
print(sys.getsizeof(i7))
print(sys.getsizeof(minimum7))
print(sys.getsizeof(min_idx7))
print(sys.getsizeof(max_idx7))
print(sys.getsizeof(sum_el7))
print(sys.getsizeof(maximum7))

# type=<class 'list'>, size=912
# size(i7) = 28
# size(minimum7) = 28
# size(min_idx7) = 28
# size(max_idx7) = 28
# size(sum_el7) = 28
# size(minimum7) = 28
# Всего места в памяти задействовано: 1080 байт


# Так как списки генерируются каждый раз по-новому, переменные могут изменять свой вес, он варируется от 24 до 28


