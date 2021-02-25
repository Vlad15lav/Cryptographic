from tools.prime_test import prime_test

# Find GCD
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Calculation M value
def find_m(b: int) -> int:
    m = 1
    for p in range(2, b):
        if prime_test(p):
            m *= pow(p, int(math.log(b, p)))
    return m
