from tkinter import *
from re import fullmatch
from tkinter import messagebox as mb
import numpy as np

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
        self.parent.title('Таблица шифрозамены')

    def showUI(self):
        self.show_table()
        self.frame.pack()

    def show_table(self):
        rows, columns = self.table.shape
        width = 3 if columns > 5 else 10
        for i in range(rows):
            for j in range(columns):
                self.entry_table = Entry(self.frame, width=width)
                self.entry_table.grid(row=i, column=j)
                self.entry_table.insert(END, self.table[i][j])
