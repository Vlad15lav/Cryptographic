import time

from tkinter import *
from tools.pollard import pollard
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
        self.parent.title('Pollard P-1')
        self.parent['bg'] = '#fafafa'

        self.frame = Frame(self.parent, bg='#fafafa')

        # Field N
        self.label_n = Label(self.frame, text='Entry N:', bg='#fafafa', font=20)
        self.entry_n = Entry(self.frame, width=40, justify='center')

        # Field B
        self.label_b = Label(self.frame, text='Entry B:', bg='#fafafa', font=20)
        self.entry_b = Entry(self.frame, width=40, justify='center')

        # Field A
        self.label_a = Label(self.frame, text='Entry A:', bg='#fafafa', font=20)
        self.entry_a = Entry(self.frame, width=40, justify='center')

        # Field B next
        self.label_b_next = Label(self.frame, text='Entry Bn:', bg='#fafafa', font=20)
        self.entry_b_next = Entry(self.frame, width=40, justify='center')

        # RadioButton for Pollard second stage
        self.label_method = Label(self.frame, text='Method', bg='#fafafa', font=20)
        self.radio_status = IntVar()
        self.radio_one = Radiobutton(self.frame, text='One stage', bg='#fafafa', value=False, variable=self.radio_status)
        self.radio_two = Radiobutton(self.frame, text='Two stages', bg='#fafafa', value=True, variable=self.radio_status)

        # Field button
        self.btn_factorize = Button(self.frame, text='Factorization', bg='gray', command=self.button_click)

        # Field Result
        self.result = Text(self.frame)

    def showUI(self):
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Field N
        self.label_n.place(x=20, y=20)
        self.entry_n.place(x=120, y=24)
        self.entry_n.insert(0, 1728239)

        # Field B
        self.label_b.place(x=20, y=60)
        self.entry_b.place(x=120, y=64)
        self.entry_b.insert(0, 50)

        # Field A
        self.label_a.place(x=20, y=100)
        self.entry_a.place(x=120, y=104)
        self.entry_a.insert(0, 2)

        # Field B Next
        self.label_b_next.place(x=20, y=140)
        self.entry_b_next.place(x=120, y=144)
        self.entry_b_next.insert(0, 50 * 50)

        # RadioButton for select Pollard stages
        self.label_method.place(x=410, y=90)
        self.radio_one.place(x=390, y=110)
        self.radio_two.place(x=390, y=130)

        # Field button
        self.btn_factorize.place(x=380, y=25, width=110, height=60)

        # Field Result
        self.result.place(x=20, y=180, width=460, height=150)

    def button_click(self):
        try:
            n = int(self.entry_n.get())
            B = int(self.entry_b.get())
            a = int(self.entry_a.get())
            b_next = int(self.entry_b_next.get())
        except ValueError:
            mb.showerror("Error", 'Please enter an integers!')
            return

        if b_next < B:
            mb.showerror("Error", "Bn should more B!")
            return


        start_time = time.time()
        res = pollard(n, B, a, self.radio_status.get(), b_next)
        stop_time = time.time()
        self.result.delete(1.0, END)

        if res == n:
            txt = 'Failed attempt.\nTry other parameter A.'
        elif res != -1:
            txt = f"Factorization:\n{n} = {res} * {n // res}\n" \
                  f"\nTime working - {stop_time - start_time} seconds"
        else:
            if self.radio_status.get():
                txt = 'Failed attempt.\nTry increasing parameter B.'
            else:
                txt ='Failed attempt.\nTry increasing parameter B, Bn and select two stage method'

        self.result.insert(1.0, txt)

    # Centring window
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.window_w) / 2
        y = (sh - self.window_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.window_w, self.window_h, x, y))