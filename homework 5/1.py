
from codecs import utf_8_decode
from encodings import utf_8
from traceback import print_tb


input_text = ""
with open("C:/Users/niki/Documents/GitHub/Python_GB/homework 5/file.txt", 'r',encoding='utf_8') as file :
    input_text= file.read()
    print(f'Исходный текст: {input_text}')
tokens = input_text.split(" ")
tokens = list(filter(lambda x: not x.__contains__("абв"), tokens ))
print(f'Обработанный текст: {tokens}')
