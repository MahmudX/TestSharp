def isPrime(n):
    if n <= 1:
        return False
    if n == 4:
        return False
    for x in range(2, round(n/2)):
        if n % x == 0:
            return False
    else:
        return True


def listPrime(n):
    j = 0
    for i in range(n):
        if isPrime(i):
            print(i, end=' ', flush=True)
            j += 1
    print()
    print(j)


print(isPrime(4))

listPrime(1000)
