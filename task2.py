num1 = int(input('Введите начало диапозона: '))
num2 = int(input('Введите конец диапозона: '))
nums = [i for i in range(num1, num2+1)]
nums_reverse = [i for i in range(num1, num2+1)]
nums_reverse.sort(reverse=True)
kratno5 = [i for i in nums if i % 5 == 0]

print('Все числа диапозона:')
print(*nums)

print('Все числа в убывающем порядке:')
print(*nums_reverse)

print('Все числа, кратные 7:')
a = [i for i in range(num1, num2+1) if i % 7 == 0]

print(*[i for i in range(num1, num2+1) if i % 7 == 0])

print('Кол-во чисел, кратных 5:')
print(len(kratno5))