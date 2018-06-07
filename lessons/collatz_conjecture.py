# https://en.wikipedia.org/wiki/Collatz_conjecture#Statement_of_the_problem

def collatz(n):
    if (n % 2 == 0):
        return n // 2
    else:
        return 3 * n + 1

def f(n):
return collatz(n)

result = f(f(f(f(f(f(f(674))))))) # 190
result2 = f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))
# print(result)
# print(result2)
