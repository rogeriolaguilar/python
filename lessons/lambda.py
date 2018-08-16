l = list(range(10)) 
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


result = list(map(lambda x: x * 2, l))
print("Simple Lambda", result) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


tuples_l_l2 =  list(map(lambda x1, x2: (x1, x2), l, result))
print("Lambda and map with more variables", tuples_l_l2)


mins = list(map(lambda tuple: min(tuple[0], tuple[1]), tuples_l_l2))
print("Using another function in lambda", mins)


odds = list(filter(lambda x1: (x1 % 2 != 0), mins))
print("using filter for odd numbers", odds)


import random
random.shuffle(l)
print("Random list", l)


rand_turples = list(map(lambda x: (x, random.randint(l[0], 99)), l))
print("Random turples", rand_turples)


rand_turples.sort()
print("Sorted tuples", rand_turples)

rand_turples.sort(key = lambda x: x[1])
print("Sorted tuples by second", rand_turples)

rand_turples.sort(key = lambda t : t[0] * t[1])
print("Sorted tuples by the product", rand_turples)
