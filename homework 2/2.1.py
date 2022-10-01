# Задача: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

real_number = float(input("Введите число: "))
#Переменная для значения суммы
sum = 0                                 
#Если введенное число отрицательное
real_number=abs(real_number)
#Функция если число имеет дробную часть и перевод числа из float в int 
while not real_number.is_integer():  
    real_number=real_number*10
#Ход выполнения задачи:
while real_number != 0:
    p = real_number % 10
    sum=sum+p
    real_number= real_number // 10
print(sum)