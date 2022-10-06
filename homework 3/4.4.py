
def input_number(msg):
    while True:
        try:
            number=int(input(msg))
            return number
        except ValueError: 
            print("Введенно не число")
            

number = input_number('Введите 10-чное число: ')
container_for_leftovers = ''

while number > 0:
    container_for_leftovers = str(number % 2) + container_for_leftovers
    number = number // 2 
print(f'В двоичном виде: {container_for_leftovers}')
