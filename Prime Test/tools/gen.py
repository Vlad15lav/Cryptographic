import random
from typing import Callable

# generate number where size is binary length
def generate_number(size: int) -> int:
    return random.randint(pow(2, size - 1), pow(2, size) - 1)

# generate prime number
def generate_prime(size: int, test_function: Callable) -> int:
    n = generate_number(size)
    n += n % 2 == 0 # to odd

    while not test_function(n): n += 2
    return n
