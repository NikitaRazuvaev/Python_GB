with open('poly1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')
