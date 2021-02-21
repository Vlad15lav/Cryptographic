from tkinter import *
from tkinter import messagebox as mb

from cfg.config import ciphers_config, cipher_num
from client.tableform import TableForm
from tools.utils import check_regex

class MainForm(Frame):
    # Инициализация главной формы
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.cipher_num = 7
        self.parent = parent # root
        self.parent.resizable(width=False, height=False)
        self.canvas = Canvas(self.parent)

        self.form_w = 900
        self.form_h = 630

        self.cipherFrames = []
        self.inputs, self.outputs = [], []
        self.labels, self.entries = [], []
        self.btn_enc, self.btn_dec, self.btn_mat = [], [], []

        self.centerWindow()
        self.initUI()
        self.showUI()

    # Инициализация виждетов для графического интерфейса
    def initUI(self):
        self.parent.title('Шифры замены')

        # Ciphers block
        for i in range(self.cipher_num):
            frm = Frame(self.parent, bg='#a0a0a0' if i % 2 == 0 else '#3f3f3f')
            self.cipherFrames.append(frm)

        # Labels,
        for i in range(self.cipher_num):
            cfg_cipher = ciphers_config[i]

            TxtInput = Text(self.cipherFrames[i])
            self.inputs.append(TxtInput)

            TxtOutput = Text(self.cipherFrames[i])
            self.outputs.append(TxtOutput)

            TxtLabel = Label(self.cipherFrames[i], text=cfg_cipher['name'], justify=CENTER,\
                             bg='#a0a0a0' if i % 2 == 0 else '#3f3f3f', font=16)
            self.labels.append(TxtLabel)

            KeyInput = Entry(self.cipherFrames[i], justify='center')
            KeyInput.insert(END, cfg_cipher['key'])
            self.entries.append(KeyInput)

            btn_encode = Button(self.cipherFrames[i], width=14, name=cfg_cipher['tag']+'_enc', text='Шифрование', bg='gray')
            btn_encode.bind("<Button-1>", self.btn_encode)
            self.btn_enc.append(btn_encode)

            btn_decode = Button(self.cipherFrames[i], width=14, name=cfg_cipher['tag']+'_dec', text='Расшифровать', bg='gray')
            btn_decode.bind("<Button-1>", self.btn_decode)
            self.btn_dec.append(btn_decode)

            btn_matrix = Button(self.cipherFrames[i], width=14, name=cfg_cipher['tag']+'_mat', text='Матрица', bg='gray')
            btn_matrix.bind("<Button-1>", self.btn_matrix)
            self.btn_mat.append(btn_matrix)

    # Отображение виджетов на графическом интерфейсе
    def showUI(self):
        self.canvas.pack()
        for i in range(self.cipher_num):
            self.cipherFrames[i].place(relx=0, rely=i / self.cipher_num, relwidth=1, relheight=1 / self.cipher_num)
            self.inputs[i].place(x=5, y=5, height=80, width=300)
            self.outputs[i].place(x=470, y=5, height=80, width=300)
            self.labels[i].place(x=320, y=0, width=140, height=60)
            self.entries[i].place(x=320, y=65, width=140)
            self.btn_enc[i].place(x=780, y=5)
            self.btn_dec[i].place(x=780, y=31)
            self.btn_mat[i].place(x=780, y=58)

    def btn_encode(self, event):
        # get index cipher
        c_name = str(event.widget).split('.')[-1]
        idx = cipher_num[c_name.split('_')[0]]
        c_cfg = ciphers_config[idx]

        key_txt = self.entries[idx].get()
        key_cfg = ciphers_config[idx]['key']
        if len(key_cfg.split(' ')) > 1:
            k, w, h = key_txt.split(' ')
            key_txt = (k, {int(w), int(h)})
        cipher = c_cfg['class'](key_txt, c_cfg['alphabet'])

        # input text
        txt = self.inputs[idx].get("1.0", "end-1c")
        if check_regex(txt) and c_cfg['reg']:
           mb.showerror("Ошибка", "Допустимые символы А-Я/а-я/ /")
           return
        reg = [s.isupper() for s in txt]

        # output text
        self.outputs[idx].delete(1.0, END)
        for s in txt.split(' '):
            result = cipher.encode(s.upper())
            self.outputs[idx].insert(END, result + ' ')
        txt = self.outputs[idx].get("1.0", "end-1c")

        self.outputs[idx].delete(1.0, END)
        if c_cfg['reg']:
            txt = [s.upper() if reg[i] else s.lower() for i, s in enumerate(txt[:-1])]
        else:
            txt = txt[:-1]
        self.outputs[idx].insert(1.0, ''.join(txt))

    def btn_decode(self, event):
        # get index cipher
        c_name = str(event.widget).split('.')[-1]
        idx = cipher_num[c_name.split('_')[0]]
        c_cfg = ciphers_config[idx]

        key_txt = self.entries[idx].get()
        key_cfg = ciphers_config[idx]['key']
        if len(key_cfg.split(' ')) > 1:
            k, w, h = key_txt.split(' ')
            key_txt = (k, {int(w), int(h)})
        cipher = c_cfg['class'](key_txt, c_cfg['alphabet'])

        # input text
        txt = self.inputs[idx].get("1.0", "end-1c")
        if check_regex(txt) and c_cfg['reg']:
            mb.showerror("Ошибка", "Допустимые символы А-Я/а-я/ /")
            return
        reg = [s.isupper() for s in txt]

        # output text
        self.outputs[idx].delete(1.0, END)
        for s in txt.split(' '):
            result = cipher.decode(s.upper())
            self.outputs[idx].insert(END, result + ' ')
        txt = self.outputs[idx].get("1.0", "end-1c")

        self.outputs[idx].delete(1.0, END)
        if c_cfg['reg']:
            txt = [s.upper() if reg[i] else s.lower() for i, s in enumerate(txt[:-1])]
        else:
            txt = txt[:-1]
        self.outputs[idx].insert(1.0, ''.join(txt))

    def btn_matrix(self, event):
        # get index cipher
        c_name = str(event.widget).split('.')[-1]
        idx = cipher_num[c_name.split('_')[0]]
        c_cfg = ciphers_config[idx]

        key_txt = self.entries[idx].get()
        key_cfg = ciphers_config[idx]['key']
        if len(key_cfg.split(' ')) > 1:
            k, w, h = key_txt.split(' ')
            key_txt = (k, {int(w), int(h)})
        cipher = c_cfg['class'](key_txt, c_cfg['alphabet'])

        newWindow = Toplevel(self.parent)
        TableForm(newWindow, cipher.get_table())

    # Центрируем форму
    def centerWindow(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.form_w) / 2
        y = (sh - self.form_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.form_w, self.form_h, x, y))