# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.
import random

arr = [random.randint(-100, 100) for _ in range(100)]
print(arr)
minimum = arr[0]
min_idx = 0
maximum = arr[0]
max_idx = 0
for i in range(1, len(arr)-1):
    if arr[i] < minimum:
        minimum = arr[i]
        min_idx = i
    elif arr[i] > maximum:
        maximum = arr[i]
        max_idx = i
print(max_idx, min_idx, maximum, minimum)
arr[min_idx] = maximum
arr[max_idx] = minimum
print(arr)