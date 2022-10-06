def input_number(msg):
    positive_value=True
    while positive_value:
        try:
            number=float(input(msg))
            t=False
        except:
            print("Введенно не число")
    return number

def get_frac(num):

    return num - int(num)
    
list = []
size_list=int(input('Введите размер списка: '))

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