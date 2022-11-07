import csv
from creatinfo import get_info

global filename 

filename = 'homework 8/file/list_phone.csv'

# Запись файла csv

def create_csv():
    info = get_info()
    
    with open(filename,'a') as file:
        file = csv.DictWriter(file, fieldnames=['Фамилия: ','Имя: ','Телефон: ','Описание: '], delimiter = ",", lineterminator="\r")
        file.writeheader()
        file.writerow({'Фамилия: ': info[0],'Имя: ': info[1],'Телефон: ':info[2],'Описание: ':info[3]})
        
        print('Сотрудник сохранен')

def read_csv():
    with open(filename, 'r') as file:
        content = csv.reader(file, delimiter = ",", lineterminator="\r")
        for line in content:
            print(line)
