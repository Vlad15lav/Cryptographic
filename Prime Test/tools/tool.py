# Find GCD
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Find symbol Legendre
def legendre(a: int, b: int) -> int:
    symbol = [a, b]
    temp = 1
    while symbol[0] != 1:
        if symbol[0] == 0:
            return 0
        if symbol[0] % 2:
            temp *= pow(-1, (symbol[0] - 1) * (symbol[1] - 1) // 4)
            symbol.reverse()
            symbol[0] %= symbol[1]
        else:
            symbol[0] //= 2
            temp *= pow(-1, (symbol[1] ** 2 - 1) // 8)
    return temp