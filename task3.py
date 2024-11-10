num1 = int(input('Введите начало диапозона: '))
num2 = int(input('Введите конец диапозона: '))

for i in range(num1, num2+1):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)