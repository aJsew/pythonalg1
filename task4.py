# 4. Определить, какое число в массиве встречается чаще всего.
import random
arr = [random.randint(-100, 100) for _ in range(100)]
print(arr)

max_length = 0
length = 0
max_length_num = arr[0]

for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[i] == arr[j]:
            length += 1
    if length > max_length:
        max_length = length
        max_length_num = arr[i]
    length = 0
print(max_length, max_length_num)