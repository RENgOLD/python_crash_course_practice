# 7.4. Начинки для пиццы.
# Напишите цикл, который предлагает пользователю
# вводить начинки для пиццы до тех пор, пока не будет введено значение 'quit'.
# При вводе каждой начинки выведите сообщение о том, что она добавлена в заказ.


pizza_toppings = []
user_input = ''
while True:
    user_input = input('Input pizza topping: ')
    if user_input.lower() != 'quit':
        pizza_toppings.append(user_input)
    else:
        break

print(pizza_toppings)
