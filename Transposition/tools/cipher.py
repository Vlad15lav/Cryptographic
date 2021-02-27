import numpy as np
import math

from itertools import chain, zip_longest
from math import ceil
from random import shuffle
from base.cipherbase import Cipher

"""
Шифр Простой одинарной перестановки
"""
class SingleTransposition(Cipher):
    def __init__(self, key: str = None, alphabet: str = None):
        super().__init__(key, alphabet)
        self.key = key
        self.alphabet = alphabet

    def encode(self, text: str) -> [str, list]:
        self.key = [i for i in range(len(text))]
        shuffle(self.key)
        text_arr = np.array(list(text))
        return ''.join(text_arr[self.key].tolist()), self.key

    def decode(self, text: str) -> str:
        self.key = list(map(int, self.key.split(' ')))
        text_arr = np.array(list(text))
        return ''.join(text_arr[np.argsort(self.key)].tolist())

    def get_table(self) -> np.array:
        return np.array([[i for i in range(len(self.key))], self.key])

"""
Шифр блочной перестановки
"""
class BlockTransposition(Cipher):
    def __init__(self, key: str, alphabet: str = None):
        super().__init__(key, alphabet)
        self.key = key
        self.key_seq = None
        self.alphabet = alphabet

    def encode(self, text: str) -> [str, list]:
        self.key = int(self.key)
        for _ in range(self.key - len(text) % self.key):
            text += text[-1]
        text_split = np.array([text[i:i + self.key] for i in range(0, len(text), self.key)])
        self.key_seq = [i for i in range(len(text_split))]
        shuffle(self.key_seq)
        return ''.join(text_split[self.key_seq].tolist()), self.key_seq

    def decode(self, text: str) -> str:
        self.key_seq = list(map(int, self.key.split(' ')))
        self.key = len(text) // len(self.key_seq)

        text_split = np.array([text[i:i + self.key] for i in range(0, len(text), self.key)])
        return ''.join(text_split[np.argsort(self.key_seq)].tolist())

    def get_table(self) -> np.array:
        return np.array([[i for i in range(len(self.key_seq))], self.key_seq])

"""
Шифр Табличной маршрутной перестановки
"""
class TableTransposition(Cipher):
    def __init__(self, key: int, alphabet: str = None):
        super().__init__(key)
        self.key = int(key)
        self.table = None

    def get_table(self) -> np.array:
        return self.table

    def encode(self, text: str) -> [str, int]:
        self.table = np.array(list(text + '_' * (self.key - len(text) % self.key)))\
          .reshape(self.key, -1)
        return ''.join(self.table.T.reshape(-1)), self.key

    def decode(self, text: str) -> str:
        result = np.array(list(text)).reshape(-1, self.key).T.reshape(-1)
        return ''.join(result).rstrip('_')

"""
Шифр вертикальной перестановки
"""
class VerticalTransposition(Cipher):
    def __init__(self, key: str, alphabet: str = None):
        super().__init__(key)
        self.key = key
        self.table = None

    def get_table(self) -> np.array:
        return self.table

    def encode(self, text: str) -> [str, np.array]:
        columns = len(self.key)
        key_list = [[s, i, i] for i, s in enumerate(list(self.key))]
        key_list = sorted(key_list, key=lambda x: x[0])
        for i, v in enumerate(key_list):
            v[-1] = i
        idx = np.int_(np.array(key_list)[:, 1])
        table_head = np.array(sorted(key_list, key=lambda x: x[1]))[:, [0, 2]].T
        table_main = np.array(list(text + '_' * (columns - len(text) % columns)))\
            .reshape(-1, columns)
        self.table = np.concatenate((table_head, table_main))
        return ''.join(table_main[:, idx].T.reshape(-1)), self.key

    def decode(self, text: str) -> str:
        key_list = [[s, i, i] for i, s in enumerate(list(self.key))]
        key_list = sorted(key_list, key=lambda x: x[0])
        for i, v in enumerate(key_list):
            v[-1] = i
        idx = np.int_(np.array(sorted(key_list, key=lambda x: x[1]))[:, -1])
        result = np.array(list(text)).reshape(len(self.key), -1).T[:, idx].reshape(-1)
        return ''.join(result).rstrip('_')

