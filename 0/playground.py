from pathlib import Path

path = Path("../10_Files/pi_digits.txt")
print(path)
contents = path.read_text()
lines = contents.splitlines()
pi = ''
for line in lines:
    pi = f'{pi}{line}'
print(pi)