def input_number(msg):
    while True:
        try:
            number=int(input(msg))
            return number
        except ValueError: 
            print("Введенно не число")
            

size_list=input_number('Введите размер списка: ')
list = [] 
list2 =[]

for i in range(size_list):
   number=float(input(f'Введите число {i+1}: '))
   list.append(number)

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        composition = list[i] * list[number]
        list2.append(composition)
        i +=1

print(list)
print(list2)

