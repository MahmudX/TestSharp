import sys
import os
import random
import datetime

x = sys.version_info
print('{}.{}.{}'.format(*x))
print(sys.platform)
print(os.name)
# print(os.getenv('PATH'))
print(os.getcwd())

random1 = os.urandom(12)
random2 = os.urandom(12).hex()
print(random1)
print(random2)

random3 = random.randint(5, 2000)
print(random3)

L = list(range(25))
print(L)
random.shuffle(L)
print(L)


now = datetime.datetime.now()
print(f'Full DateTime: {now}')
date = now.date()
day = now.day
year = now.year
print(f'Only Date: {date}')
print(f'Only Day: {day}')
print(f'Only Year: {year}')
print(f'Month: {now.month}')
