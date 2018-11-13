a = list(input('Введите первое число: '))
b = list(input('Введите второе число: '))
ans = []
print(a)
num_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
nums = ['0', '1', '2' '3', '4', '5', '6', '7', '8', '9']
for i in range(len(a)):
    if (a[i]).isdigit():
        pass
    else:
        a[i] = num_dict[a[i]]


for i in range(len(a)):
    if (a[i]).isdigit():
        pass
    else:
        a[i] = num_dict[a[i]]


a.reverse()
b.reverse()
mult = 1
print(a)
for i in range(0, len(a), 1):
    print(i)
    a[i] = int(a[i]) * 10 ** i
for i in range(0, len(b), 1):
    b[i] = int(b[i]) * 10 ** i

a.reverse()
b.reverse()
print(a)

sum_el = 0
sum_el2 = 0
for i in range(len(a)):
    sum_el += a[i]
for i in range(len(b)):
    sum_el2 += b[i]
total_sum = sum_el + sum_el2
total_mult = sum_el * sum_el2
print(total_sum)
total_sum = hex(total_sum)
total_mult = hex(total_mult)
print(total_sum, total_mult)
total_sum = list(total_sum)
total_mult = list(total_mult)
total_sum = total_sum[2:]
total_mult = total_mult[2:]
for i in range(len(total_sum)):
    if total_sum[i].isalpha():
        total_sum[i] = total_sum[i].upper()
for i in range(len(total_mult)):
    if total_mult[i].isalpha():
        total_mult[i] = total_mult[i].upper()
print(total_sum, total_mult)


