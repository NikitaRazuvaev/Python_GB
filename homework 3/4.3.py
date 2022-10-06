def input_number_float(msg):
    while True:
        try:
            number=float(input(msg))
            return number
        except ValueError: 
            print("Введенно не число")
            

def get_frac(num):

    return num - int(num)
    
list = []
size_list= input_number_float('Введите размер списка: ')

for i in range(size_list):
   number=float(input(f'Введите число {i+1}: '))
   list.append(number)
min_num=get_frac(list[0])
max_num=get_frac(list[0])
for i in range(len(list)):
    if max_num < get_frac(list[i]):
        max_num = get_frac(list[i])
    if min_num > get_frac(list[i]):
       min_num = get_frac(list[i])
calc_list=(max_num - min_num)
print(f'{list} => {str(calc_list)[:4]}')