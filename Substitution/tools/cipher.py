import numpy as np

from itertools import starmap, cycle
from base.cipherbase import Cipher
from random import randint

"""
Шифр Цезаря
"""
class CaesarCipher(Cipher):
    def __init__(self, key: str, alphabet: str = None):
        super().__init__(key, alphabet)

        key = int(key) % len(alphabet)
        self.alphabet = alphabet
        self.rot_alphabet = alphabet[key:] + alphabet[:key]

        self.trans_enc = str.maketrans(self.alphabet, self.rot_alphabet)
        self.trans_dec = str.maketrans(self.rot_alphabet, self.alphabet)

    def get_table(self) -> np.array:
        return np.vstack((np.array(list(self.alphabet)), np.array(list(self.rot_alphabet))))

    def encode(self, txt: str) -> str:
        return txt.translate(self.trans_enc)

    def decode(self, txt: str) -> str:
        return txt.translate(self.trans_dec)

"""
Шифр Лозунг
"""
class SloganCipher(Cipher):
    def __init__(self, key: str, alphabet: str = None):
        super().__init__(key, alphabet)
        self.alphabet = alphabet
        self.key_plus_alphabet = ''.join(sorted(set(key), key=key.index))\
                                 + ''.join(filter(lambda x: x not in key, alphabet))

        self.trans_enc = str.maketrans(alphabet, self.key_plus_alphabet)
        self.trans_dec = str.maketrans(self.key_plus_alphabet, alphabet)

    def get_table(self) -> np.array:
        return np.vstack((np.array(list(self.alphabet)), np.array(list(self.key_plus_alphabet))))

    def encode(self, txt: str) -> str:
        return txt.translate(self.trans_enc)

    def decode(self, txt: str) -> str:
        return txt.translate(self.trans_dec)

