# 10.3. Более простой код. В программе file_reader.py в этом разделе
# ис-пользуется временная переменная, lines, демонстрирующая работу
# метода splitlines(). Вы можете опустить временную переменную и выполнить
# цикл непосредственно над списком, который возвращает метод splitlines(),
# сле-дующим образом:for line in contents.splitlines():Удалите временную
# переменную из всех программ в этом разделе, чтобы сделать их код более
# лаконичным.

from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()

for line in content.splitlines():
    print(line)
