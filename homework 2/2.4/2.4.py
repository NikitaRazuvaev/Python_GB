import numbers
from random import randint


numbers=[]
for i in range(10):
    numbers.append(randint(-10,10))
print(numbers)

def get_numbers(numbers):
    count= 0
    for element in numbers:
        count +=1
    return count
print("Количество элементов:", get_numbers(numbers))
file = open( 'file.txt', 'r')
x = int(file.readline())
y = int(file.readline(2))

for i in range(len(numbers)):
    mult = numbers[x - 1] * numbers[y-1]
print(f'Множество элементов: {numbers[x-1]} * {numbers[y-1]} =', mult )