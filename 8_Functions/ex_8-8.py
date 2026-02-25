# 8.7. Альбом. Напишите функцию make_album(), которая создает словарь с
# описанием музыкального альбома. Функция должна получать имя исполнителя и
# на-звание альбома и возвращать словарь, содержащий эти два вида
# информации. Используйте функцию для создания трех словарей, представляющих
# разные альбомы. Выведите все возвращаемые значения, чтобы показать,
# что информация правильно сохраняется во всех трех словарях. Глава 8. Функции
# 179Добавьте в make_album() дополнительный параметр для сохранения
# количества дорожек в альбоме, имеющий значение по умолчанию None. Если в
# строке вызова есть значение количества дорожек, то добавьте это значение в
# словарь альбома. Создайте как минимум один новый вызов функции, который
# передает количество дорожек в альбоме.
#
# 8.8. Пользовательские альбомы. Начните
# с программы из упражнения 8.7. Напишите цикл while, в котором пользователь
# вводит данные об исполните-ле и название альбома. Затем в цикле вызывается
# функция make_album() для введенных пользователем данных и выводится
# созданный словарь. Не забудьте предусмотреть признак завершения в цикле while.

def make_album(artist_name,album_name,tracks = ''):
    album = {'Artist name': artist_name,'Album name': album_name}
    if tracks:
        album['Tracks'] = tracks
    return album

while True:
    user_input_artist_name = input('Enter Artist name or "q" for quit: ')
    if user_input_artist_name.lower() == 'q':
        break
    user_input_album_name = input('Enter Album name: ')
    user_input_tracks = input('Enter tracks number (Optional): ')

    if user_input_tracks:
        current_album = make_album(user_input_artist_name,user_input_artist_name,user_input_tracks)
    else:
        current_album = make_album(user_input_artist_name,user_input_album_name)

    print(current_album)