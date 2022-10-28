# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
input_text = ""
with open("file.txt", 'r',encoding='utf_8') as file :
    input_text= file.read()
    print(f'Исходный текст: {input_text}')

pack = ''
i=0 
while i < len(input_text):
    ln = 9
    found = False
    while not found and ln>3:
        j = i - ln
        while j >= 0 and (i-j) <100:
            if input_text[i:i+ ln] == input_text[j:j + ln]:
                pack += '%1d%2d' % (ln,(i-j))
                i+= ln
                found = True
                break
            j -= 1
        ln -= 1
    if not found: 
        pack += input_text[i]
        i+=1
print(f'Обработанный текст: {pack}')
unpack = ''
i=0 
while i < len(pack):
    if pack[i] != '#':
        unpack += input_text[i]
        i+=1
        continue
    ln = int(pack[i+1: i+2])
    dist = int(pack[i+2: i+4])
    unpack += unpack[-dist: -dist+ln]
    i += 4
print(f'Обработанный текст: {unpack}')
if input_text != unpack:
    print('!!!!!!!!!!!!')