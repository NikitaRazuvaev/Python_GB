from models_SQL import is_auntificated
from model_csv import create_csv, read_csv
import os


print(f'Добро пожаловать в базу данных сотрудников. \nАвторизуйтесь в системе для дальнейшей работы')


if is_auntificated():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print('------МЕНЮ------\n1. Создать сотрудника \n2. Показать сотрудников\n3. Выход\n')
        chose = int(input('Введите номер меню: '))
        if chose == 1:
            create_csv()
        elif chose == 2:
            read_csv()
        elif chose == 3:
            break




    

    
