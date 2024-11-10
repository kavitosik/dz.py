num1 = int(input('Введите начало диапозона: '))
num2 = int(input('Введите конец диапозона: '))
nums = []

for i in range(num1, num2+1):
    if i % 7 == 0:
        nums.append(i)

print(f'Вот все числа, которые делятся на 7 в выбранном диапозоне:')
print(*nums)