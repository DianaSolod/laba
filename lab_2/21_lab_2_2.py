import sys
import random
import string
import time
import math  


def show_progress_bar(bar_length, completed, total):
    bar_length_unit_value = (total / bar_length)
    completed_bar_part = math.ceil(completed / bar_length_unit_value)
    progress = "*" * completed_bar_part
    remaining = " " * (bar_length - completed_bar_part)
    percent_done = "%.2f" % ((completed / total) * 100)
    print(f'[{progress}{remaining}] {percent_done}%', end='\r')


def gen(name, Mb, K=(10, 100), L=(3,10)):
    file = open(name + '.txt', 'w')
    size = Mb * 1024**2
    text = ''
    while sys.getsizeof(text) < size:
        num1 = random.randint(*K)
        for i in range(num1):
            num2 = random.randint(*L)
            word = ''.join(random.choice(string.ascii_lowercase) for i in range(num2))
            text += word + ' '
        text += '\n'
        show_progress_bar(50,sys.getsizeof(text),size)
    file.write(text)
    file.close()
    if sys.getsizeof(text) >= size:
        print("\n"+ "Your file is ready")

#запуск функции и взаимодействие с пользователем
def main():
    while True:
        name = input("Enter file name: ")
        try:
            Mb = float(input("Enter size of the file: "))
            K = tuple(int(x.strip()) for x in input("Enter number of words(interval): ").split(','))
            L = tuple(int(x.strip()) for x in input("Enter length of words(interval): ").split(','))
            break
        except ValueError:
            print("Wrong input")
    gen(name, Mb, K, L)


if __name__ == "__main__":
    main()

