import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from cipher.rsa import RSA
from config.config import reg_decode

# Tkinter interface
class MainForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frame = Frame(self, bg='#fafafa')
        self.parent = parent
        self.parent.resizable(width=False, height=False)

        self.cipher = None

        self.min_length = 8
        self.window_w = 500
        self.window_h = 550

        self.centerWindow()
        self.initUI()
        self.showUI()

    def initUI(self):
        self.parent.title('RSA')
        self.parent['bg'] = '#fafafa'

        self.frame = Frame(self.parent, bg='#fafafa')

        # Field binary length
        self.label_length = Label(self.frame, text='Entry Binary Length:', bg='#fafafa', font=20)
        self.entry_length = Entry(self.frame, justify='center')

        # Keys Fields:
        # N
        self.n_label = Label(self.frame, text='N:', bg='#fafafa', font=20)
        self.n_txt = Entry(self.frame, justify='center')
        # p
        self.p_label = Label(self.frame, text='p:', bg='#fafafa', font=20)
        self.p_txt = Entry(self.frame, justify='center')
        # q
        self.q_label = Label(self.frame, text='q:', bg='#fafafa', font=20)
        self.q_txt = Entry(self.frame, justify='center')
        # Euler
        self.euler_label = Label(self.frame, text='\u03C6(N):', bg='#fafafa', font=20)
        self.euler_txt = Entry(self.frame, justify='center')
        # e
        self.e_label = Label(self.frame, text='e:', bg='#fafafa', font=20)
        self.e_txt = Entry(self.frame, justify='center')
        # d
        self.d_label = Label(self.frame, text='d:', bg='#fafafa', font=20)
        self.d_txt = Entry(self.frame, justify='center')

        # Info keys
        self.key_label = Label(self.frame, text='Keys:\nPublic - (e, N)\nPrivate - (d, N)', justify=LEFT, bg='#fafafa', font=20)

        # Input Text
        self.inp_label = Label(self.frame, text='Entry Text:', bg='#fafafa', font=20)
        self.inp_txt = Text(self.frame)

        # Result Text
        self.out_label = Label(self.frame, text='Result Text:', bg='#fafafa', font=20)
        self.out_txt = Text(self.frame)

        # Buttons
        self.btn_gen = Button(self.frame, text='Gen Key', bg='gray', command=self.__btn_generate)
        self.btn_enc = Button(self.frame, text='Encode', bg='gray', command=self.__btn_encode)
        self.btn_dec = Button(self.frame, text='Decode', bg='gray', command=self.__btn_decode)


    def showUI(self):
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Field Bin Length
        self.label_length.place(x=20, y=20)
        self.entry_length.place(x=180, y=24)

        # Field N
        self.n_label.place(x=10, y=77)
        self.n_txt.place(x=30, y=80, width=200, height=20)
        # Field p
        self.p_label.place(x=10, y=117)
        self.p_txt.place(x=30, y=120, width=200, height=20)
        # Field q
        self.q_label.place(x=10, y=157)
        self.q_txt.place(x=30, y=160, width=200, height=20)
        # Field Euler
        self.euler_label.place(x=240, y=77)
        self.euler_txt.place(x=280, y=80, width=200, height=20)
        # Field e
        self.e_label.place(x=260, y=117)
        self.e_txt.place(x=280, y=120, width=200, height=20)
        # Field d
        self.d_label.place(x=260, y=157)
        self.d_txt.place(x=280, y=160, width=200, height=20)

        # Keys Info
        self.key_label.place(x=22, y=190, width=140, height=60)

        # Input Text
        self.inp_label.place(x=20, y=250)
        self.inp_txt.place(x=20, y=275, width=460, height=110)

        # Result Text
        self.out_label.place(x=20, y=390)
        self.out_txt.place(x=20, y=420, width=460, height=110)

        # Buttons
        self.btn_gen.place(x=350, y=20, width=120)
        self.btn_enc.place(x=350, y=185, width=120)
        self.btn_dec.place(x=350, y=215, width=120)

    # Check input value
    def __check_input(self, input_value: str) -> bool:
        try:
            n = int(input_value)
        except ValueError:
            mb.showerror("Error", 'Please enter an integers!')
            return False

        return True

        # Generate keys
    def __btn_generate(self):
        size = int(self.entry_length.get())

        if size < self.min_length:
            mb.showerror("Error", 'Please enter a positive numbers! (n >= 8)')
            return False

        self.cipher = RSA(int(size))
        p, q, n, euler, e, d = self.cipher.params()
        self.n_txt.delete(0, END)
        self.n_txt.insert(0, n)

        self.p_txt.delete(0, END)
        self.p_txt.insert(0, p)

        self.q_txt.delete(0, END)
        self.q_txt.insert(0, q)

        self.euler_txt.delete(0, END)
        self.euler_txt.insert(0, euler)

        self.e_txt.delete(0, END)
        self.e_txt.insert(0, e)

        self.d_txt.delete(0, END)
        self.d_txt.insert(0, d)

    def __btn_encode(self):
        e, n = self.e_txt.get(), self.n_txt.get()
        if not self.__check_input(e): return
        if not self.__check_input(n): return

        txt = self.inp_txt.get("1.0", "end-1c").rstrip('\n')
        # Check outside the alphabet
        for s in txt:
            if ord(s) >= 2048:
                mb.showerror("Error",
                    repr(f"Foreign characters are used: {ord(s)}"))
                return

        result = self.cipher.encode(txt)
        self.out_txt.delete(1.0, END)
        self.out_txt.insert(1.0, result)

    def __btn_decode(self):
        d, n = self.d_txt.get(), self.n_txt.get()
        if not self.__check_input(d): return
        if not self.__check_input(n): return

        txt = self.inp_txt.get("1.0", "end-1c").rstrip('\n')
        # Check outside the alphabet
        reg_val_txt = re.sub(reg_decode, '', txt)

        # There are extra characters
        if len(reg_val_txt) > 0:
            mb.showerror("Error",
                         repr(f"Foreign characters are used: {''.join(set(reg_val_txt))}"))
            return

        result = self.cipher.decode(txt)
        self.out_txt.delete(1.0, END)
        self.out_txt.insert(1.0, result)

    # Centring window
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.window_w) / 2
        y = (sh - self.window_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.window_w, self.window_h, x, y))
