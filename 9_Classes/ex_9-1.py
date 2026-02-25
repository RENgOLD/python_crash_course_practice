# 9.1. Ресторан. Создайте класс Restaurant. Его метод __init__() должен
# содержать два атрибута: restaurant_name и cuisine_type. Создайте метод
# describe_restaurant(), который выводит два атрибута, и метод
# open_restaurant(),который выводит сообщение о том, что ресторан
# открыт. Создайте на основе своего класса экземпляр restaurant. Выведите два
# атрибута по отдельности, затем вызовите оба метода.
from pydoc import describe


class Restaurant:
    """Метод, описывающий ресторан."""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует параметры имени и типа кухни ресторана."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Вывод описания ресторана."""
        print(f'Ресторан: {self.restaurant_name}. Кухня: {self.cuisine_type}')

    def open_restaurant(self):
        """Вывод сообщения об открытии ресторана."""
        print('Ресторан открыт.')

rest1 = Restaurant('Пиццерия','Итальянская')
Restaurant.describe_restaurant(rest1)
Restaurant.open_restaurant(rest1)
