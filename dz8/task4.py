num = int(input('Введите число(стоп число - 7): '))
sum = 0
max = num
min = num

while num != 7:
    print('Сумма:')
    sum += num
    print(sum)
    if num > max:
        max = num
    print('Максимальное число: ')
    print(max)
    if num < min:
        min = num
    print('Минимальное число: ')
    print(min)
    num = int(input('Введите число(стоп число - 7): '))
print('Good bye!')