guests = ['Name1', 'Name2', 'Name3', 'Name4']
print(f'Invite you, {guests[0]}')
print(f'Invite you, {guests[1]}')
print(f'Invite you, {guests[2]}')
print(f'Invite you, {guests[3]}')

cantCome = 'Name2'
guests.remove(cantCome)
guests.append('Name5')
print(f'\n{cantCome} cant come :(\nNew list of guests:')
print(f'Invite you, {guests[0]}')
print(f'Invite you, {guests[1]}')
print(f'Invite you, {guests[2]}')
print(f'Invite you, {guests[3]}')

print('\nNew guests invited!\nNew list of guests:')
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

print('\nSadly, we can invite only two guests :/')
print(f'Sorry, cant invite you, {guests.pop()}')
print(f'Sorry, cant invite you, {guests.pop()}')
print(f'Sorry, cant invite you, {guests.pop()}')
print(f'Sorry, cant invite you, {guests.pop()}')
print(f'Sorry, cant invite you, {guests.pop()}')
print('\nNew list of guests:')
print(f'Invite you, {guests[0]}')
print(f'Invite you, {guests[1]}')
del guests[0]
del guests[0]
print(f'Check empty list: {guests}')