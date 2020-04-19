
import time
import math  

def show_progress_bar(bar_length, completed, total):
    bar_length_unit_value = (total / bar_length)
    completed_bar_part = math.ceil(completed / bar_length_unit_value)
    progress = "*" * completed_bar_part
    remaining = " " * (bar_length - completed_bar_part)
    percent_done = "%.2f" % ((completed / total) * 100)
    print(f'[{progress}{remaining}] {percent_done}%', end='\r')


def Sort(List): 
    if len(List) >1: 
        middle = len(List)//2 
        Left = List[:middle] 
        Right = List[middle:]  
        Sort(Left)          #рекурсивно сортируем половины
        Sort(Right) 
        i = 0; j = 0; k = 0; 
        while i < len(Left) and j < len(Right): 
            if Left[i] < Right[j]: 
                List[k] = Left[i] 
                i+=1
            else: 
                List[k] = Right[j] 
                j+=1
            k+=1
        while i < len(Left):      #добавляем элементы если половины неравные
            List[k] = Left[i] 
            i+=1
            k+=1          
        while j < len(Right): 
            List[k] = Right[j] 
            j+=1
            k+=1

def main():
    l = open("file.txt", 'r+')
    a=[]
    for line in l:
        a.append(line)
    for i in range(len(a)):
        a[i]=a[i].split()
        Sort(a[i])
    Sort(a)
    b=" "
    for i in range(len(a)):
        b+=" ".join(a[i])
        b+='\n'
    for i in range(len(b)):
        show_progress_bar(50,i,len(b))
    l = open("file.txt", 'w+')
    l.write(b)
    l.close()
    print(b)

if __name__ == "__main__":
    main()





