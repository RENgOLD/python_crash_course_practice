# 10.14. Проверка пользователя. Последняя версия remember_me.py
# предполагает, что пользователь либо уже ввел свое имя, либо программа
# выполняется впервые. Ее нужно изменить на тот случай, если текущий
# пользователь не является тем человеком, который использовал программу
# последним. Прежде чем выводить приветствие в greet_user(), спросите
# пользователя, правильно ли определено его имя. Если ответ будет
# отрицательным, то вызовите get_new_username() для получения правильного
# имени пользователя.

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
        if input(f'Are you {user['name']}? Enter "y" for yes: ').lower() == 'y':
            print(f"Welcome back, {user['name']}! ({user['age']} years old, "
                  f"from {user['country']})")
        else:
            user = get_new_userdata(path)
    else:
        user = get_new_userdata(path)
        print(f"We'll remember you when you come back, {user['name']}!")

greet_user()