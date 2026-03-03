# 9.5. Попытки входа. Добавьте атрибут login_attempts в класс User из
# упражнения 9.3. Напишите метод increment_login_attempts(), увеличивающий
# значение login_attempts на 1. Напишите еще один метод,
# reset_login_attempts(),обнуляющий значение login_attempts. Создайте
# экземпляр класса User и вызовите increment_login_attempts() не-сколько раз.
# Выведите значение login_attempts, чтобы убедиться в том, что значение было
# изменено правильно, а затем вызовите reset_login_attempts().Снова выведите
# login_attempts и убедитесь в том, что значение обнулилось.

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
        self.login_attempts = 0

user1 = User('Геннадий', 'Иванов', 'gena', '1234', 'gena@ivanov.com')
user2 = User('Name2','lastname2','username2','password2','e@mail.2')
user3 = User('Name3','lastname3','username3','password3','e@mail.3')

User.describe_user(user1)
User.describe_user(user2)
User.describe_user(user3)

User.greet_user(user1)
User.greet_user(user2)
User.greet_user(user3)

User.increment_login_attempts(user3)
User.increment_login_attempts(user3)
User.increment_login_attempts(user3)
User.increment_login_attempts(user3)
User.describe_user(user3)
User.reset_login_attempts(user3)
User.describe_user(user3)
