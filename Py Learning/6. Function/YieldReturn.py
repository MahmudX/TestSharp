def inclusiveFor(*args):
    argsNum = len(args)
    start = 0
    step = 1
    stop = 0

    if argsNum == 0:
        raise TypeError(f'Expected at least one argument. Found {argsNum}')
    elif argsNum == 1:
        stop = args[0]
    elif args[0] > args[1]:
        raise TypeError(f'Starting position should be less than or equal to the range.')
    elif argsNum == 2:
        (start, stop) = args
    elif argsNum == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'Expected up to three arguments. Found {argsNum}')
    i = start
    while i <= stop:
        yield i
        i += step

for i in inclusiveFor(22, 22, 3):
    print(i, end=' ', flush=True)
