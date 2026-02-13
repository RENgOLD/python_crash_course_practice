# 6.7. Люди.
# Начните с программы, написанной для упражнения 6.1.
# Создайте два новых словаря, представляющих разных людей, и сохраните все три
# словаря в списке people. Переберите элементы списка людей. В процессе перебора
# вы-ведите всю имеющуюся информацию о каждом человеке.


people = {
    'human1': {
        'first_name': 'John',
        'last_name': 'Wick',
        'age': 52,
        'city': 'New York'
    },
    'human2': {
        'first_name': 'Bruce',
        'last_name': 'Wayne',
        'age': 40,
        'city': 'Gotham'
    },
    'human3': {
        'first_name': 'Tony',
        'last_name': 'Stark',
        'age': 35,
        'city': 'New York'
    }
}

for human, human_info in people.items():
    print(f'\n{human}:')
    for k, v in human_info.items():
        print(f'{k}: {v}')