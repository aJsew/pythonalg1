# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

import random
arr = [random.randint(-100, 100) for _ in range(100)]
print(arr)

minimum = arr[0]
min_idx = 0
maximum = arr[0]
max_idx = 0
sum_el = 0

for i in range(1, len(arr)-1):

    if arr[i] < minimum:
        minimum = arr[i]
        min_idx = i

    elif arr[i] > maximum:
        maximum = arr[i]
        max_idx = i

if min_idx > max_idx:
    print(arr[max_idx:min_idx])
    for i in range(max_idx + 1, min_idx - 1):
        sum_el += arr[i]

elif max_idx > min_idx:
    print(arr[min_idx:max_idx])
    for i in range(min_idx + 1, max_idx - 1):
        sum_el += arr[i]

print(min_idx, max_idx)
print(sum_el)