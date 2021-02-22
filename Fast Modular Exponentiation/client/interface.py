import time

from tkinter import *
from tkinter import messagebox as mb
from client.tableform import TableForm
from tools.fast import FastME

# Tkinter interface
class MainForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frame = Frame(self, bg='#fafafa')
        self.parent = parent
        self.parent.resizable(width=False, height=False)

        self.tool = FastME()

        self.window_w = 500
        self.window_h = 250

        self.centerWindow()
        self.initUI()
        self.showUI()

    def initUI(self):
        self.parent.title('Fast Modular Exponentiation')
        self.parent['bg'] = '#fafafa'

        self.frame = Frame(self.parent, bg='#fafafa')

        # Field A
        self.label_a = Label(self.frame, text='Entry A:', bg='#fafafa', font=20)
        self.entry_a = Entry(self.frame, width=40, justify='center')

        # Field B
        self.label_b = Label(self.frame, text='Entry B:', bg='#fafafa', font=20)
        self.entry_b = Entry(self.frame, width=40, justify='center')

        # Field N
        self.label_n = Label(self.frame, text='Entry N:', bg='#fafafa', font=20)
        self.entry_n = Entry(self.frame, width=40, justify='center')

        # Field button
        self.btn_pow = Button(self.frame, text='Pow', bg='gray', command=self.button_pow)
        self.btn_table = Button(self.frame, text='Show Table', bg='gray', command=self.button_table)

        # Field Result
        self.label_result = Label(self.frame, text=u"a^b mod N:", bg='#fafafa', font=20)
        self.result = Text(self.frame)

    def showUI(self):
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Field A
        self.label_a.place(x=20, y=20)
        self.entry_a.place(x=120, y=24)

        # Field B
        self.label_b.place(x=20, y=60)
        self.entry_b.place(x=120, y=64)

        # Field N
        self.label_n.place(x=20, y=100)
        self.entry_n.place(x=120, y=104)

        # Field button
        self.btn_pow.place(x=380, y=25, width=110, height=40)
        self.btn_table.place(x=380, y=70, width=110, height=40)

        # Field Result
        self.label_result.place(x=220, y=125)
        self.result.place(x=20, y=150, width=460, height=80)

    def button_pow(self):
        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            n = int(self.entry_n.get())
        except ValueError:
            mb.showerror("Error", 'Please enter an integers!')
            return

        self.result.delete(1.0, END)
        self.result.insert(1.0, self.tool.fast_me(a, b, n))

    def button_table(self):
        table = self.tool.get_table()
        if table is None:
            mb.showerror("Error", 'Use pow!')
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