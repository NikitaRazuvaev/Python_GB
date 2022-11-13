from tkinter import *
from decimal import *
import math


##Интерфейс 
root = Tk()
root.title("Калькулятор")


buttons = (('7','8','9','/','','5'),
           ('4','5','6','*','','5'),
           ('1','2','3','-','log'),
           ('0','.','=','+','ln'),
           )
activeStr = ''
stack = []

def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label_calc.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label_calc.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label_calc.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label_calc['text'])
            operation()
            stack.clear()
            stack.append(label_calc['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label_calc['text'])
                stack.append(text)
                activeStr = ''
                label_calc.configure(text='0')

label_calc = Label(root, text='0', width=35)

def operation():
    global stack
    global label_calc
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())
#Сложение
    if operation =='+':
        result = operand1 + operand2
#Вычитание
    if operation =='-':
        result = operand1 - operand2
#Деление
    if operation =='/':
        result = operand1 / operand2
#Умножение
    if operation =='*':
        result = operand1 * operand2
#Десятичный логарифм
    if operation =='log':
        result = math.log10(operand2)
#Натуральный логарифм
    if operation == 'ln':
        result = math.log(operand2)
    label_calc.configure(text=str(result))
label_calc.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='CE', command=lambda text='CE': click(text),fg = 'white', bg='LightSkyBlue')
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(5):
        button = Button(root, text=buttons[row][col],
                command=lambda row=row, col=col: click(buttons[row][col]),fg = 'black', bg='LightBlue')
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()

