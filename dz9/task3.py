total = 0

for i in range(100, 9999):
    i = str(i)
    x = len(i)
    if x == 3:
        if i[0] != i[1] != i[2] and i[0] != i[2]:
            total += 1
    elif x == 4:
        if i[0] != i[1] != i[2] != i[3] and i[0] != i[2] and i[0] != i[3] and i[1] != i[3]:
            total += 1

print(total)
