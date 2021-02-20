import string
import numpy as np

from tools.tool import xor4str
from config.config import rus_alphabet, eng_alphabet

class Gamma:
    def __init__(self, key: str = None, isRus: bool = True):
        self.isRus = isRus
        if isRus:
            self.__alp = np.array(list(rus_alphabet))
        else:
            self.__alp = np.array(list(eng_alphabet))
        self.N = self.__alp.shape[0]
        self.codes = np.array([format(i, '06b') for i in range(self.N)])

        self.key = key
        if self.key is not None:
            self.key_code = np.array([self.codes[self.__alp == s][0] for s in key])

    def bin2char(self, bin_key: str) -> str:
        bin_code = [bin_key[i:i + 6] for i in range(0, len(bin_key), 6)]
        return ''.join([self.__alp[self.codes == c][0] for c in bin_code])

    def char2bin(self, sym_key: str) -> str:
        return ''.join([self.codes[self.__alp == s][0] for s in sym_key])

    def encode(self, txt: str, key_seq: str = None) -> str:
        txt_code = [self.codes[self.__alp == s][0] for s in txt]

        output = None
        if self.key is not None:
            output = [self.__alp[int(xor4str(self.key_code[i % self.key_code.shape[0]], txt_code[i]), 2) % self.N]
                      for i in range(len(txt_code))]
        elif key_seq is not None:
            seq_code = np.array([self.codes[self.__alp == s][0] for s in key_seq])
            output = [self.__alp[int(xor4str(seq_code[i], txt_code[i]), 2) % self.N]
                      for i in range(len(txt_code))]
        return ''.join(output)