result = []
for i in range(2, 1000):
    factor = [1]
    for j in range(2, i):
        if i % j == 0:
            factor.append(j)
        if sum(factor) >= i:
            break
    if sum(factor) == i:
        result.append(i)
print(result)
print(len(result))
