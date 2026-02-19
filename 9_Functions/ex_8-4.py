# 8.4. Большие футболки. Измените функцию make_shirt(), чтобы футболки
# по умолчанию имели размер L и на них выводился текст «Я люблю Python».
# Создайте футболку с размером L и текстом по умолчанию, а также футболку
# любого раз-мера с другим текстом.

def make_shirt(size='L',text='I love Python'):
    print(f'Shirt of {size} size with text "{text}" was created.')

make_shirt()
make_shirt('XXL','Test')