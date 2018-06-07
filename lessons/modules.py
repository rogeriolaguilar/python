import math
print(math.pi)


import math as m
print(m.pi)

print(dir(math))
print()
print(math.__name__)
print(m.__name__)


import collatz_conjecture # module from this projects
print(collatz_conjecture.f(3))
print(collatz_conjecture.result)


import datetime
date = datetime.date(2000,12,30)
today = datetime.date.today()
print(date)
print(today)
print("Subtracting dates:", today - date)
print("Subtracting dates and getting days:", (today - date).days)