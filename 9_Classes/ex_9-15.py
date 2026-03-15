# 9.15. Анализ лотереи. Напишите цикл, который проверяет, насколько
# сложно выиграть в смоделированной вами лотерее. Создайте список или кортеж
# my_ticket. Напишите цикл, который продолжает генерировать комбинации до тех
# пор, пока не выпадет выигрышная комбинация. Выведите сообщение с информацией
# о том, сколько выполнений цикла понадобилось для получения выигрышной
# комбинации.

from random import choice

hex = [i for i in range(0,10)]
hex.append('a')
hex.append('b')
hex.append('c')
hex.append('d')
hex.append('e')
win_number = ''
my_ticket = 'dab9'
try_number = 0

while my_ticket != win_number:
    win_number = ''
    try_number += 1
    for i in range(0, 4):
        win_number = f'{win_number}{choice(hex)}'

print(f'Лотерея выиграна с {try_number} попытки.')
