# 7.8. Бутерброды. Создайте список sandwich_orders, заполните его
# названиями различных видов бутербродов. Создайте пустой список
# finished_sandwiches.В цикле переберите элементы первого списка и выведите
# сообщение для каждого элемента (например, «Я приготовил бутерброд с
# тунцом»). После этого каждый бутерброд из первого списка перемещается в
# список finished_sandwiches. После того как все элементы первого списка будут
# обработаны, выведите сообщение,в котором перечисляются все изготовленные
# бутерброды.

sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3', 'sandwich4',
                    'sandwich5']
finished_sandwitches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwitches.append(current_sandwich)
    print(f'{current_sandwich} is done.')

print('All sandwiches is done.')