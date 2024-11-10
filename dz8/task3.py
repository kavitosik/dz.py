num = 0

while num != 7:
    num = int(input("Введите число: "))
    if num > 0 and num != 7:
        print('Number is positive')
    elif num < 0:
        print('Number is negative')
    elif num == 0:
        print('Number is equal to zero')
    else:
        print("Good bye!")