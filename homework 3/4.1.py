# Задайте список из нескольких чисел. Напишите программу, которая найдет сумму элементов списка, стоящих на нечётных позиции.

def input_number(msg):
    while True:
        try:
            number=int(input(msg))
            return number
        except ValueError: 
            print("Введенно не число")
            
    


size_list= input_number('Введите размер списка: ')
list = [] 
sum_list = 0
for i in range(size_list):
   number_list=int(input(f'Введите число {i+1}: '))
   list.append(number_list)
   if i % 2 !=0:
        sum_list += list[i]
print(list)
print(f'Сумма нечетных чисел равно {sum_list}')
