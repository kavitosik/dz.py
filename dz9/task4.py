num = int(input("Введите любое целое число: "))

num = str(num)
num = num.replace('3', '')
num = num.replace("6", "")

print(f'Вот число без цифр 3 и 6: {num}')
