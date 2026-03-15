# 9.14. Лотерея. Создайте список или кортеж, содержащий серию из десяти
# чисел и пяти букв. Случайным образом выберите четыре числа или буквы из
# списка. Выведите сообщение о том, что билет, содержащий эту комбинацию из
# четырех цифр или букв, является выигрышным.

from random import choice

hex = [i for i in range(0,10)]
hex.append('a')
hex.append('b')
hex.append('c')
hex.append('d')
hex.append('e')
win_number = ''

for i in range(0,4):
    win_number = f'{win_number}{choice(hex)}'

print(win_number)