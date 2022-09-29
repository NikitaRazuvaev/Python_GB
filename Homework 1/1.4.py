from random import random


def input_number(msg):
    t=True
    while t:
        try:
            number=int(input(msg))
            if number < 1 or number > 4:
                print("Номер четверти от 1 до 4 ")
            else:
                t=False
        except:
            print("Введенно не число")
    return number



n = input_number('Введите номер четверти: ')
if n == 1:
    dx = 1
    dy = 1
elif n == 2:
    dx = -1
    dy = 1
elif n == 3:
    dx = -1
    dy = -1
else:
    dx = 1
    dy = -1
    
for i in range(1,11):
    x = random() * dx
    y = random() * dy
    print(f"({x},{y})")

