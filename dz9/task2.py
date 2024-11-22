for i in range(100, 999):
    i = str(i)
    if i[0] == i[1] or i[0] == i[2] or i[1] == i[2]:
        print(int(i))
