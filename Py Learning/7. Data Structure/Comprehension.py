from math import pi


def printList(o):
    print('START> ', end='', flush=True)
    for x in o:
        print(x, end=' ', flush=True)
    print('<END')


seq = range(11)
printList(seq)
seq2 = [x*2 for x in seq]
printList(seq2)
seq3 = [x for x in seq2 if x % 3 != 0]
printList(seq3)
seq4 = [(x, x**2) for x in seq3]
printList(seq4)

seq5 = [round(pi, i) for i in seq]
printList(seq5)

dict1 = {x: x ** 2 for x in seq}
print(dict1)

set1 = {x for x in 'mahmudulhasan' if x not in 'asha'}
printList(sorted(set1))
