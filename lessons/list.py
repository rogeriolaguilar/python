
print([4,2,23,4])

print(range(5))
print(list( range(5))   )
print(list( range(5, 10)    ))
print(list( range(4, 10, 2)    ))

text = 'This is a text.'
list = text.split()
print(list)
print(list.index('is'))
print(" ".join(list))

# Iteraction list

def print_itens(list):
    for item in list:
        print(item)
print_itens(['A', 'b', 'c'])


def strange_sum(list):
    sum = 0
    for item in list:
        if item % 3 != 0:
            sum += item
    return sum

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))


# Append vs Extend
list = [1,2,3]
list.append(4)
print(list)
list.extend([4,5,6])
print(list)
list.append([4,5,6])
print(list)

list.reverse()



def fib_fun(interactions):
    fib = [0,1]
    i = 0
    while i < interactions:
        fib.append(fib[-2]+ fib[-1])
        i += 1
    return fib

print(fib_fun(10))
print(fib_fun(20))


