# Задайте список из нескольких чисел. Напишите программу, которая найдет сумму элементов списка, стоящих на нечётных позиции.
from operator import index

size_list=int(input('Введите размер списка: '))
list = [] 
sum_list = 0
for i in range(size_list):
   number_list=int(input(f'Введите число {i+1}: '))
   list.append(number_list)
   if i % 2 !=0:
        sum_list += list[i]
print(list)
print(f'Сумма нечетных чисел равно {sum_list}')
