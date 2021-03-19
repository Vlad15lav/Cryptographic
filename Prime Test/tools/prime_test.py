import math
import random
from typing import Callable
from tools.tool import find_gcd, legendre

# Test Miller Rabin
def miller_rabin(n: int) -> bool:
    if n == 2: return True
    if n % 2 == 0: return False

    d = n - 1
    # find d: n - 1 = 2^t * d
    while not d % 2: d //= 2

    for _ in range(int(math.log2(n))):
        a = random.randint(2, n - 1)
        # first step
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        # second step
        while d != n - 1:
            x, d = pow(x, 2, n), d * 2
            if x == n - 1:
                break
        else:
            return False
    return True

# Test Solovay Strassen
def solovay_strassen(n: int) -> bool:
    if n == 2: return True
    if n % 2 == 0: return False

    for _ in range(int(math.log2(n))):
        a = random.randint(2, n - 1)
        d = find_gcd(a, n)

        if d > 1: return False
        if pow(a, (n - 1) // 2, n) != legendre(a, n) % n:
            return False
    return True
