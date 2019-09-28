# For
names = ['Mahmud', 'Asha', 'Hasan', 'Suraia']
for i in names:
    if i == 'Hasan':
        break
    print(i)
else:
    print('That was all names.')

# While
name = ''
while name != 'Mahmud':
    name = input('Please enter the correct name: ')
else:
    print('Authorized')