# 5.8. Здравствуйте, админ! Создайте список из пяти и более имен пользователей,
# содержащий имя 'admin'. Представьте, что пишете код, который выводит
# приветственное сообщение для каждого пользователя после его входа на сайт.
# Переберите элементы списка и выведите сообщение для каждого пользователя:
# • для пользователя 'admin' выведите особое сообщение: например, «Здравствуйте,
# admin, хотите просмотреть отчет о состоянии дел?»;
# • в остальных случаях выводите универсальное приветствие: например,
# «Привет,Денис, спасибо, что авторизовался в системе».

users = ['admin', 'user1', 'user2', 'user3', 'user4']

current_user = 'user11'

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