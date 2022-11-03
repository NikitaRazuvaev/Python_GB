from models import creat_csv 
from models import creat_json
from models import creat_txt


def reading_file():
    input_option = int(input("Выбирите формат файла:\n 1.СSV \n 2.JSON \n 3.TXT \n"))
    if input_option == "1":
        creat_csv()
    elif input_option == "2":
        creat_json()
    elif input_option == "3":
        creat_txt()