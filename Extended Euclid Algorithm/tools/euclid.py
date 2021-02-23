import numpy as np

class Euclid:
    def __init__(self):
        self.table = None

    def alg_euclid(self, A: int, B: int) -> [int, int]:
        # First four columns
        A_list, B_list, mod_list, div_list = [], [], [], []
        while A % B != 0:
            A_list.append(A)
            B_list.append(B)
            mod_list.append(A % B)
            div_list.append(A // B)

            A, B = B, mod_list[-1]
        A_list.append(A)
        B_list.append(B)
        mod_list.append(A % B)
        div_list.append(A // B)
        # Last two columns
        x, y = [0], [1]
        rows = len(div_list)
        for i in range(1, rows):
            x.append(y[i - 1])
            y.append(x[i - 1] - y[i - 1] * div_list[rows - i - 1])
        # Create table
        tab_head = np.array(['A', 'B', 'Mod', 'Div', 'X', 'Y'])
        tab_values = np.concatenate(([np.array(A_list)], [np.array(B_list)],\
                                    [np.array(mod_list)], [np.array(div_list)],\
                                    [np.array(x[::-1])], [np.array(y[::-1])]),\
                                    axis=0).T
        self.table = np.vstack((tab_head, tab_values))
        return B_list[-1], x[-1], y[-1]

    def get_table(self) -> np.array:
        return self.table