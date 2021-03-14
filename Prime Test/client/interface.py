from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from tools.prime_test import miller_rabin, solovay_strassen
from tools.gen import generate_prime

# Tkinter interface
class MainForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.frame = Frame(self, bg='#fafafa')
        self.parent = parent
        self.parent.resizable(width=False, height=False)

        self.text_value = tk.StringVar()
        self.text_value.set("Result: ")

        self.window_w = 500
        self.window_h = 350

        self.centerWindow()
        self.initUI()
        self.showUI()

    def initUI(self):
        self.parent.title('Prime Numbers Tools')
        self.parent['bg'] = '#fafafa'

        self.frame = Frame(self.parent, bg='#fafafa')

        # Field N
        self.label_n = Label(self.frame, text='Entry N:', bg='#fafafa', font=20)
        self.entry_n = Entry(self.frame, width=45, justify='center')

        # Field length number
        self.label_bin = Label(self.frame, text='Binary Length:', bg='#fafafa', font=20)
        self.entry_bin = Entry(self.frame, width=20, justify='center')

        # Field test button
        self.test_mr = Button(self.frame, text='Test Miller Rabin', bg='gray', command=self.button_test_mr)
        self.test_ss = Button(self.frame, text='Test Solovay-Strassen', bg='gray', command=self.button_test_ss)

        # Field Result Test
        self.label_result = Label(self.frame, textvariable=self.text_value, bg='#fafafa', font=20)

        # Field gen number
        self.label_num = Label(self.frame, text='Generated number:', bg='#fafafa', font=20)
        self.result_num = Text(self.frame)

        # Field gen button
        self.gen_mr = Button(self.frame, text='Gen Miller Rabin', bg='gray', command=self.button_gen_mr)
        self.gen_ss = Button(self.frame, text='Gen Solovay-Strassen', bg='gray', command=self.button_gen_ss)

    def showUI(self):
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Field N
        self.label_n.place(x=20, y=20)
        self.entry_n.place(x=80, y=24)

        # Field length num
        self.label_bin.place(x=20, y=120)
        self.entry_bin.place(x=130, y=124)

        # Field test button
        self.test_mr.place(x=365, y=20, width=120, height=25)
        self.test_ss.place(x=365, y=60, width=120, height=25)

        # Field Result Test
        self.label_result.place(x=20, y=60)

        # Field gen button
        self.gen_mr.place(x=365, y=120, width=120, height=25)
        self.gen_ss.place(x=365, y=160, width=120, height=25)

        # Field gen number
        self.label_num.place(x=20, y=170)
        self.result_num.place(x=20, y=200, width=460, height=140)

    # Check input value
    def __check_input(self, input_value: str) -> bool:
        try:
            n = int(input_value)
        except ValueError:
            mb.showerror("Error", 'Please enter an integers!')
            return False
        if n < 2:
            mb.showerror("Error", 'Please enter a positive numbers! (n > 1)')
            return False
        return True

    # Test Miller Rabin Button Event
    def button_test_mr(self):
        n = self.entry_n.get()
        if not self.__check_input(n): return
        n = int(n)

        check = miller_rabin(n)
        self.text_value.set('Result: ' + ('Prime' if check else 'Composite'))

    # Test Solovay-Strassen Button Event
    def button_test_ss(self):
        n = self.entry_n.get()
        if not self.__check_input(n): return
        n = int(n)

        check = solovay_strassen(n)
        self.text_value.set('Result: ' + ('Prime' if check else 'Composite'))

    # Generate number with Miller Rabin Button Event
    def button_gen_mr(self):
        bin_len = self.entry_bin.get()
        if not self.__check_input(bin_len): return
        bin_len = int(bin_len)

        n = generate_prime(bin_len, miller_rabin)
        self.result_num.delete(1.0, END)
        self.result_num.insert(1.0, n)

    # Generate number with Solovay-Strassen Button Event
    def button_gen_ss(self):
        bin_len = self.entry_bin.get()
        if not self.__check_input(bin_len): return
        bin_len = int(bin_len)

        n = generate_prime(bin_len, solovay_strassen)
        self.result_num.delete(1.0, END)
        self.result_num.insert(1.0, n)

    # Centring window
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.window_w) / 2
        y = (sh - self.window_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.window_w, self.window_h, x, y))