# 9.9. Обновление аккумулятора. Используйте окончательную версию
# программы electric_car.py из этого раздела. Добавьте в класс Battery метод
# upgrade_battery(). Он должен проверять размер аккумулятора и устанавливать
# мощность равной 65, если она имеет другое значение. Создайте экземпляр
# электромобиля с аккумулятором по умолчанию, вызовите get_range(), а затем
# вызовите его еще раз после upgrade_battery(). Убедитесь в том, что запас
# хода увеличился.

class Car:
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит данные о пробеге машины в милях."""
        print(f"Эта машина проехала {self.odometer_reading} километров.")

    def update_odometer(self, km):
        """Устанавливает на одометре заданное значение."""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Вы не можете скручивать пробег!")

    def increment_odometer(self, kms):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += kms

class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self,battery_size=40):
        """Инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f'Мощность батареи {self.battery_size} кВт.')

    def update_battery(self):
        """Метод для сброса значения размера батареи."""
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя. Затем инициализирует атрибуты,
        специфические для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()

car1 = ElectricCar('nissan', 'leaf', 2024)
print(car1.get_descriptive_name())
print(car1.battery.describe_battery())
car1.battery.update_battery()
print(car1.battery.describe_battery())
