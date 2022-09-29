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
    print("x > 0 , y > 0 ")
elif n == 2:
    print("x < 0 , y > 0 ")
elif n == 3:
    print("x < 0 , y < 0 ")
else:
    print("x > 0 , y < 0 ")
    