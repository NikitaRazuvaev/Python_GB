
from multiprocessing.sharedctypes import Value


size_list=int(input('Введите размер списка: '))
list = [] 
list2 =[]
for i in range(size_list):
   number_list=int(input(f'Введите число {i+1}: '))
   list.append(number_list)

for i in range(len(list)):
    while i<len(list)/2 and number_list > len(list)/2:
        number_list = number_list -1
        composition = list[number_list] * list[i]
        list2.append(composition)
        i +=1

print(list)
print(list2)

