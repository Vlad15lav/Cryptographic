import random

from tools.gen import generate_prime, generate_public
from tools.tool import fast_me, alg_euclid

class RSA:
    def __init__(self, bin_size: int = None):
        self.__length_alp = 2048 # Max code symbol

        if bin_size is not None:
            self.__bin_size = bin_size
            self.__p, self.__q = generate_prime(bin_size), generate_prime(bin_size)
            self.__n = self.__p * self.__q
            self.__euler = (self.__p - 1) * (self.__q - 1)
            self.__e = generate_public(self.__n, self.__euler)
            _, _, self.__d = alg_euclid(self.__euler, self.__e)
            self.__d %= self.__euler

    def params(self) -> [int, int, int, int, int, int]:
        return self.__p, self.__q, self.__n, self.__euler, self.__e, self.__d

    def set_params(self, e: int = None, d: int = None, n: int = None):
        self.__e, self.__d, self.__n = e, d, n

    def public_key(self) -> [int, int]:
        return [self.__e, self.__n]

    def private_key(self) -> [int, int]:
        return [self.__d, self.__n]

    def encode(self, message: str) -> str:
        return ''.join([str(fast_me(ord(s), self.__e, self.__n)) + ' ' for s in list(message)]).rstrip(' ')

    def decode(self, message: str) -> str:
        return ''.join([str(chr(fast_me(int(c), self.__d, self.__n) % self.__length_alp)) for c in message.split(' ')]).rstrip(' ')
