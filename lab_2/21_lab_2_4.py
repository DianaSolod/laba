#я не нашла способ ввести с клавиатуры массив любой вложенности, поэтому он введен в программе
def arrcheck(arr):          #функция, проверяющая, является ли массив не вложенным
    c = 0
    for i in range(len(arr)):
        if not isinstance(arr[i], list):
            c = c + 1
    if c == len(arr):
        return 1
    else:
        return 0


def flat(arr):
    i=0
    while i<30:
        i += 1
        M = []
        if isinstance(arr[i], list):
            le = len(arr[i])
            for j in range(le):
                M.append(arr[i][j])
            for s in range(le):
                arr.insert(i + s, M[s])
            del arr[i + s + 1]
            if i == len(arr)-1:
                i = 0
        if arrcheck(arr):
            break
    print("Your array = ", arr)

def main():
    a=[1,2,[[[[[[[[2]]]]]]]]]
    print(a)
    flat(a)

if __name__ == "__main__":
    main()
