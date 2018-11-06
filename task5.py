# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

arr = [random.randint(-100, 100) for _ in range(100)]
print(arr)

j = 0
while arr[j] >= 0:
    j += 1
max_min_el = arr[j]
max_mie_el_idx = j


for i in range(j, len(arr)-1):
    if arr[i] < 0:
        min_el = arr[i]
        if min_el > max_min_el:
            max_min_el = min_el
            max_mie_el_idx = i

print(max_min_el, max_mie_el_idx)