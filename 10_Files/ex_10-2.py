# 10.2. Изучение C. Метод replace() может использоваться для замены
# любого слова в строке другим словом. В следующем примере слово 'dog'
# заменяется словом 'cat':>>> message = "I really like dogs.">>>
# message.replace('dog', 'cat')'I really like cats.' Прочитайте каждую строку
# из только что созданного файла learning_python.txt и замените слово Python
# названием другого языка — например, C. Выведите каждую измененную строку на
# экран.

from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
content = content.replace('Python','Java')
print(content)