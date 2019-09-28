x = 'heLLo world'
print("Swap the case: " + x.swapcase())
print("Set all cast to upper: " + x.upper())
print("Set all cast to lower: " + x.lower())
print("Set all cast to lower aggresivly: " + x.casefold())
print("Set every word\'s first letter to upper: " + x.title())
print("Set the first word\'s first letter to upper in a sentence: " + x.capitalize())

x = x.split()
y = '--'.join(x)
print(y)
