# 10.13. Словарь пользователя. В программе remember_me.py хранится только один
# вид данных — имя пользователя. Дополните этот пример, запросив еще два вида
# информации о пользователе, а затем сохраните все собранные данные в словарь.
# Запишите его в файл с помощью функции json.dumps() и прочитайте данные с
# помощью функции json.loads(). Выведите сводку, какие именно данные о
# пользователе сохранила ваша программа.

from pathlib import Path
import json
user = {}

def get_stored_user(path):
    """Получает хранимое имя пользователя, если оно существует."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_userdata(path):
    """Запрашивает новое имя пользователя."""
    user['name'] = input("What is your name? ")
    user['age'] = input("What is your age? ")
    user['country'] = input("Where are you from? ")

    contents = json.dumps(user)
    path.write_text(contents)
    return user


def greet_user():
    """Приветствует пользователя по имени."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        print(f"Welcome back, {user['name']}! ({user['age']} years old, "
              f"from {user['country']})")
    else:
        user = get_new_userdata(path)
        print(f"We'll remember you when you come back, {user['name']}!")

greet_user()
