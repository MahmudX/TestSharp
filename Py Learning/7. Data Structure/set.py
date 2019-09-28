def printSet(o):
    print('{', end='', flush=True)
    for x in o:
        print(x, end=', ', flush=True)
    print('}')

a = set('Hello World')
b = set('Mahmudul Hasan')

printSet(sorted(b))
printSet(sorted(a))

printSet(sorted(b ^ a))
printSet(sorted(b - a))
printSet(sorted(b & a))
printSet(sorted(b | a))