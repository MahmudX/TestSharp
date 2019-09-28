import time


def f1(f):
    def f2():
        print('This is before function call.')
        f()
        print('This is after function call')
    return f2


# @f1
def f3():
    print('This is f3')


# f3()
x = f1(f3)
# x()

# Elapsed Time


def ElapsedTime(f):
    def Wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time is {(t2 - t1) * 1000}ms')
    return Wrapper

# @ElapsedTime
def BigSum():
    numList = []
    for i in range(1000):
        numList.append(i)
    print(f"The big sum is: {sum(numList)}")

# ElapsedTime(BigSum)()
# BigSum()