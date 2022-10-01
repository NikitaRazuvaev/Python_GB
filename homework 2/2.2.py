#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
number_num = int(input("Введите число N: "))
factorial = 1
result=[]
for i in range(1, number_num+1):
     factorial *= i
     result.append(factorial) 
print(result)