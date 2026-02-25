# 4.12. Больше циклов. Во всех версиях foods.py из этого раздела мы избегали
# использования цикла for при выводе для экономии места. Выберите версию
# foods.py и напишите два цикла for для вывода каждого списка.

my_pizza = ['Pepperoni', '4Cheese', 'Margarita']

friend_pizza = my_pizza[:]

my_pizza.append('Spicy')
friend_pizza.append('Carbonara')

for i in my_pizza:
	print(i)

print()

for i in friend_pizza:
	print(i)