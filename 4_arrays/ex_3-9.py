guests = ['Name1', 'Name2', 'Name3', 'Name4']

print(f'\nNew guests invited!\nNew list of guests:')
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
print(f'{len(guests)} guests')