import random

# The sieve of Eratosthenes - prime numbers in [a, b]
def eratosthenes(a: int, b: int) -> list:
    temp = [i for i in range(2, b + 1)]
    i = 0
    while i < len(temp):
        cur_div = temp[i]
        temp = list(filter(lambda x: x % cur_div != 0 or x == cur_div, temp))
        i += 1
    return list(filter(lambda x: x >= a, temp))