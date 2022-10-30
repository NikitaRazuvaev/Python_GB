# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
###----------------------------------------------------------------------
###input_text = ""
#with open("file.txt", 'r',encoding='utf_8') as file :
#    input_text= file.read()
#    print(f'Исходный текст: {input_text}')

#pack = ''
#i=0 
#while i < len(input_text):
#    ln = 9
#    found = False
#    while not found and ln>3:
#        j = i - ln
#        while j >= 0 and (i-j) <100:
#            if input_text[i:i+ ln] == input_text[j:j + ln]:
#                pack += '%1d%2d' % (ln,(i-j))
#                i+= ln
#                found = True
#               break
#            j -= 1
#        ln -= 1
#    if not found: 
#        pack += input_text[i]
#        i+=1
#print(f'Обработанный текст: {pack}')
#unpack = ''
#i=0 
#while i < len(pack):
#    if pack[i] != '#':
#        unpack += input_text[i]
#        i+=1
#        continue
#    ln = int(pack[i+1: i+2])
#    dist = int(pack[i+2: i+4])
#    unpack += unpack[-dist: -dist+ln]
#    i += 4
#print(f'Обработанный текст: {unpack}')
#if input_text != unpack:
#    print('!!!!!!!!!!!!')
###----------------------------------------------------------------------

input_text = ""
with open("file.txt", 'r',encoding='utf_8') as file :
    input_text= file.read()
    print(f'Исходный текст: {input_text}')

tokens = []
last_letter = ''
count = 0
for letter in input_text:
    if last_letter != letter :
        if last_letter != '' :
            tokens.append((last_letter, count))
        last_letter = letter
        count = 0
    count +=1
tokens.append((last_letter, count))
pack = ''.join(map(lambda x: x[0] + str(x[1]), tokens))

print(f'Обработанный текст: {pack}')

tokens = []
last_letter = ''
count = 0
for letter in pack:
    if not letter.isnumeric():
        if last_letter != '':
            tokens.append((last_letter, count))
        last_letter = letter
        count = 0
    else:    
        count = count * 10 + int(letter)         
tokens.append((last_letter, count))    
unpack = ''.join(map(lambda x: x[0] * x[1], tokens))

print(f'Обработанный текст: {unpack}')
if input_text != unpack:
    print('!!!!!!!!!!!!')
