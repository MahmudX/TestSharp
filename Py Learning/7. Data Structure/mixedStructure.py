Tracking = 0
def main():
    
    R = range(11)
    L = ['Mahmud', 5, {'Love': 'Asha'}, 9]
    T = (None, 5, 'Hello')
    S = set("Hi! I'm Bill Gates and I'm the founder and CEO of Microsoft")
    D = dict(One=1, Two=2, Three=3, Four=4)
    Mix = [R, L, T, S, D]
    Display(Mix)

def Display(o):
    global Tracking
    Tracking += 1

    if isinstance(o, list):
        printList(o)
    elif isinstance(o, tuple):
        printTuple(o)
    elif isinstance(o, dict):
        printDict(o)
    elif isinstance(o, set):
        printSet(o)
    elif isinstance(o, range):
        printList(o)
    elif o is None:
        print('Nada', end=' ', flush=True)
    else:
        print(repr(o), end=' ', flush=True)
    Tracking -= 1

    if Tracking <= 1:
        print()


def printList(o):
    print('[', end=' ')
    for x in o:
        Display(x)
    print(']', end=' ', flush=True)


def printSet(o):
    print('{', end=' ')
    for x in sorted(o):
        Display(x)
    print('}', end=' ', flush=True)


def printTuple(o):
    print('(', end='')
    for x in o:
        Display(x)
    print(')',end=' ', flush=True)


def printDict(o):
    print('{', end=' ')
    for x, y in o.items():
        print(x, end=': ')
        Display(y)
    print('}', end=' ', flush= True)

if __name__ == "__main__": main()