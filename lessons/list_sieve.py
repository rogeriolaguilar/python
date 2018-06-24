"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        # Remove appropriate multiples of divisor from answer
        i = 0
        while i < len(answer) - 1:
            if answer[i] != divisor and answer[i] % divisor == 0:
                answer.pop(i)
                i -= 1
            i += 1
        
    return answer

print(compute_primes(200))
print(len(compute_primes(200)))
print(len(compute_primes(2000)))




#### Correct response
"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        for stride in range(2 * divisor, bound, divisor):
            if stride in answer:
                answer.remove(stride)
    return answer

print(len(compute_primes(200)))
print(len(compute_primes(2000)))
