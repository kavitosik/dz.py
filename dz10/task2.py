def umnojenie():
    first = 1
    second = 1
    while first <= 10:
        for second in range(1, 12):
            if second <= 10:
                print(f'{first} * {second} = {first * second}')
            else:
                print('.'*22)
        first += 1

umnojenie()
