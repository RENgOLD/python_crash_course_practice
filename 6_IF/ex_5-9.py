# 5.9. Нет пользователей.
# Добавьте в программу hello_admin.py оператор if,который проверит, что список
# пользователей не пуст.
# • Если список пуст, то выведите сообщение «Нам нужно добавить несколько
# пользователей!»
# • Удалите из списка все имена пользователей и убедитесь в том, что программа
# выводит правильное сообщение.

users = ['admin', 'user1', 'user2', 'user3', 'user4']
#users = []
current_user = 'user11'

if users:
    if current_user in users:
        if current_user == 'admin':
            print("message for admin")
        if current_user == 'user1':
            print("message for user1")
        if current_user == 'user2':
            print("message for user2")
        if current_user == 'user3':
            print("message for user3")
        if current_user == 'user4':
            print("message for user4")
    else:
        print("unknown user")
else:
    print("no users")