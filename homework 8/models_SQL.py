import sqlite3

#Работа с таблицами создание, удаление,проверка

#Регистрация пользователя

global db
global sql

db = sqlite3.connect('homework 8/file/profil.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    numgroup BIGINT
) """)
db.commit()

def get_creds():
    user_login = input('Login: ')
    user_password = input('Password: ')
    return user_login, user_password

def regist():
    user_login, user_password = get_creds()

    sql.execute("SELECT login FROM users")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)",(user_login, user_password,0))
        db.commit()
        print('Зарегистрировано! ')
    else:
        print('Такая запись уже есть!')

        for value in sql.execute("SELECT * FORM users"):
            print(value)

#Авторизация
def is_auntificated():
    user_login, user_password = get_creds()

    sql.execute(f'SELECT login FROM users WHERE login  = "{user_login}" AND password = "{user_password}"') 
    if sql.fetchone() is None:
        print('Такого пользователя не существует. Доступ закрыт')
        ConnectionAbortedError()
    else:
        return True

