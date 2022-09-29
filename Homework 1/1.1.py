# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def input_number(msg):
    t=True
    while t:
        try:
            number=int(input(msg))
            if number < 1 or number > 7:
                print("Число не в рамках недели")
            else:
                t=False
        except:
            print("Введенно не число")
    return number

a = input_number('Введите цифру неделею:')
if a == 6 or a == 7:
    print("Да")
else:
    print("Нет")