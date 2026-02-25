# 8.12. Бутерброды. Напишите функцию, которая получает список
# компонентов бутерброда. Функция должна иметь один параметр для любого
# количества значений, переданных при вызове функции, и выводить описание
# заказанного бутерброда. Вызовите функцию три раза с разными количествами
# аргументов.

def make_burger(*burger_components):
    print('This burger contains:')
    for burger_component in burger_components:
        print(f'- {burger_component}')

make_burger('cheese', 'tomatoes', 'beef', 'cucumber', 'pepper')
make_burger('cheese', 'beef')
make_burger('cheese', 'beef', 'cucumber')

