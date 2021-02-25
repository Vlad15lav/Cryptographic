import random
import math

from functools import reduce
from tools.utils import luke_sequence, find_gcd
from tools.sieve import eratosthenes

"""
Algorithm Williams's p+1
"""
def williams(n: int, B: int, P: int = 1, Q: int = -1) -> int:
    b = random.randint(0, n)
    d = find_gcd(b ** 2 - 4, n)
    if 1 != d:
        return d

    p = eratosthenes(2, B)
    q = [pow(p_i, int(math.log(B, p_i))) for p_i in p]
    R = reduce(lambda x, y: x * y, q)

    u = luke_sequence(0, 1, R - 1, P, Q)

    d = find_gcd(u, n)
    if 1 != d:
        return d
    else:
        return -1
