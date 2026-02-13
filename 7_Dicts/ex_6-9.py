# 6.9. Любимые места. Создайте словарь favorite_places. Придумайте
# названия трех мест, которые станут ключами словаря, и сохраните для каждого
# человека из упражнения 6.7 от одного до трех любимых мест. Чтобы задача
# стала более интересной, опросите нескольких друзей и соберите реальные
# данные для своей программы. Переберите данные в словаре, выведите имя
# каждого человека и его любимые места.

people = {
    'human1': {
        'first_name': 'John',
        'last_name': 'Wick',
        'age': 52,
        'city': 'New York',
        'favorite_places': ['Home', 'Continental']
    },
    'human2': {
        'first_name': 'Bruce',
        'last_name': 'Wayne',
        'age': 40,
        'city': 'Gotham',
        'favorite_places': ['Cave']
    },
    'human3': {
        'first_name': 'Tony',
        'last_name': 'Stark',
        'age': 35,
        'city': 'New York',
        'favorite_places': ['Avengers Tower','Stark Enterprises','Workshop']
    }
}

for human, human_info in people.items():
    print(f'\n{human_info['first_name']} {human_info['last_name']} favourite places:')
    for place in human_info['favorite_places']:
        print(place)