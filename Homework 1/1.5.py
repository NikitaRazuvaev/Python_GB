from cmath import sqrt


def input_number(msg):
    t=True
    while t:
        try:
            number=float(input(msg))
            t=False
        except:
            print("Введенно не число")
    return number


x1 = input_number('Координата x1: ')
y1 = input_number('Координата y1: ')
x2 = input_number('Координата x2: ')
y2 = input_number('Координата y2: ')

l = sqrt((x1-x2)**2 + (y1-y2)**2)
print(f"Длинна между точками: {l}")