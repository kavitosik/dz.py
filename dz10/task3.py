def umnojenie():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    second = 1
    first = num1
    while first in range(num1, num2 + 1):
        for second in range(1, 12):
            if second <= 10:
                print(f'{first} * {second} = {first * second}')
            else:
                print('.'*22)
        first += 1


umnojenie()
