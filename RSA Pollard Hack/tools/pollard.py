import math
import random
from tools.tool import find_gcd

def factorization(n: int) -> [int, int, int]:
    x = random.randint(1, n - 2)
    y, i, j = 1, 0, 2

    while find_gcd(n, abs(x - y)) == 1:
        if i == j:
            y, j = x, j * 2

        x = (x ** 2 - 1) % n
        i += 1
    d = find_gcd(n, abs(x - y))
    return i, d, n // d