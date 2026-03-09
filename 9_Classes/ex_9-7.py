# 9.7. Администратор. Администратор — особая разновидность
# пользователя. Напишите класс Admin, наследуемый от класса User из упражнения
# 9.3 или 9.5. Добавьте атрибут privileges для хранения списка строк вида
# "разрешено добавлять сообщения", "разрешено удалять пользователей",
# "разрешено банить пользователей" и т. д. Напишите метод show_privileges()
# для вывода набора привилегий администратора. Создайте экземпляр Admin и
# вызовите свой метод.

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

class Admin(User):

    def __init__(self, first_name, last_name, username, password, email, privileges):
        super().__init__(first_name, last_name, username, password, email)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


admin1 = Admin("AdminName","AdminLastName","Admin","AdminPassword","Admin@email.com","canBan")
admin1.describe_user()
admin1.show_privileges()
