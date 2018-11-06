# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

arr = [_ for _ in range(2, 100)]
print(arr)

mult2 = 0
mult3 = 0
mult4 = 0
mult5 = 0
mult6 = 0
mult7 = 0
mult8 = 0
mult9 = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        mult2 += 1
        if arr[i] % 4 == 0:
            mult4 += 1
        if arr[i] % 6 == 0:
            mult6 += 1
        if arr[i] % 8 == 0:
            mult8 += 1
        if arr[i] % 3 == 0:
            mult3 += 1
        if arr[i] % 5 == 0:
            mult5 += 1
        if arr[i] % 7 == 0:
            mult7 += 1
        if arr[i] % 9 == 0:
            mult9 += 1
    elif arr[i] % 3 == 0:
        mult3 += 1
        if arr[i] % 6 == 0:
            mult6 += 1
        if arr[i] % 9 == 0:
            mult9 += 1
        if arr[i] % 5 == 0:
            mult5 += 1
        if arr[i] % 7 == 0:
            mult7 += 1
    elif arr[i] % 5 == 0:
        mult5 += 1
        if arr[i] % 7 == 0:
            mult7 += 1
    elif arr[i] % 7 == 0:
        mult7 += 1

print(mult2, mult3, mult4, mult5, mult6, mult7, mult8, mult9)
