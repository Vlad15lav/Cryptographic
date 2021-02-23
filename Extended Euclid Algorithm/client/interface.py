import time

from tkinter import *
from tkinter import messagebox as mb
from client.tableform import TableForm
from tools.euclid import Euclid

# Tkinter interface
class MainForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frame = Frame(self, bg='#fafafa')
        self.parent = parent
        self.parent.resizable(width=False, height=False)

        self.tool = Euclid()

        self.window_w = 500
        self.window_h = 250

        self.centerWindow()
        self.initUI()
        self.showUI()

    def initUI(self):
        self.parent.title('Extended Euclid Algorithm')
        self.parent['bg'] = '#fafafa'

        self.frame = Frame(self.parent, bg='#fafafa')

        # Field A
        self.label_a = Label(self.frame, text='Entry A:', bg='#fafafa', font=20)
        self.entry_a = Entry(self.frame, width=40, justify='center')

        # Field B
        self.label_b = Label(self.frame, text='Entry B:', bg='#fafafa', font=20)
        self.entry_b = Entry(self.frame, width=40, justify='center')

        # Field button
        self.btn_pow = Button(self.frame, text='Build', bg='gray', command=self.button_build)
        self.btn_table = Button(self.frame, text='Show Table', bg='gray', command=self.button_table)

        # Field Result
        self.label_result = Label(self.frame, text="Result AX + BY = 1", bg='#fafafa', font=20)
        self.label_x = Label(self.frame, text='X', bg='#fafafa', font=20)
        self.result_x = Text(self.frame)
        self.label_y = Label(self.frame, text='Y', bg='#fafafa', font=20)
        self.result_y = Text(self.frame)
        self.label_gcd = Label(self.frame, text='GCD(A, B)', bg='#fafafa', font=20)
        self.result_gcd = Text(self.frame)

    def showUI(self):
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Field A
        self.label_a.place(x=20, y=20)
        self.entry_a.place(x=120, y=24)

        # Field B
        self.label_b.place(x=20, y=60)
        self.entry_b.place(x=120, y=64)

        # Field button
        self.btn_pow.place(x=380, y=24, width=110, height=25)
        self.btn_table.place(x=380, y=58, width=110, height=25)

        # Field Result
        self.label_result.place(x=180, y=100)
        self.label_x.place(x=50, y=130)
        self.result_x.place(x=120, y=130, width=250, height=25)
        self.label_y.place(x=50, y=165)
        self.result_y.place(x=120, y=165, width=250, height=25)
        self.label_gcd.place(x=20, y=200)
        self.result_gcd.place(x=120, y=200, width=250, height=25)

    def button_build(self):
        try:
            A = int(self.entry_a.get())
            B = int(self.entry_b.get())
        except ValueError:
            mb.showerror("Error", 'Please enter an integers!')
            return

        gcd, x, y = self.tool.alg_euclid(A, B)

        self.result_x.delete(1.0, END)
        self.result_x.insert(1.0, x)
        self.result_y.delete(1.0, END)
        self.result_y.insert(1.0, y)
        self.result_gcd.delete(1.0, END)
        self.result_gcd.insert(1.0, gcd)


    def button_table(self):
        table = self.tool.get_table()
        if table is None:
            mb.showerror("Error", 'Use build!')
        else:
            newWindow = Toplevel(self.parent)
            TableForm(newWindow, table)

    # Centring window
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.window_w) / 2
        y = (sh - self.window_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.window_w, self.window_h, x, y))