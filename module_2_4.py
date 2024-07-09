numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
notSimple = []
simple = []

for i in numbers:
    if i == 1:
        notSimple.append(i)
    for j in range(2, i - 1):
        if i % j == 0:
            notSimple.append(i)
            break

for el in numbers:
    if el not in notSimple:
        simple.append(el)

print('Список непростых чисел: ', notSimple)
print('Список простых чисел: ', simple)