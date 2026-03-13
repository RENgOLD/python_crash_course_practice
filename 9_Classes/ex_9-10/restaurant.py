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
        """Установка количества обслуженных посетителей"""
        self.number_served = number

    def increment_number_served(self,number):
        """Увеличивает количество посетителей на заданную величину"""
        self.number_served += number

class IceCreamStand(Restaurant):
    """Класс для киоска с мороженым, наследованный от класса Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Сорт1', 'Сорт2', 'Сорт3', 'Сорт4']

    def print_flavors(self):
        print(f'Доступные сорта мороженого: {self.flavors}')