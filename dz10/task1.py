num1 = int(input("Введите начало диапозона: "))
num2 = int(input("Введите конец диапозона: "))

for i in range(num1, num2 + 1):
    n = 2
    while i % n != 0:
        n += 1
        if n == i:
            print(f"{i} - простое.")