"""
Шифр поворотной решетки
"""
class RotaryTransposition(Cipher):
    def __init__(self, key: str, alphabet: str = None):
        super().__init__(key)
        """
        Инициализация
        :param key: длина входной строки
        :param alphabet: алфавит

        stencil - трафарет
        size - размер трафарета (должен быть четный)
        """
        self.key = key
        self.table = None
        self.stencil_size = ceil(int(key) ** 0.5)
        if self.stencil_size % 2:
            self.stencil_size += 1

        # Задаем трафарет и его повороты
        self.stencil = self.set_stencil()
        self.stencil_first_flip = np.flip(self.stencil, 1)
        self.stencil_second_flip = np.flip(self.stencil_first_flip, 0)
        self.stencil_fird_flip = np.flip(self.stencil_second_flip, 1)

        # Находим последовательность индексов для записи строки в матрицу
        self.index_order = np.concatenate([np.where(self.stencil == 1),
                                           np.where(self.stencil_first_flip == 1),
                                           np.where(self.stencil_second_flip == 1),
                                           np.where(self.stencil_fird_flip == 1),
                                          ], axis=1)

    def set_stencil(self) -> np.array:
        stencil = np.full((self.stencil_size, self.stencil_size), 0)

        # Создаем трафарет по такому же принципу как в примере
        for i in range(0, self.stencil_size, 2):
            for j in range(i // 2, self.stencil_size, 2):
                stencil[i, j] = 1

        return stencil

    def get_table(self) -> np.array:
        return self.table

    def encode(self, message: str) -> [str, str]:
        self.table = np.full((self.stencil_size, self.stencil_size), '*')

        # Записываем символы сообщения в матрицу в порядке их появления по трафарету
        for i, j, ch in zip_longest(*self.index_order, message, fillvalue='*'):
            self.table[i, j] = ch

        # Выписываем символы из матрицы в строку
        enc = ''
        for i in range(self.stencil_size):
            enc += ''.join(self.table[:, i])
        return enc, self.key

    def decode(self, text: str) -> str:
        self.table = np.full((self.stencil_size, self.stencil_size), '*')

        # Заполняем таблицу, используя зашифрованное сообщение
        for i in range(0, len(text), self.stencil_size):
            self.table[:, i // 4] = list((text[i:i+4]))

        # Дешифруем на основе имеющихся трафаретов
        dec = ''
        for i, j in zip(*self.index_order):
            dec += self.table[i, j]

        # Удаляем вспомогательные символы и возвращаем результат
        return dec.replace('*', '')


"""
Шифр Магический квадрат
"""
class MagicSquare(Cipher):
    def __init__(self, key: str, alphabet: str = None):
        super().__init__(key)
        self.key = key
        self.table = None
        self.magic_square = np.array([[16, 3, 2, 13],  # 0
                                      [5, 10, 11, 8],  # 1
                                      [9, 6, 7, 12],  # 2
                                      [4, 15, 14, 1]])  # 3
        self.indexes = ((3, 3), (0, 2), (0, 1), (3, 0), (1, 0), (2, 1), (2, 2),
                        (1, 3), (2, 0), (1, 1), (1, 2), (2, 3), (0, 3), (3, 2), (3, 1),
                        (0, 0))

    def get_table(self) -> np.array:
        return self.table

    def encode(self, text) -> [str, str]:
        table = np.full((4, 4), '*')

        for (i, j), ch  in zip_longest(self.indexes, text, fillvalue='*'):
            table[i, j] = ch
        self.table = table

        return ''.join(table.reshape(-1)), self.key


    def decode(self, text):
        table = np.array(list(text)).reshape(4, 4)

        res = ''
        for (i, j) in self.indexes:
            res += table[i, j]
        return res.replace('*', '')

"""
Шифр Двойной перстановки
"""
class DoubleTransposition(Cipher):
    def __init__(self, key: str, alphabet: str):
        super().__init__(key, alphabet)
        self.column_key, self.row_key = key.split(' ')
        self.alphabet = alphabet
        self.table = self.create_table()

    def create_table(self) -> np.array:
        key_table = np.copy(self.alphabet)
        idx_col, idx_row = list(map(int, list(self.column_key))), list(map(int, list(self.row_key)))
        key_table[:, range(len(idx_col))] = key_table[:, idx_col]
        key_table[range(len(idx_row)), :] = key_table[idx_row, :]
        return key_table

    def get_table(self) -> np.array:
        return self.table

    def encode(self, text: str) -> [str, str]:
        return ''.join([self.table[self.alphabet == s].item() for s in text]), f'{self.column_key} {self.row_key}'

    def decode(self, text: str) -> str:
        return ''.join([self.alphabet[self.table == s].item() for s in text])