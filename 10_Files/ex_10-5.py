# 10.5. Гостевая книга. Напишите цикл while, который в цикле запрашивает у
# пользователей имена. При вводе каждого имени выведите на экран приветствие и
# добавьте строку с сообщением в файл guest_book.txt. Проследите за тем,
# чтобы каждое сообщение размещалось в отдельной строке файла.

from pathlib import Path
path = Path('guest_book.txt')
user_list = []
file_input = ''

while True:
    user_input = input("Введите имя пользователя или exit для выхода: ")
    if user_input.lower() != 'exit':
        welcome_message = f'Здравствуйте, {user_input}!'
        print(welcome_message)
        user_list.append(welcome_message)
    else:
        break

print(user_list)

for user in user_list:
    file_input += user + '\n'

print(file_input)
path.write_text(file_input, encoding='utf-8')
