def get_info():
    
    info =[]
    surname = input("Введите фамилию: ")
    info.append(surname)
    name = input("Введите имя: ")
    info.append(name)
    phone_number = input("Введите телефон: ")
    valid = True
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    print('Сотрудник веден!')
    return info
