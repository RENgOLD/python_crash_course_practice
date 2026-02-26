# 9.3. Пользователи. Создайте класс User и два атрибута first_name и
# last_name, а затем еще несколько атрибутов, которые обычно хранятся в
# профиле пользователя. Напишите метод describe_user(), который выводит
# сводку с информацией о пользователе. Создайте еще один метод — greet_user(),
# позволяющий вывести персональное приветствие для пользователя. Создайте
# несколько экземпляров, представляющих разных пользователей. Вызовите оба
# метода для каждого пользователя.

class User:
    """Класс, описывающий пользователя."""

    def __init__(self, first_name, last_name, username, password, email):
        """Метод инициализации атрибутов пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email

    def describe_user(self):
        """Метод, выводящий информацию о пользователе"""
        print(f'Данные пользователя {self.username}:\n'
              f'  Пароль: {self.password}\n'
              f'  Имя: {self.first_name}\n'
              f'  Фамилия:{self.last_name}\n'
              f'  email: {self.email}\n')

    def greet_user(self):
        """Метод, выводящий персональное приветствие пользователя"""
        print(f'Здравствуйте, {self.first_name}!')

user1 = User('Геннадий', 'Иванов', 'gena', '1234', 'gena@ivanov.com')
user2 = User('Name2','lastname2','username2','password2','e@mail.2')
user3 = User('Name3','lastname3','username3','password3','e@mail.3')

User.describe_user(user1)
User.describe_user(user2)
User.describe_user(user3)

User.greet_user(user1)
User.greet_user(user2)
User.greet_user(user3)
