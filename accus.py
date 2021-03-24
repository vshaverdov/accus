import numpy as np
ageall = [20, 25, 18, 27]

# Создаём словари account
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

# Создаём словари user
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

# Создаём список 
user_list = [user1, user2, user3, user4] 

# Выводим 
enter = input('Введите ключ (name или account): ').lower()


try:
    print(f'значение ключа {enter} для юзера 1 = {user1[enter]}')
    print(f'значение ключа {enter} для юзера 2 = {user2[enter]}')
    print(f'значение ключа {enter} для юзера 3 = {user3[enter]}')
    print(f'значение ключа {enter} для юзера 4 = {user4[enter]}')
except KeyError: 
    print('Введенный ключ не найден')

enter_number = input('Введите порядковый номер: ')
users = user_list[int(enter_number)-1]


try:
    print(f'Данные по юзеру №: {enter_number}')
    print(f'Имя: {users["name"]}')
    print(f'Возраст: {users["age"]}')
    print(f'Логин: {users["account"]["login"]}')
    print(f'Пароль: {users["account"]["password"]}')
    print(f'Средний возраст пользователей: {np.mean(ageall)}' ) 

except ValueError:
    print('Пользователь с указанным номером не найден.')

enter_end = input('Введите номер пользователя, которого нужо переместить в конец: ')


print(f'Список до измения: {user_list}')
new_user = user_list.pop(int(enter_end)-1)
user_list.append(new_user)
print(f'Список после измения: {user_list}')
