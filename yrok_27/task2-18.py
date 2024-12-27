num = input("Введите любое трёхзначное число: ")

num1 = num[0] + num[1] + num[2]
num2 = num[0] + num[2] + num[1]
num3 = num[1] + num[0] + num[2]
num4 = num[1] + num[2] + num[0]
num5 = num[2] + num[0] + num[1]
num6 = num[2] + num[1] + num[0]

print("Вот все возможные числа:")
print(f"{num1}")
print(f"{num2}")
print(f"{num3}")
print(f"{num4}")
print(f"{num5}")
print(f"{num6}")