"""
Шифр Трисемуса
"""
class TrisemusCipher(Cipher):
    # key - кортеж из ключевого слова и размеров матрицы
    def __init__(self, key: (str, (int, int)), alphabet: str = None):
        super().__init__(key, alphabet)
        self.alphabet = alphabet
        self.key = key

    def create_table(self) -> [int, dict, list]:
        keyword, (height, width) = self.key

        # построение таблицы
        pos = 0
        table = [['.' for x in range(width)] for y in range(height)] # заполняем точками
        # словарь с позициями символов в таблице
        hchars = {}
        for i in keyword + self.alphabet:
            # повторяющиеся символы будут отброшены
            if hchars.get(i) is None:
                hchars[i] = pos
                table[pos // width][pos % width] = i
                pos += 1
                if pos >= width * height:
                    break
        return pos, hchars, table

    def get_table(self) -> np.array:
        _, _, table = self.create_table()
        return np.array(table)

    def encode(self, txt: str) -> str:
        keyword, (height, width) = self.key

        pos, hchars, table = self.create_table()

        result = ""
        for i in txt:
            pos = hchars.get(i)
            if pos is not None:
                x = pos % width
                y = (pos // width + 1) % height
                result += table[y][x]
            else: # далее нужно выбрать одно из действий с символами, отсутсвующими в таблице:
                result += i # оставить неизменными

        return result

    def decode(self, txt: str) -> str:
        keyword, (height, width) = self.key

        pos, hchars, table = self.create_table()

        result = ""
        for i in txt:
            pos = hchars.get(i)
            if pos is not None:
                x = pos % width
                y = (pos // width - 1 + height) % height
                result += table[y][x]
            else: # далее нужно выбрать одно из действий с символами, отсутсвующими в таблице:
                result += i # оставить неизменными

        return result

"""
Шифр Полибианский квадрат
"""
class PolybianChiper(Cipher):
    def __init__(self, key: dict, alphabet: str = None):
        super().__init__(key, alphabet)
        self.alphabet = alphabet

    def get_table(self) -> np.array:
        return self.alphabet

    def encode(self, txt: str) -> str:
        res = ""
        for ch in range(len(txt)):
            for i in range(self.alphabet.shape[0]):
                for j in range(self.alphabet.shape[1]):
                    if txt[ch] == self.alphabet[i][j]:
                        res += str(i + 1) + str(j + 1)
        return res

    def decode(self, txt: str) -> str:
        res = ""
        for ch in range(0, len(txt) - 1, 2):
            raw = int(txt[ch]) - 1
            col = int(txt[ch + 1]) - 1
            res += str(self.alphabet[raw][col])
        return res

"""
Шифр Системы омофонов
"""
class HomophonicCipher(Cipher):
    def __init__(self, key: str, alphabet: str = None):
        super().__init__(key, alphabet)
        self.list_alpha = (('012', '659'), ('128', '556'), ('325', '026'), ('210', '215'), ('435', '436'),
                           ('037', '700'), ('346', '007'), ('991', '995'), ('889', '885'), ('088', '087'),
                           ('888', '643'), ('891', '890'), ('456', '458'), ('112', '119'), ('230', '234'),
                           ('064', '149'), ('058', '073'), ('265', '323'), ('347', '349'), ('321', '322'),
                           ('121', '122'), ('081', '082'), ('075', '076'), ('071', '072'), ('055', '056'),
                           ('043', '044'), ('041', '042'), ('032', '033'), ('504', '031'), ('502', '503'),
                           ('501', '248'), ('065', '749'), ('106', '098'))

        self.alphabet = {
            'А': ['012', '659'],
            'Б': ['128', '556'],
            'В': ['325', '026'],
            'Г': ['210', '215'],
            'Д': ['435', '436'],
            'Е': ['037', '700'],
            'Ё': ['346', '007'],
            'Ж': ['991', '995'],
            'З': ['889', '885'],
            'И': ['088', '087'],
            'Й': ['888', '643'],
            'К': ['891', '890'],
            'Л': ['456', '458'],
            'М': ['112', '119'],
            'Н': ['230', '234'],
            'О': ['064', '149'],
            'П': ['058', '073'],
            'Р': ['265', '323'],
            'С': ['347', '349'],
            'Т': ['321', '322'],
            'У': ['121', '122'],
            'Ф': ['081', '082'],
            'Х': ['075', '076'],
            'Ц': ['071', '072'],
            'Ч': ['055', '056'],
            'Ш': ['043', '044'],
            'Щ': ['041', '042'],
            'Ъ': ['032', '033'],
            'Ы': ['504', '031'],
            'Ь': ['502', '503'],
            'Э': ['501', '248'],
            'Ю': ['065', '749'],
            'Я': ['106', '098']
            }
        self.table = np.array(())

        for i, ch in enumerate(alphabet):
            self.alphabet[ch] = self.list_alpha[i]

    def get_table(self) -> np.array:
        temp = []
        for key, val in self.alphabet.items():
            temp.append([key, *val])
        return np.array(temp)

    def encode(self, text: str) -> str:
        result = ""
        for i in text:
            if i in self.alphabet:
                length = len(self.alphabet[i])
                result += self.alphabet[i][randint(0, length - 1)]
        return result

    def decode(self, text: str) -> str:
        result = ""
        for i in range(0, len(text), 3):
            ch = text[i:i+3]
            for j in self.alphabet:
                if ch in self.alphabet[j]:
                    result += j
        return result


"""
Шифр Playfair
"""
class PlayfairCipher(Cipher):
    letter = "Я"
    def __init__(self, key: str, alphabet: str = None):
        super().__init__(key, alphabet)
        self.alphabet = alphabet
        self.matrix = self.create_matrix(key)
        self.original_special_numbers = None

    def create_matrix(self, key_word: str) -> np.array:
        """
        Создание матрицы для алфавита
        :param key_word: str
        :return:
        """
        self.N, self.M = 4,8
        matrix = np.zeros((self.N, self.M), dtype=np.str_)
        key_word = key_word.upper()
        alphabet = self.alphabet

        # удаление повторяющихся символов)))
        key = ''
        for i in key_word:
            if i not in key:
                key += i

        # вставка ключевого слова в начало матрицы
        i, j = 0, 0
        for l in key:
            matrix[i][j] = l
            alphabet = alphabet.replace(l, "")
            j += 1
            if j == self.M:
                i += 1
                j = 0
        # Добавляем оставшийся алфавит
        for l in alphabet:
            matrix[i][j] = l
            j += 1
            if j == self.M:
                i += 1
                j = 0

        return matrix

    def get_table(self) -> np.array:
        return self.matrix

    def find_special_symbol(self, text: str) -> list:
        """
        Для нахождения специльного символа в тексте
        :param text:
        :return:
        """
        numbers = []
        for i in range(len(text)):
            if text[i] == self.letter:
                numbers.append(i)
        return numbers

    def encode(self, text: str) -> str:
        text = text.upper().replace(" ", "")
        # Сохраняем первоначальное расположение выбранного символа
        self.original_special_numbers = self.find_special_symbol(text)
        encode_text = ""
        bigrams_matrix = []
        length = len(text) + 1 if len(text) % 2 != 0 else len(text) # Количество биграмм

        # Создаем биграммы
        i, j = 0, 1
        while i <= length - 1:
            # Если дошли до последнее элемента
            if i == length - 1 or j == length - 1:
                # если осталось только одна буква
                if i == len(text) - 1:
                    bigrams_matrix.append("{}{}".format(text[i], self.letter))
                # если осталось только два буква
                elif i == len(text):
                    break
                else:
                    # если оставшие буква не одинаковые
                    if text[i] != text[j]:
                        bigrams_matrix.append(text[i:j + 1])
                    # если оставшие буква одинаковые
                    else:
                        bigrams_matrix.append("{}{}".format(text[i], self.letter))
                        bigrams_matrix.append("{}{}".format(text[j], self.letter))
                break

            # Если буквы не одинаковые
            if text[i] != text[j]:
                bigrams_matrix.append(text[i:j + 1])
                i += 2
                j += 2

            else:
                bigrams_matrix.append("{}{}".format(text[i], self.letter))
                # bigrams_matrix.append(text[i:j+1])
                i += 1
                j += 1

        # Шифруем
        # 1. Разные строки и стоблцы. 2. Одинаковые строки. 3. Одинаковые столбцы
        for i in bigrams_matrix:
            a, b = i
            a_i, a_j = self.find_symbol(a)
            b_i, b_j = self.find_symbol(b)
            # если в одной строке
            if a_i == b_i:
                encode_text += self.matrix[a_i][(a_j + 1) % self.M] + self.matrix[b_i][(b_j + 1) % self.M]
            # если в одной столбце
            elif a_j == b_j:
                encode_text += self.matrix[(a_i + 1) % self.N][a_j] + self.matrix[(b_i + 1) % self.N][b_j]
            else:
                encode_text += self.matrix[a_i][b_j] + self.matrix[b_i][a_j]
        return encode_text


    def find_symbol(self, symbol: str) -> [int, int]:
        """
        :param symbol:
        :param b:
        :return:
        """
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                if symbol == self.matrix[i][j]:
                    return i, j

    def decode(self, text: str) -> str:
        self.original_special_numbers = self.find_special_symbol(text)
        decoded_text = ''
        bigrams_matrix = []
        # Создаем биграммы
        for i in range(0, len(text)-1, 2):
            bigrams_matrix.append('{}{}'.format(text[i], text[i+1]))


        # РАсШифруем
        # 1. Разные строки и стоблцы. 2. Одинаковые строки. 3. Одинаковые столбцы
        for i in bigrams_matrix:
            a, b = i
            a_i, a_j = self.find_symbol(a)
            b_i, b_j = self.find_symbol(b)
            # если в одной строке
            if a_i == b_i:
                decoded_text += self.matrix[a_i][(a_j - 1) % self.M] + self.matrix[b_i][(b_j - 1) % self.M]
            # если в одной столбце
            elif a_j == b_j:
                decoded_text += self.matrix[(a_i - 1) % self.N][a_j] + self.matrix[(b_i - 1) % self.N][b_j]
            # если в разных столбце и строке
            else:
                decoded_text += self.matrix[a_i][b_j] + self.matrix[b_i][a_j]

        # Удаление лишний особых символов
        decoded_text = decoded_text.replace(self.letter, '')
        for i in self.original_special_numbers:
            decoded_text = decoded_text[:i] + self.letter + decoded_text[i:]
        return decoded_text

"""
Шифр Виженера
"""
class VigilanteCipher(Cipher):
    def __init__(self, key: dict, alphabet: str = None):
        super().__init__(key, alphabet)
        self.alphabet = alphabet
        self.alphabet_len = len(alphabet)
        self.key = key

    # Вспомогательная функция для шифрования символа
    def enc(self, c: str, k: str) -> str:
        return self.alphabet[(self.alphabet.index(c) + self.alphabet.index(k) + 1) % self.alphabet_len]

    # Функция шифрования
    def encode(self, text: str) -> str:
        return ''.join(starmap(self.enc, zip(text, cycle(self.key))))

    # Фукнция дешифрования
    def decode(self, text: str) -> str:
        # Вспомогательная функция для дешифрования
        def dec(c, k):
            return self.alphabet[(self.alphabet.index(c) - self.alphabet.index(k) - 1) % self.alphabet_len]
        return ''.join(starmap(dec, zip(text, cycle(self.key))))

    def get_table(self) -> np.array:
        table = np.full((self.alphabet_len + 2, self.alphabet_len + 2), ' ')

        for i, ch in enumerate(self.alphabet):
            table[0][i + 2] = table[i + 2][0] = ch

        for i, ch1 in enumerate(self.alphabet):
            for j, ch2 in enumerate(self.alphabet):
                table[i + 2, j + 2] = self.enc(ch1, ch2)
        return table