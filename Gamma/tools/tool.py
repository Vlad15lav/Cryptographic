import numpy as np
import random

def xor4str(first_code: str, second_code: str) -> str:
    return ''.join([str(int(a) ^ int(b)) for a, b in zip(first_code, second_code)])

def get_gamma(length: int) -> str:
    var = ['0', '1']
    np.random.shuffle(var)
    rand_seq = ''.rjust(length // 2, var[0]).rjust(length, var[-1])
    return ''.join(random.sample(rand_seq, length))