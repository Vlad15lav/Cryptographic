from tools.pollard import factorization
from tools.tool import fast_me, alg_euclid

# Hacking RSA Function
def hacking_rsa(e: int, n: int, message: str) -> [int, int, int, int, int, str]:
    """

    :param e: part public key
    :param n: part public key
    :param message: hacking cryptogram
    :return: iterations, p, q, euler, d, decode text
    """
    iterations, p, q = factorization(n)
    euler = (p - 1) * (q - 1)
    _, _, d = alg_euclid(euler, e)
    d %= euler
    text = ''.join([str(chr(fast_me(int(c), d, n) % 2048)) for c in message.split(' ')]).rstrip(' ')
    return iterations, p, q, euler, d, text