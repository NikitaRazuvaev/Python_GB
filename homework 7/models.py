import csv
import json
from interface import get_info as info


# Запись файла csv
info_pepole = info()
def creat_csv():
    file = 'list_phone.csv'
    with open(file,'a') as file:
        file = csv.writer(file, delimiter = ",", lineterminator="\r")
        file.writerow(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

# Запись файла json
def creat_json():
    file = 'list_phone.json'
    with open(file,'a') as file:
        json.dump(info, file)
        
# Запись файла txt 
def creat_txt():
    file = 'Phonebook.txt'
    with open (file, 'a') as file:
        file.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')    


