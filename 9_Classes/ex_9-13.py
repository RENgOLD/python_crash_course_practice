# 9.13. Игра в кости. Создайте класс Die с одним атрибутом sides, который
# имеет значение по умолчанию 6. Напишите метод roll_die() для вывода
# случайного числа от 1 до количества граней на кубике. Создайте экземпляр,
# представляющий шестигранный кубик, и смоделируйте десять бросков. Создайте
# экземпляры, представляющие 10- и 20-гранный кубик. Смоделируйте десять
# бросков каждого кубика.

from random import randint

class Die:
    """Класс для кубика"""

    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        current_roll = randint(1,self.sides)
        print(f'Кубик с числом граней - {self.sides} был брошен и выпало - {current_roll}.')

Die6 = Die(6)
Die10 = Die(10)
Die20 = Die(20)

for i in range(0,10):
    Die6.roll_die()

for i in range(0,10):
    Die10.roll_die()

for i in range(0,10):
    Die20.roll_die()