# Find GCD
def find_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Sequence Luke
def luke_sequence(last_u: int, cur_u: int, count: int, P: int = 1, Q: int = -1) -> int:
    temp_u = 0
    for _ in range(count):
        temp_u = last_u * P + cur_u * Q
        last_u = cur_u
        cur_u = temp_u
    return temp_u
