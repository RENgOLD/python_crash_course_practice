# 10.1. Изучение Python. Откройте пустой файл в текстовом редакторе и
# напишите несколько строк текста о возможностях Python. Каждая строка должна
# начинаться с фразы «В Python вы можете...» Сохраните файл под именем
# learning_python.txt в каталоге, использованном для примеров этой главы.
# Напишите программу, которая читает файл и выводит текст два раза: читая
# весь файл и сохраняя строки в списке, проходя по каждой строке.

from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
print(content)
print()

lines = content.splitlines()
for line in lines:
    print(line)