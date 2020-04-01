{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#функция, которая создает массив или читает его из файла\n",
    "def arr(x):\n",
    "    if x == 'b':\n",
    "        print('Enter size of array')\n",
    "        N = int(input())\n",
    "        L = [0]*N\n",
    "        for i in range(N): \n",
    "           print ( \"L[\", i, \"]=\", sep = \"\", end = \"\" ) \n",
    "           L[i] = float(input())\n",
    "        print(\"L = \", L)\n",
    "        return L\n",
    "    else:\n",
    "        data = []\n",
    "        file = open(input(\"Enter file path: \"))\n",
    "        for line in file:\n",
    "            data.append([float(x) for x in line.split()])\n",
    "        return data[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def dec(L):\n",
    "    N = len(L)\n",
    "    len1 = math.ceil(math.sqrt(N))\n",
    "    B = [0]*len1\n",
    "    for i in range(N):\n",
    "        B[i // len1] += L[i]        #определение суммы каждого блока длиной корень из длины массива\n",
    "    print(\"B = \", B)\n",
    "    print('Enter indexes')\n",
    "    i = int(input())\n",
    "    r = int(input())\n",
    "    Sum = 0\n",
    "    while i <= r:\n",
    "        if i % len1 == 0 and i + len1 - 1 <= r:     #к сумме прибавляется значение блока если блок входит в промежуток\n",
    "            Sum += B[i // len1]\n",
    "            i += len1\n",
    "        else:\n",
    "            Sum += L[i]      #иначе (в конце) к сумме прибавляются слагаемые покомпонентно\n",
    "            i += 1\n",
    "    print('Sum = ' + str(Sum))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#запуск функции и взаимодействие с пользователем\n",
    "a = 1\n",
    "while(a != 'c'):\n",
    "    a = input('Type a to load a file or b to enter array (c to exit): ')\n",
    "    if a == 'a' or a == 'b':\n",
    "        B = arr(a)\n",
    "        dec(B)\n",
    "    elif a == 'c':\n",
    "        continue\n",
    "    else:\n",
    "        print(\"Wrong input\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
