# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

print(repr('Hello 😁'))
print(ascii('Hello 😁'))
print('Hello 😁')
print('Hello \U0001f601')
print(ord('🌷'))
print(chr(127799))

x = (1, 2, 3, 4, 5)
y = (6, 7, 8, 9, 10)
z = zip(x, y)
for a, b in z:
    print(f'{a} - {b}')

a = ('rabbit', 'cat', 'parrot', 'cattle')
for i, j in enumerate(a):
    print(f'index: {i} = {j.capitalize()}')