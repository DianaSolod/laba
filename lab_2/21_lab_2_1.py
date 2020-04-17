import math

#функция, которая создает массив или читает его из файла
def arr(x):
    if x == 'b':
        print('Enter size of array')
        N = int(input())
        L = [0]*N
        for i in range(N): 
           print ( "L[", i, "]=", sep = "", end = "" ) 
           L[i] = float(input())
        print("L = ", L)
        return L
    else:
        data = []
        file = open(input("Enter file path: "))
        for line in file:
            data.append([float(x) for x in line.split()])
        return data[0]

def dec(L):
    N = len(L)
    len1 = math.ceil(math.sqrt(N))
    B = [0]*len1
    for i in range(N):
        B[i // len1] += L[i]        #определение суммы каждого блока длиной корень из длины массива
    print("B = ", B)
    print('Enter indexes')
    i = int(input())
    r = int(input())
    Sum = 0
    while i <= r:
        if i % len1 == 0 and i + len1 - 1 <= r:     #к сумме прибавляется значение блока если блок входит в промежуток
            Sum += B[i // len1]
            i += len1
        else:
            Sum += L[i]      #иначе (в конце) к сумме прибавляются слагаемые покомпонентно
            i += 1
    print('Sum = ' + str(Sum))


#запуск функции и взаимодействие с пользователем
def main():
    a = 1
    while(a != 'e'):
        a = input('Type a to load a file or b to enter array (e to exit): ')
        if a == 'a' or a == 'b':
            B = arr(a)
            dec(B)
        elif a == 'e':
            continue
        else:
            print("Wrong input")
           
if __name__ == "__main__":
    main()        
