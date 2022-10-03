#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
number_num = int(input("Введите число N: "))

def sequence(numbeer_num):
    return[((1 + 1 / x)**x, 2) for x in range (1, number_num + 1)] 
print(sequence(number_num))
print(round(sum(sequence(number_num))))