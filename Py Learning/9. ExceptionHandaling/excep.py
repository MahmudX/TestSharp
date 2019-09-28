import sys

try:
    print(5/0)
except:
    print(f'Got an error {sys.exc_info()[1]}')
    print('Error Details:')
    print(f'{sys.exc_info()}')
    print(f'{sys.exc_info()[0]}')
    print(f'{sys.exc_info()[1]}')
    print(f'{sys.exc_info()[2]}')

print()
print('Auto catch exception')
try:
    print(5/0)
except Exception as identifier:
    print(identifier)

# Custom Exception


def CustomErrorEx(n):
    if n > 5:
        raise TypeError('N shouldnt be more than 5')
    else:
        print(n)
try:
    print('Enter a number: ')
    CustomErrorEx(int(input()))
except Exception as identifier:
    print(identifier)