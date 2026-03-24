# 11.3. Штат компании. Напишите класс Employee, представляющий
# работника.Метод __init__() должен получать данные об имени, фамилии и
# ежегодном окладе;все эти значения должны сохраняться в атрибутах. Напишите
# метод give_raise(),который по умолчанию увеличивает ежегодный оклад на 5000
# долларов, но при этом может получать другую сумму прибавки. Напишите тестовый
# сценарий для Employee. Напишите два тестовых
# метода:test_give_default_raise() и test_give_custom_raise(). Используйте
# метод setUp(), чтобы вам не приходилось заново создавать экземпляр Employee
# в каж-дом тестовом методе. Запустите свой тестовый сценарий и убедитесь в
# том, что оба теста прошли успешно.

class Employee:
    """Класс, представляющий работника."""
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.salary = int(salary)

    def give_raise(self,value=5000):
        self.salary += value
        print(f'Salary of employee "{self.firstname} {self.lastname}" increased'
              f' by {value} and now its {self.salary}.')

#empl1 = Employee('first','second','12000')
#empl1.give_raise(7000)