# 10.4. Гость. Напишите программу, которая запрашивает у пользователя его
# имя. Введенный ответ сохраняется в файле guest.txt.

from pathlib import Path

user_name = input("Введите имя пользователя: ")
path = Path('guest.txt')
path.write_text(user_name)
