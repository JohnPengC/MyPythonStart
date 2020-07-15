result = []
for i in range(2, 100):
    is_result = True
    for j in range(2, i):
        if i % j == 0:
            is_result = False
            break
    if is_result:
        result.append(i)
print(result)
print(len(result))
