import numpy as np
from tkinter import *

class TableForm(Frame):
    def __init__(self, parent, table: np.array):
        Frame.__init__(self, parent)
        self.parent = parent
        self.table = table
        self.frame = Frame(self.parent)
        self.parent.resizable(width=False, height=False)
        self.initUI()
        self.showUI()

    def initUI(self):
        self.parent.title('Table')

    def showUI(self):
        self.show_table()
        self.frame.pack()

    def show_table(self):
        rows, columns = self.table.shape
        for i in range(rows):
            for j in range(columns):
                self.entry_table = Entry(self.frame, width=5)
                self.entry_table.grid(row=i, column=j)
                self.entry_table.insert(END, self.table[i][j])
