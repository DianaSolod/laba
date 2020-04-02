def check(a):
    b = a
    i = 0
    for i in range(1): 
        while a % 2 == 0 and a > 2:
            a = a / 2
        if a == 2 or b == 1:
            print("Number " + str(b) + " is a power of 2")
        else:
            print("Number " + str(b) + " is NOT a power of 2")

#запуск функции и взаимодействие с пользователем
a = 1
while(a != 'e'):
    a = input('Введите число (e to exit): ')
    if a.isnumeric():
        check(int(a))
    elif a == 'e':
        continue
    else:
        print("Wrong input")

