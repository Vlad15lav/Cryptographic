import re
import time

from tkinter import *
from tkinter import messagebox as mb
from tools.hacker import hacking_rsa
from config.config import reg_decode

# Tkinter interface
class MainForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frame = Frame(self, bg='#fafafa')
        self.parent = parent
        self.parent.resizable(width=False, height=False)

        self.window_w = 550
        self.window_h = 550

        self.centerWindow()
        self.initUI()
        self.showUI()

    def initUI(self):
        self.parent.title('RSA Hacking')
        self.parent['bg'] = '#fafafa'

        self.frame = Frame(self.parent, bg='#fafafa')

        # Field e
        self.label_e = Label(self.frame, text='Entry e:', bg='#fafafa', font=20)
        self.entry_e = Entry(self.frame, justify='center')

        # Field N
        self.label_n = Label(self.frame, text='Entry N:', bg='#fafafa', font=20)
        self.entry_n = Entry(self.frame, justify='center')

        # Field Cryptogram
        self.label_cryp = Label(self.frame, text='Entry Cryptogram:', bg='#fafafa', font=20)
        self.inp_cryp = Text(self.frame)

        # Field button
        self.btn_hack = Button(self.frame, text='Hack', bg='gray', command=self.__button_hack)

        # Field Result
        self.label_result = Label(self.frame, text="Hacking Result", bg='#fafafa', font=20)

        # Field iterations and time
        self.label_score = Label(self.frame, text="Time hacking", bg='#fafafa', font=20, anchor="center")

        # Field p
        self.label_p = Label(self.frame, text='p', bg='#fafafa', font=20)
        self.result_p = Text(self.frame)

        # Field q
        self.label_q = Label(self.frame, text='q', bg='#fafafa', font=20)
        self.result_q = Text(self.frame)

        # Field Euler
        self.label_euler = Label(self.frame, text='\u03C6(N)', bg='#fafafa', font=20)
        self.result_euler = Text(self.frame)

        # Field d
        self.label_d = Label(self.frame, text='d', bg='#fafafa', font=20)
        self.result_d = Text(self.frame)

        # Field Decode
        self.label_dec = Label(self.frame, text='Decode:', bg='#fafafa', font=20)
        self.result_dec = Text(self.frame)

    def showUI(self):
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Field e
        self.label_e.place(x=10, y=17)
        self.entry_e.place(x=70, y=20, width=260)

        # Field n
        self.label_n.place(x=10, y=57)
        self.entry_n.place(x=70, y=60, width=260)

        # Field Cryptogram
        self.label_cryp.place(x=10, y=90)
        self.inp_cryp.place(x=10, y=120, width=530, height=120)

        # Field button
        self.btn_hack.place(x=400, y=40, width=110, height=25)

        # Field Result
        self.label_result.place(x=220, y=240)

        # Field iterations and time
        self.label_score.place(x=325, y=260, width=200, height=120)

        # Result p
        self.label_p.place(x=15, y=267)
        self.result_p.place(x=45, y=270, width=260, height=20)

        # Result q
        self.label_q.place(x=15, y=297)
        self.result_q.place(x=45, y=300, width=260, height=20)

        # Result Euler
        self.label_euler.place(x=5, y=327)
        self.result_euler.place(x=45, y=330, width=260, height=20)

        # Result d
        self.label_d.place(x=15, y=357)
        self.result_d.place(x=45, y=360, width=260, height=20)

        # Field Decode
        self.label_dec.place(x=10, y=380)
        self.result_dec.place(x=10, y=410, width=530, height=120)

    def __button_hack(self):
        try:
            e = int(self.entry_e.get())
            n = int(self.entry_n.get())
        except ValueError:
            mb.showerror("Error", 'Please enter an integers!')
            return

        if not e > 0 or not n > 0:
            mb.showerror("Error", 'Please enter an positive odd number')
            return

        crypt = self.inp_cryp.get("1.0", "end-1c")
        if crypt == '':
            mb.showerror("Error", "Entry cryptogram!")
            return

        # Check outside the alphabet
        reg_val_txt = re.sub(reg_decode, '', crypt)

        # There are extra characters
        if len(reg_val_txt) > 0:
            mb.showerror("Error",
                         repr(f"Foreign characters are used: {''.join(set(reg_val_txt))}"))
            return

        start_time = time.time()
        iterations, p, q, euler, d, decode_txt = hacking_rsa(e, n, crypt)
        stop_time = time.time()
        step = stop_time - start_time

        self.label_score.config(text='Time hacking\nIterations - {}\nTime - {}s'\
                                .format(iterations, round(step, 2)))

        self.result_p.delete(1.0, END)
        self.result_p.insert(1.0, p)

        self.result_q.delete(1.0, END)
        self.result_q.insert(1.0, q)

        self.result_euler.delete(1.0, END)
        self.result_euler.insert(1.0, euler)

        self.result_d.delete(1.0, END)
        self.result_d.insert(1.0, d)

        self.result_dec.delete(1.0, END)
        self.result_dec.insert(1.0, decode_txt)

    # Centring window
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.window_w) / 2
        y = (sh - self.window_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.window_w, self.window_h, x, y))