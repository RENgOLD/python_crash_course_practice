guests = ['Name1', 'Name2', 'Name3', 'Name4']
print(f'Invite you, {guests[0]}')
print(f'Invite you, {guests[1]}')
print(f'Invite you, {guests[2]}')
print(f'Invite you, {guests[3]}')

print()

cantCome = 'Name2'
guests.remove(cantCome)
guests.append('Name5')
print(f'{cantCome} cant come :(\nNew list of guests:')
print(f'Invite you, {guests[0]}')
print(f'Invite you, {guests[1]}')
print(f'Invite you, {guests[2]}')
print(f'Invite you, {guests[3]}')

print('New guests invited!\nNew list of guests:')
guests.insert(0, 'NameStart')
guests.insert(2, 'NameMiddle')
guests.append('NameEnd')
print(f'Invite you, {guests[0]}')
print(f'Invite you, {guests[1]}')
print(f'Invite you, {guests[2]}')
print(f'Invite you, {guests[3]}')
print(f'Invite you, {guests[4]}')
print(f'Invite you, {guests[5]}')
print(f'Invite you, {guests[6]}')
