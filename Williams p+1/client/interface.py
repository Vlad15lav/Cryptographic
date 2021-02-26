import time

from tkinter import *
from tools.williams import williams
from tkinter import messagebox as mb

# Tkinter interface
class MainForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frame = Frame(self, bg='#fafafa')
        self.parent = parent
        self.parent.resizable(width=False, height=False)

        self.window_w = 500
        self.window_h = 350

        self.centerWindow()
        self.initUI()
        self.showUI()

    def initUI(self):
        self.parent.title('Williams P+1')
        self.parent['bg'] = '#fafafa'

        self.frame = Frame(self.parent, bg='#fafafa')

        # Field N
        self.label_n = Label(self.frame, text='Entry N:', bg='#fafafa', font=20)
        self.entry_n = Entry(self.frame, width=40, justify='center')

        # Field B
        self.label_b = Label(self.frame, text='Entry B:', bg='#fafafa', font=20)
        self.entry_b = Entry(self.frame, width=40, justify='center')

        # Field P
        self.label_p = Label(self.frame, text='Entry P:', bg='#fafafa', font=20)
        self.entry_p = Entry(self.frame, width=40, justify='center')

        # Field Q next
        self.label_q = Label(self.frame, text='Entry Q:', bg='#fafafa', font=20)
        self.entry_q = Entry(self.frame, width=40, justify='center')

        # Field button
        self.btn_factorize = Button(self.frame, text='Factorization', bg='gray', command=self.button_click)

        # Field Result
        self.result = Text(self.frame)

    def showUI(self):
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Field N
        self.label_n.place(x=20, y=20)
        self.entry_n.place(x=120, y=24)
        self.entry_n.insert(0, 4056187)

        # Field B
        self.label_b.place(x=20, y=60)
        self.entry_b.place(x=120, y=64)
        self.entry_b.insert(0, 5)

        # Field P
        self.label_p.place(x=20, y=100)
        self.entry_p.place(x=120, y=104)
        self.entry_p.insert(0, 1)

        # Field Q
        self.label_q.place(x=20, y=140)
        self.entry_q.place(x=120, y=144)
        self.entry_q.insert(0, 5)

        # Field button
        self.btn_factorize.place(x=380, y=25, width=110, height=60)

        # Field Result
        self.result.place(x=20, y=180, width=460, height=150)

    def button_click(self):
        try:
            n = int(self.entry_n.get())
            B = int(self.entry_b.get())
            P = int(self.entry_p.get())
            Q = int(self.entry_q.get())
        except ValueError:
            mb.showerror("Error", 'Please enter an integers!')
            return

        if B > 14:
            mb.showerror("Warning", 'Recommendation value B not more 14!')
            return
        
        start_time = time.time()
        res = williams(n, B, P, Q)
        stop_time = time.time()
        self.result.delete(1.0, END)

        if res == n:
            txt = 'Failed attempt.\nTry other parameter A.'
        elif res != -1:
            txt = f"Factorization:\n{n} = {res} * {n // res}\n" \
                  f"\nTime working - {stop_time - start_time} seconds"
        else:
            txt = 'Failed attempt.\nTry increasing parameter B.'

        self.result.insert(1.0, txt)

    # Centring window
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.window_w) / 2
        y = (sh - self.window_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.window_w, self.window_h, x, y))
