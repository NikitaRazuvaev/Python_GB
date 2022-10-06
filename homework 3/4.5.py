def input_number(msg):
    while True:
        try:
            number=int(input(msg))
            return number
        except ValueError: 
            print("Введенно не число")
            
def get_index(i, size_list):
    return  size_list + 1 + i

size_list=input_number('Введите размер списка: ')
list = [None] * (size_list * 2 +2)
list[get_index(-2, size_list)] = -1
list[get_index(-1, size_list)] = 1
list[get_index(0, size_list)] = 0
list[get_index(1, size_list)] = 1
list[get_index(2, size_list)] = 1

for i in range(3, size_list+1):
    list[get_index(i, size_list)] = list[get_index(i-1, size_list)] + list[get_index(i-2, size_list)]
for i in range(3, size_list + 1):
    list[get_index(-i, size_list)] = list[get_index(-i+2, size_list)] - list[get_index(-i+1, size_list)]

for i in range(-size_list, size_list+1):
    print(list[get_index(i, size_list)])