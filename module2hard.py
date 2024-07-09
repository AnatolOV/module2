import random
firstNumber = random.randint(3,20)
result = []
for i in range(1, firstNumber + 1):
    n1 = i
    for r in range(2, firstNumber + 1):
        if n1 < r:
           n2 = r
        if firstNumber % (n1 + n2) == 0:
            result.append(n1)
            result.append(n2)
print(''.join(map(str, result)))
