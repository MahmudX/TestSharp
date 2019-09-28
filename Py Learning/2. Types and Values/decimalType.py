from decimal import *
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print(type(x))
print(x)
