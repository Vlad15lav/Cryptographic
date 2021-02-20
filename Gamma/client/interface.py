import re

from tkinter import *
from tkinter import messagebox as mb
from config.config import reg_rus, reg_eng
from tools.tool import get_gamma

from tools.cipher import Gamma

class MainForm(Frame):
    # Main form init
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(width=False, height=False)
        self.canvas = Canvas(self.parent)

        self.frame = Frame(self.parent, bg='#fafafa')

        self.form_w = 500
        self.form_h = 400
        self.isRus = True

        self.centerWindow()
        self.initUI()
        self.showUI()

    # Init Widgets
    def initUI(self):
        # Key frame
        self.key_frame = Frame(self.parent, bg='#fafafa')
        self.key_label = Label(self.frame, text='Ввод ключа:', bg='#fafafa', font=20)
        self.scroll_key = Scrollbar(self.key_frame, orient='horizontal')

        # Only upper for Entry
        def to_uppercase_key(*args):
            varKey.set(varKey.get().upper())

        varKey = StringVar(self.parent)
        try:
            varKey.trace_add('write', to_uppercase_key)
        except AttributeError:
            varKey.trace('w', to_uppercase_key)
        self.key_input = Entry(self.key_frame, justify='center', textvariable=varKey,
                               xscrollcommand=self.scroll_key.set)

        # Entering text frame
        self.text_frame = Frame(self.parent, bg='#fafafa')
        self.text_label = Label(self.frame, text='Ввод текста:', bg='#fafafa', font=20)
        self.scroll_txt = Scrollbar(self.text_frame)
        self.text_input = Text(self.text_frame, name="txt_tag", yscrollcommand=self.scroll_txt.set)

        # Output text frame
        self.out_frame = Frame(self.parent, bg='#fafafa')
        self.out_label = Label(self.frame, text='Результат:', bg='#fafafa', font=20)
        self.scroll_out = Scrollbar(self.out_frame)
        self.out_input = Text(self.out_frame, yscrollcommand=self.scroll_out.set)

        # Button call the cipher
        self.btn_enc = Button(self.frame, width=14, text='За/Расшифровать', bg='gray', command=self.btn_encode)
        # Button call the change language
        self.btn_key = Button(self.frame, width=14, text='Случ. ключ', bg='gray', command=self.btn_randkey)
        # Button call the change language
        self.btn_cl = Button(self.frame, width=14, text='Сменить язык', bg='gray', command=self.btn_changlang)
        # Button call the convert chars code to bin
        self.btn_bc = Button(self.frame, width=14, text='Двоичный ключ', bg='gray', command=self.btn_symcode)
        # Button call the convert bin code to chars
        self.btn_sc = Button(self.frame, width=14, text='Символьный ключ', bg='gray', command=self.btn_bincode)
        # Button clear
        self.btn_c = Button(self.frame, width=14, text='Очистка', bg='gray', command=self.btn_clear)

    # Show Widgets
    def showUI(self):
        self.canvas.pack()
        self.parent.title('Шифр Гаммирование')
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Init key block frame
        self.key_frame.place(relx=0.25, rely=0.04, relwidth=0.48, relheight=0.09)
        self.key_label.place(x=20, y=12)
        self.scroll_key.pack(side=BOTTOM, fill=X)
        self.key_input.place(x=0, y=0, width=250)

        # Init Entries block frame
        self.text_frame.place(relx=0.05, rely=0.33, relwidth=0.9, relheight=0.25)
        self.text_label.place(x=20, y=105)
        self.scroll_txt.pack(side=RIGHT, fill=Y)
        self.text_input.place(x=0, y=0, height=100, width=435)

        # Init output frame
        self.out_frame.place(relx=0.05, rely=0.70, relwidth=0.9, relheight=0.25)
        self.out_label.place(x=20, y=250)
        self.scroll_out.pack(side=RIGHT, fill=Y)
        self.out_input.place(x=0, y=0, height=100, width=435)

        # Init buttons
        self.btn_enc.place(x=380, y=20)
        self.btn_key.place(x=380, y=55)
        self.btn_cl.place(x=380, y=90)
        self.btn_bc.place(x=260, y=55)
        self.btn_sc.place(x=260, y=90)
        self.btn_c.place(x=140, y=90)

    # Centring Form window
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.form_w) / 2
        y = (sh - self.form_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.form_w, self.form_h, x, y))

    # Click encode/decode
    def btn_encode(self):
        key = self.key_input.get()
        txt = self.text_input.get("1.0", "end-1c").upper()
        self.text_input.delete(1.0, END)
        self.text_input.insert(1.0, txt)

        # Check empty widgets
        if key == '' or txt == '':
            if self.isRus:
                mb.showerror("Ошибка", "Пустая строка!")
            else:
                mb.showerror("Error", "Empty string!")
            return

        # Check outside the alphabet
        if self.isRus:
            reg_val_key = re.sub(reg_rus, '', key)
            reg_val_txt = re.sub(reg_rus, '', txt)
        else:
            reg_val_key = re.sub(reg_eng, '', key)
            reg_val_txt = re.sub(reg_eng, '', txt)

        # There are extra characters
        if len(reg_val_key) > 0 or len(reg_val_txt) > 0:
            if self.isRus:
                mb.showerror("Ошибка",
                             repr(f"Используются посторонние символы: {''.join(set(reg_val_key + reg_val_txt))}"))
            else:
                mb.showerror("Error", repr(f"Foreign characters are used: {''.join(set(reg_val_key + reg_val_txt))}"))
            return

        # Check end line
        txt = txt.replace("\n", "")
        cipher = Gamma(key=key, isRus=self.isRus)

        self.out_input.delete(1.0, END)
        self.out_input.insert(1.0, cipher.encode(txt))

    # Click for random gamma
    def btn_randkey(self):
        txt_lenght = len(self.text_input.get("1.0", "end-1c"))
        if txt_lenght != 0:
            cipher = Gamma(isRus=self.isRus)
            self.key_input.delete(0, END)
            self.key_input.insert(0, cipher.bin2char(get_gamma(txt_lenght * 6)))
        else:
            if self.isRus:
                mb.showerror("Ошибка", "Введите текст!")
            else:
                mb.showerror("Error", "Entry text!")

    # Click for change language
    def btn_changlang(self):
        self.isRus = not self.isRus
        if self.isRus:
            self.parent.title('Шифр Гаммирования')
            self.key_label.config(text='Ввод ключа:')
            self.text_label.config(text='Ввод текста:')
            self.out_label.config(text='Результат:')
            self.btn_enc.config(text='За/Расшифровать')
            self.btn_key.config(text='Случ. ключ')
            self.btn_cl.config(text='Сменить язык')
            self.btn_bc.config(text='Двоичный ключ')
            self.btn_sc.config(text='Символьный ключ')
            self.btn_c.config(text='Очистка')
        else:
            self.parent.title('Cipher Gamming')
            self.key_label.config(text='Entry Key:')
            self.text_label.config(text='Entry Text:')
            self.out_label.config(text='Result:')
            self.btn_enc.config(text='Encode/Decode')
            self.btn_key.config(text='Random Key')
            self.btn_cl.config(text='Change Language')
            self.btn_bc.config(text='Binary key')
            self.btn_sc.config(text='Symbol key')
            self.btn_c.config(text='Clear')

    # Clear Text Widgets
    def btn_clear(self):
        self.key_input.delete(0, END)
        self.text_input.delete("1.0", END)
        self.out_input.delete("1.0", END)

    # Convert binary code to symbols
    def btn_bincode(self):
        key = self.key_input.get()
        txt = self.text_input.get("1.0", "end-1c")
        out = self.out_input.get("1.0", "end-1c")
        if key == '' or txt == '' or out == '':
            if self.isRus:
                mb.showerror("Ошибка", "Пустая строка!")
            else:
                mb.showerror("Error", "Empty string!")
            return

        if len(key) % 6 != 0:
            if self.isRus:
                mb.showerror("Ошибка", "Не правильная длина кода!")
            else:
                mb.showerror("Error", "Incorrect length code!")
            return
        unq_sym = ''.join(set(key))
        if unq_sym != '01' and unq_sym != '10':
            if self.isRus:
                mb.showerror("Ошибка", "Некорректный код!")
            else:
                mb.showerror("Error", "Incorrect code!")
            return

        cipher = Gamma(isRus=self.isRus)
        self.key_input.delete(0, END)
        self.key_input.insert(0, cipher.bin2char(key))

        self.text_input.delete("1.0", END)
        self.text_input.insert("1.0", cipher.bin2char(txt))

        self.out_input.delete("1.0", END)
        self.out_input.insert("1.0", cipher.bin2char(out))

    # Convert symbols code to binary
    def btn_symcode(self):
        key = self.key_input.get()
        txt = self.text_input.get("1.0", "end-1c")
        out = self.out_input.get("1.0", "end-1c")
        if key == '' or txt == '' or out == '':
            if self.isRus:
                mb.showerror("Ошибка", "Пустая строка!")
            else:
                mb.showerror("Error", "Empty string!")
            return

        cipher = Gamma(isRus=self.isRus)
        self.key_input.delete(0, END)
        self.key_input.insert(0, cipher.char2bin(key))

        self.text_input.delete("1.0", END)
        self.text_input.insert("1.0", cipher.char2bin(txt))

        self.out_input.delete("1.0", END)
        self.out_input.insert("1.0", cipher.char2bin(out))