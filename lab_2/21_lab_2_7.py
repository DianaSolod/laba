def leon(n):
    if n == 0 or n == 1:
        return 1
    return leon(n - 1) + leon(n - 2) + 1

#запуск функции и взаимодействие с пользователем
def main():
    a = 1
    while(a != 'e'):
        a = input('Введите номер числа леонардо (e to exit): ')
        if a.isnumeric():
            print(a,'число Леонардо: ',leon(int(a)))
        elif a == 'e':
            continue
        else:
            print("Wrong input")

if __name__ == "__main__":
    main()
