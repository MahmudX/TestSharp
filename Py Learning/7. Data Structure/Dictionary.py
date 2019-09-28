def printDict(o):
    for i, j in o.items(): print(f'{i} sounds {j}')


Animals = dict(Tiger='Roar', Lion='Growls', Cat='Meaw')
Animals['Monkey'] = 'Hi Hi'
# printDict(Animals)

# print('Keys Only - ')
# for i in Animals.keys(): print(i)

# print('Values Only - ')
# for i in Animals.values(): print(i)

# print('found' if 'JackAss' in Animals else 'Not Found')

# print(Animals['Lion'])
print(Animals.get('Eliphant'))