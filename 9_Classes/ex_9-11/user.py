class User:
    """Класс, описывающий пользователя."""

    def __init__(self, first_name, last_name, username, password, email):
        """Метод инициализации атрибутов пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Метод, выводящий информацию о пользователе"""
        print(f'Данные пользователя {self.username}:\n'
              f'  Пароль: {self.password}\n'
              f'  Имя: {self.first_name}\n'
              f'  Фамилия:{self.last_name}\n'
              f'  email: {self.email}\n'
              f'  Попыток входа: {self.login_attempts}\n')

    def greet_user(self):
        """Метод, выводящий персональное приветствие пользователя"""
        print(f'Здравствуйте, {self.first_name}!')

    def increment_login_attempts(self):
        """Увеличивает количество попыток"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Обнуляет количество попыток входа"""
        self.login_attempts = 0

class Admin(User):
    """Класс, описывающий администратора"""
    def __init__(self, first_name, last_name, username, password, email):
        """Инициализация класса администратора"""
        super().__init__(first_name, last_name, username, password, email)
        self.privileges = Privileges()

class Privileges:
    """Класс, описывающий привилегии администратора"""
    def __init__(self,privileges='read'):
        """Инициализация класса привилегий"""
        self.privileges = privileges

    def show_privileges(self):
        """Вывод информации о текущих привилегиях администратора"""
        print(f'Права администратора: {self.privileges}')