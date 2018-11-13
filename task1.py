n = int(input('Введите количество предприятий: '))

names = []
income = []
all_pred_inc = 0
more = []
less = []
same = []
for i in range(n):
    names.append(input('Введите название предприятия'))
    inc1, inc2, inc3, inc4 = map(int, input('Введите прибыли за 4 квартала через пробел: ').split())
    total_inc = (inc1 + inc2 + inc3 + inc4) / 4
    all_pred_inc += total_inc
    income.append(total_inc)
all_pred_inc = all_pred_inc / n
for i in range(n):
    if income[i] < all_pred_inc:
        less.append(names[i])
    elif income[i] > all_pred_inc:
        more.append(names[i])
    else:
        same.append(names[i])
print('Больше среднего: ')
for i in range(len(more)):
    print(more[i])
print('Меншье среднего: ')
for i in range(len(less):
    print(less[i])
