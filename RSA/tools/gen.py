import random
from tools.tool import find_gcd
from tools.prime_test import miller_rabin

# generate number where size is binary length
def generate_number(size: int) -> int:
    return random.randint(pow(2, size - 1), pow(2, size) - 1)

# generate prime number
def generate_prime(size: int) -> int:
    n = generate_number(size)
    if n == 2: return n
    n += n % 2 == 0 # to odd

    while not miller_rabin(n):
        n += 2
    return n

def generate_public(N: int, euler: int) -> int:
    e = generate_number(N // 3)
    while find_gcd(e, euler) != 1: e += 1
    return e
