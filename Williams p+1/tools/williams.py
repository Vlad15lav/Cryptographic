import numpy as np
import random
import math

from functools import reduce
from tools.utils import luke_sequence
from tools.sieve import eratosthenes

"""
Algorithm Williams's p+1
"""
def williams(n: int, B: int, P: int = 1, Q: int = -1) -> int:
    b = random.randint(0, n)
    d = np.gcd(b ** 2 - 4, n)
    if 1 < d < n:
        return d

    p = eratosthenes(2, B)
    q = [pow(p_i, int(math.log(B, p_i))) for p_i in p]
    R = reduce(lambda x, y: x * y, q)

    u_list = [0, 1]
    for _ in range(R - 1):
        u_list = luke_sequence(u_list, P, Q)

    d = np.gcd(u_list[-1], n)
    if 1 < d < n:
        return d
    else:
        return -1