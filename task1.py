import random
# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.


def bubble_sort():
    arr = [random.randint(-100, 100) for _ in range(10)]
    print(arr)
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    print(arr)


bubble_sort()


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


array = [random.uniform(0, 50) for _ in range(10)]
print(array)


def merge(right, left, result):
    result.append((left if left[0] < right[0] else right).pop(0))
    return merge(right=right, left=left, result=result) if left and right else result + left + right


merge_sort = (lambda arr: arr if len(arr) == 1 else merge(merge_sort(arr[int(len(arr) / 2):]),
                                                          merge_sort(arr[:int((len(arr) / 2))]), []))


print(merge_sort(array))


# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше ее.


def median(m):
    arr = [random.randint(0, 50) for _ in range(m * 2 + 1)]
    print(arr)
    left = []
    right = []
    for i in range(len(arr)):
        more = 0
        less = 0
        count = 0
        for j in range(0, i):
            if arr[j] < arr[i]:
                less += 1
            elif arr[j] > arr[i]:
                more += 1
            else:
                count += 1
        for j2 in range(i+1, len(arr)):
            if arr[j2] < arr[i]:
                less += 1
            elif arr[j2] > arr[i]:
                more += 1
            else:
                count += 1
        if (less == more) | (less + count == more) | (more + count == less):
            for l in range(len(arr)):
                if arr[l] == arr[i]:
                    right.append(arr[l])
                elif arr[l] < arr[i]:
                    left.append(arr[l])
            for l in range(len(arr)):
                if arr[l] > arr[i]:
                    right.append(arr[l])
            print(arr[i])
            result = left + right
            return result


print(median(10))
# print(merge_sort([41, 31, 29, 15, 20, 33, 6, 48, 49, 35, 38, 39, 29, 30, 49, 25, 24, 8, 1, 5, 3]))
