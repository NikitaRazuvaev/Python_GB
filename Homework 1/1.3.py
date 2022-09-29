def input_number(msg):
    t=True
    while t:
        try:
            number=float(input(msg))
            if number == 0:
                print("Координата не может равна 0")
            else:
                t=False
        except:
            print("Введенно не число")
    return number


x = input_number('Координата x: ')
y = input_number('Координата y: ')
if x > 0 and y > 0:
    print('I')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
else:
    print('IV')