# 8.9. Сообщения. Создайте список с серией коротких сообщений. Передайте
# список функции show_messages(), которая выводит текст каждого сообщения в
# списке.
# 8.10. Отправка сообщений. Начните с копии вашей программы из
# упражнения 8.9. Напишите функцию send_messages(), которая выводит каждое
# сообщение и перемещает его в новый список sent_messages. После вызова
# функции выведите оба списка и убедитесь в том, что перемещение прошло
# успешно.
# 8.11. Архивированные сообщения. Начните с программы из упражнения
# 8.10. Вызовите функцию send_messages(), чтобы создать копию списка
# сообщений. После вызова функции выведите оба списка и убедитесь в том,
# что в исходном списке остались все сообщения.

unsent_messages = ['message1','message2','message3','message4','message5',]
sent_messages = []

def show_messages(list_of_messages):
    for message in list_of_messages:
        print(message)

def send_messages(list_of_messages):
    while list_of_messages:
        sent_messages.append(list_of_messages.pop())

show_messages(unsent_messages)
print(unsent_messages)
print(sent_messages)

send_messages(unsent_messages[:])
print(unsent_messages)
print(sent_messages)
