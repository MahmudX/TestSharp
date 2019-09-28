# List (Mutable)
L = [1, 2, 3, 4, 5]
L[2] = 9
print(L)

x = list(range(10))
for i in x:
    print(f'x is {i}')

# Tuple (Immutable)
T = (1, 2, 3, 4, 5)
print(T)

x = range(10)
for i in x:
    print(f'x is {i}')

# Dictionary (Mutable)
D = {1: "One", 2: 'Two', 3: 'Three'}
D[2] = 'Nine'
for k, v in D.items():
    print(f'Key = {k} and Value = {v}')
