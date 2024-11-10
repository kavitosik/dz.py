num1 = int(input('Введите начало диапозона: '))
num2 = int(input('Введите конец диапозона: '))

chet_nums = [i for i in range(num1, num2+1) if i % 2 == 0]
nechet_nums = [i for i in range(num1, num2+1) if i % 2 != 0]
krat9_nums = [i for i in range(num1, num2+1) if i % 9 == 0]

total = 0
print('Сумма всех чётных чисел: ')
for i in chet_nums:
    total += i
print(total)

total = 0
print('Сумма всех нечётных чисел: ')
for i in nechet_nums:
    total += i
print(total)

total = 0
print('Сумма всех чисел, кратных 9: ')
for i in krat9_nums:
    total += i
print(total)

total = 0
print('Сумма среднего арифметического всех групп: ')
all_nums = chet_nums + nechet_nums + krat9_nums
for i in all_nums:
    total += i
total = total / len(all_nums)
print(total)