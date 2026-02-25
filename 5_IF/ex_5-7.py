# 5.7. Любимый фрукт.
# Составьте список своих любимых фруктов. Напишите серию независимых операторов
# if для проверки того, присутствуют ли некоторые фрукты в списке.
# • Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
# • Напишите пять операторов if. Каждый должен проверять, входит ли определенный
# тип фрукта в список. Если входит, то блок if должен выводить
# сообщение вида «Вы очень любите бананы!»

favorite_fruits = ['apple', 'banana', 'orange']
message = "You love "

if 'apple' in favorite_fruits:
    print(message + 'apple')

if 'banana' in favorite_fruits:
    print(message + 'banana')

if 'orange' in favorite_fruits:
    print(message + 'orange')