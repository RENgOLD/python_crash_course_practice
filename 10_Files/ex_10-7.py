# 10.7. Калькулятор. Поместите код из упражнения 10.5 в цикл while,
# чтобы пользователь мог продолжать вводить числа, даже если допустил ошибку и
# ввел текст вместо числа.

while True:
    try:
        first_int = int(input('Введите первое число: '))
    except ValueError:
        pass
    else:
        break

while True:
    try:
        second_int = int(input('Введите второе число: '))
    except ValueError:
        pass
    else:
        break

result = first_int + second_int
print(f'{first_int} + {second_int} = {result}')