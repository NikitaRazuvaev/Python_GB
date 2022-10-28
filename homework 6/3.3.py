import os 

# Инициализация карты

def clear_console():
    os.system('clear||cls')

maps = [1,2,3,
        4,5,6,
        7,8,9]
 
# Инициализация победных линий
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
# Вывод карты на экран
def print_maps():
    print( f'{maps[0]} {maps[1]} {maps[2]} \n{maps[3]} {maps[4]} {maps[5]} \n{maps[6]} {maps[7]} {maps[8]}')
 
# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
# Получить текущий результат игры
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
    return win
 
# Основная программа
game_over = False
player1 = True

while game_over == False:
 
    # 1. Показываем карту
    print_maps()
 
    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))
    
    clear_console()

    step_maps(step,symbol) # делаем ход в указанную ячейку
    win = get_result() # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
 
# Игра окончена. Покажем карту. Объявим победителя.        
print_maps()
print(f"Победил {win}!")