def input_number(msg):
    t=True
    while t:
        try:
            number=int(input(msg))
            if number < 1:
                print("Число не натуральное")
            else:
                t=False
        except ValueError:
            print("Введенно не число")
    return number

n= input_number('Введите натуральное число N: ')
current=n
list_simple_multipliers=[]
i=2
while i <= current:
    if current % i == 0: 
        list_simple_multipliers.append(i)
        current //=i
    else:
        i+=1

print(f"Простые множители числа {n} в списке: {list_simple_multipliers}")

