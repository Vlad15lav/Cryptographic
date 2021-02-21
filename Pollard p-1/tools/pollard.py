import numpy as np
import copy

from tools.utils import find_m
from tools.prime_test import eratosthenes

"""
Algorithm Pollard p-1
"""
def pollard(n: int, B: int, a: int, stage: bool = True, B_next: int = 100) -> int:
    M = find_m(B)
    b = pow(a, M, n)
    gcd = np.gcd(n, b - 1)
    if gcd == 1:
        return second_pollard(n, b, B, B_next) if stage else -1
    else:
        return gcd

"""
The second stage Pollard p-1
"""
def second_pollard(n: int, b: int, B: int, B_next: int) -> int:
    q_list = eratosthenes(B, B_next)

    c_cur = pow(b, q_list[0], n)
    gcd = np.gcd(n, c_cur - 1)
    if gcd != 1:
        return gcd

    for i in range(len(q_list) - 1):
        c_cur = pow(c_cur * pow(b, q_list[i + 1] - q_list[i]), n)
        gcd = np.gcd(n, c_cur - 1)
        if gcd != 1 and gcd != n:
            return gcd
    return -1