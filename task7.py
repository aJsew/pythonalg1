# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random
arr = [random.randint(-100, 100) for _ in range(100)]
print(arr)

if arr[0] < arr[1]:
    min_el_1 = 0
    min_el_2 = 1
else:
    min_el_1 = 1
    min_el_2 = 0

for i in range(2, len(arr)-1):
    if arr[i] < arr[min_el_1]:
        diff = min_el_1
        min_el_1 = i
        if arr[diff] < arr[min_el_2]:
            min_el_2 = diff
    else:
        if arr[i] < arr[min_el_2]:
            min_el_2 = i
print('№ элемента в массиве:', min_el_1, 'Элемент:', arr[min_el_1], '\n№ элемента в массиве:', min_el_2, 'Элемент:', arr[min_el_2])