# 9.4. Посетители. Начните с программы из упражнения 9.1. Добавьте
# атрибут number_served со значением по умолчанию 0; он представляет
# количество об-служенных посетителей. Создайте экземпляр restaurant.
# Выведите значение number_served, потом измените и выведите снова. Добавьте
# метод set_number_served(), позволяющий задать количество обслуженных
# посетителей. Вызовите его с новым числом, снова выведите значение. Добавьте
# метод increment_number_served(), который увеличивает количество
# обслуженных посетителей на заданную величину. Вызовите его с любым числом,
# которое могло бы представлять количество обслуженных клиентов — скажем,
# за один день.

class Restaurant:
    """Метод, описывающий ресторан."""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует параметры имени и типа кухни ресторана."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Вывод описания ресторана."""
        print(f'Ресторан: {self.restaurant_name}. Кухня: {self.cuisine_type}. Обслужено посетителей: {self.number_served}')

    def open_restaurant(self):
        """Вывод сообщения об открытии ресторана."""
        print('Ресторан открыт.')

    def set_number_served(self,number):
        """Установка количества обсуженных посетителей"""
        self.number_served = number

    def increment_number_served(self,number):
        """Увеличивает количество посетителей на заданную величину"""
        self.number_served += number

rest1 = Restaurant('Пиццерия','Итальянская')
Restaurant.describe_restaurant(rest1)

rest1.number_served = 3
Restaurant.describe_restaurant(rest1)

Restaurant.set_number_served(rest1,10)
Restaurant.describe_restaurant(rest1)

Restaurant.increment_number_served(rest1,5)
Restaurant.describe_restaurant(rest1)

Restaurant.open_restaurant(rest1)
