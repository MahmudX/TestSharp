# List Printer
def ListPrinter(itemList):
    i = 0
    while i < 5:
        print(itemList[i])
        i += 1

# Fibonacci
def GetFibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ', flush=True)
        a, b = b, a + b
    print()

GetFibonacci(1000)
words = ['Mahmud', 'Hasan', 'Suraia', 'Sarmin', 'Asha']
ListPrinter(words)
