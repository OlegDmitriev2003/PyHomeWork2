import os
clear = lambda: os.system('cls')
clear()

length = int(input('Введите длинну последовательности: '))
a = int(input('Введите первый элемент последовательности: '))
d = int(input('Введите разность последовательности: '))

progression = [0]*length

for i in range (a, length):
    progression[i] = (a + (i-1) * d)
    print (progression[i])