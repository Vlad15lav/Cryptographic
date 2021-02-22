import numpy as np

class FastME:
    def __init__(self):
        self.table = None

    def fast_me(self, a: int, b: int, n: int) -> int:
        bin_b = list(bin(b).split('b')[-1])
        a_list = [a]
        for i in range(1, len(bin_b)):
            cur_a = a_list[i - 1]
            a_list.append((cur_a * cur_a * a) % n if int(bin_b[i]) \
                              else (cur_a * cur_a) % n)

        self.table = np.vstack((np.array(bin_b), np.array(a_list)))
        return a_list[-1]

    def get_table(self) -> np.array:
        return self.table