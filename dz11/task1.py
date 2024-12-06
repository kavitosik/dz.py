def draw_shrift(vord):
    if vord == 'а':
        print("Это буква 'а':")
        probel = 0
        zvezda = 10
        for i in range(10):
            i = "*" * zvezda
            j = " " * probel
            stroka = '' + j
            stroka = stroka + i
            print(stroka)
            zvezda -= 1
            probel += 1
    if vord == 'б':
        print("Это буква 'б':")
        n = 1
        for i in range(10):
            i = ["*"] * n
            print(''.join(i))
            n += 1


vord = input("Введите букву от 'а' до 'к': ")

draw_shrift(vord)
