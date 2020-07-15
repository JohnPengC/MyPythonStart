result = [1, 1]
for i in range(2, 20):
    result.append(result[i - 1] + result[i - 2])
print(result)
print(len(result))
