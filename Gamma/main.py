import tkinter as tk
from config.config import *
from client.interface import MainForm

def main():
    # Запуск графического интерфейса
    root = tk.Tk()
    MainForm(root)
    root.mainloop()

# Запуск программы
if __name__ == '__main__':
    main()

# import re
#
# from tools.chiper import Gamming
# from tools.tool import get_gamma
# from tkinter import *
# from tkinter import messagebox as mb
#
# # Global parameters
# root = Tk()
# reg_rus = '[А-Я0-9Ё !@#$%^&*\|/+=<>|\,.?~\\\\-]'
# reg_eng = '[A-Z0-9 !@#$%^&*\|/+=<>|\,.?~{}№;:()\\\\-]'
# isRus = True
#
# # Click encode/decode
# def btn_encode():
#     key = KeyInput.get()
#     txt = TxtInput.get("1.0", "end-1c").upper()
#     TxtInput.delete(1.0, END)
#     TxtInput.insert(1.0, txt)
#
#     if key == '' or txt == '':
#         if isRus:
#             mb.showerror("Ошибка", "Пустая строка!")
#         else:
#             mb.showerror("Error", "Empty string!")
#         return
#
#     if isRus:
#         reg_val_key = re.sub(reg_rus, '', key)
#         reg_val_txt = re.sub(reg_rus, '', txt)
#     else:
#         reg_val_key = re.sub(reg_eng, '', key)
#         reg_val_txt = re.sub(reg_eng, '', txt)
#
#     if len(reg_val_key) > 0 or len(reg_val_txt) > 0:
#         if isRus:
#             mb.showerror("Ошибка", repr(f"Используются посторонние символы: {''.join(set(reg_val_key + reg_val_txt))}"))
#         else:
#             mb.showerror("Error", repr(f"Foreign characters are used: {''.join(set(reg_val_key + reg_val_txt))}"))
#         return
#
#     # Check /n end
#     txt = txt.replace("\n","")
#     cipher = Gamming(key=key, isRus=isRus)
#
#     BoxOutput.delete(1.0, END)
#     BoxOutput.insert(1.0, cipher.encode(txt))
#
# # Click for random gamma
# def btn_randkey():
#     txt_lenght = len(TxtInput.get("1.0", "end-1c"))
#     if txt_lenght != 0:
#         #KeyInput.delete(0, END)
#         #KeyInput.insert(0, get_gamma(txt_lenght * 6))
#         cipher = Gamming(isRus=isRus)
#         KeyInput.delete(0, END)
#         KeyInput.insert(0, cipher.bin2char(get_gamma(txt_lenght * 6)))
#     else:
#         if isRus:
#             mb.showerror("Ошибка", "Введите текст!")
#         else:
#             mb.showerror("Error", "Entry text!")
#
# # Click for change lang
# def btn_changlang():
#     global isRus
#     isRus = not isRus
#     if isRus:
#         root.title('Шифр Гаммирования')
#         KeyLabel.config(text='Ввод ключа:')
#         TxtLabel.config(text='Ввод текста:')
#         OutLabel.config(text='Результат:')
#         btn_enc.config(text='За/Дешифровать')
#         btn_key.config(text='Случ. ключ')
#         btn_cl.config(text='Сменить язык')
#         btn_bc.config(text='Двоичный ключ')
#         btn_sc.config(text='Символьный ключ')
#         btn_c.config(text='Очистка')
#     else:
#         root.title('Cipher Gamming')
#         KeyLabel.config(text='Entry Key:')
#         TxtLabel.config(text='Entry Text:')
#         OutLabel.config(text='Result:')
#         btn_enc.config(text='Encode/Decode')
#         btn_key.config(text='Random Key')
#         btn_cl.config(text='Change Language')
#         btn_bc.config(text='Binary key')
#         btn_sc.config(text='Symbol key')
#         btn_c.config(text='Clear')
#
# def btn_clear():
#     KeyInput.delete(0, END)
#     TxtInput.delete("1.0", END)
#     BoxOutput.delete("1.0", END)
#
# # Convert binary code to symbols
# def btn_bincode():
#     key = KeyInput.get()
#     txt = TxtInput.get("1.0", "end-1c")
#     out = BoxOutput.get("1.0", "end-1c")
#     if key == '' or txt == '' or out == '':
#         if isRus:
#             mb.showerror("Ошибка", "Пустая строка!")
#         else:
#             mb.showerror("Error", "Empty string!")
#         return
#
#     if len(key) % 6 != 0:
#         if isRus:
#             mb.showerror("Ошибка", "Не правильная длина кода!")
#         else:
#             mb.showerror("Error", "Incorrect length code!")
#         return
#     unq_sym = ''.join(set(key))
#     if unq_sym != '01' and unq_sym !='10':
#         if isRus:
#             mb.showerror("Ошибка", "Некорректный код!")
#         else:
#             mb.showerror("Error", "Incorrect code!")
#         return
#
#     cipher = Gamming(isRus=isRus)
#     KeyInput.delete(0, END)
#     KeyInput.insert(0, cipher.bin2char(key))
#
#     TxtInput.delete("1.0", END)
#     TxtInput.insert("1.0", cipher.bin2char(txt))
#
#     BoxOutput.delete("1.0", END)
#     BoxOutput.insert("1.0", cipher.bin2char(out))
#
# # Convert symbols code to binary
# def btn_symcode():
#     key = KeyInput.get()
#     txt = TxtInput.get("1.0", "end-1c")
#     out = BoxOutput.get("1.0", "end-1c")
#     if key == '' or txt == '' or out == '':
#         if isRus:
#             mb.showerror("Ошибка", "Пустая строка!")
#         else:
#             mb.showerror("Error", "Empty string!")
#         return
#
#     cipher = Gamming(isRus=isRus)
#     KeyInput.delete(0, END)
#     KeyInput.insert(0, cipher.char2bin(key))
#
#     TxtInput.delete("1.0", END)
#     TxtInput.insert("1.0", cipher.char2bin(txt))
#
#     BoxOutput.delete("1.0", END)
#     BoxOutput.insert("1.0", cipher.char2bin(out))
#
# # Only upper for Entry
# def to_uppercase_key(*args):
#     varKey.set(varKey.get().upper())
#
# varKey = StringVar(root)
# try:
#     varKey.trace_add('write', to_uppercase_key)
# except AttributeError:
#     varKey.trace('w', to_uppercase_key)
#
# ##### Form
# root.title('Шифр Гаммирование')
# root['bg'] = '#fafafa'
# root.geometry('500x400')
#
# root.resizable(width=False, height=False)
# canvas = Canvas(root, height=500, width=400)
# canvas.pack()
#
# frame = Frame(root, bg='#fafafa')
# frame.place(relx=0, rely=0, relwidth=1, relheight=1)
#
# ##### FIELDS
# # Fields for Entry
# frameKEY = Frame(root, bg='#fafafa')
# frameKEY.place(relx=0.25, rely=0.04, relwidth=0.48, relheight=0.09) #
# KeyLabel = Label(frame, text='Ввод ключа:', bg='#fafafa', font=20)
# KeyLabel.place(x=20, y=12) #
#
# scroll_key = Scrollbar(frameKEY, orient='horizontal')
# scroll_key.pack(side=BOTTOM, fill=X) #
# KeyInput = Entry(frameKEY, justify='center', textvariable=varKey, xscrollcommand=scroll_key.set)
# KeyInput.place(x=0, y=0, width=250) #
#
# # Field for txt
# frameTXT = Frame(root, bg='#fafafa')
# frameTXT.place(relx=0.05, rely=0.33, relwidth=0.9, relheight=0.25) #
# TxtLabel = Label(frame, text='Ввод текста:', bg='#fafafa', font=20)
# TxtLabel.place(x=20, y=105) #
#
# scroll_txt = Scrollbar(frameTXT)
# scroll_txt.pack(side=RIGHT, fill=Y) #
# TxtInput = Text(frameTXT, name="txt_tag", yscrollcommand=scroll_txt.set)
# TxtInput.place(x=0, y=0, height=100, width=435) #
#
# # Field for result
# frameOUT = Frame(root, bg='#fafafa')
# frameOUT.place(relx=0.05, rely=0.70, relwidth=0.9, relheight=0.25) #
# OutLabel = Label(frame, text='Результат:', bg='#fafafa', font=20)
# OutLabel.place(x=20, y=250) #
#
# scroll_out = Scrollbar(frameOUT)
# scroll_out.pack(side=RIGHT, fill=Y) #
# BoxOutput = Text(frameOUT, yscrollcommand=scroll_out.set)
# BoxOutput.place(x=0, y=0, height=100, width=435) #
#
# ##### BUTTONS
# # Button call the cipher
# btn_enc = Button(frame, width=14, text='За/Дешифровать', bg='gray', command=btn_encode)
# btn_enc.place(x=380, y=20)
# # Button call the change language
# btn_key = Button(frame, width=14, text='Случ. ключ', bg='gray', command=btn_randkey)
# btn_key.place(x=380, y=55)
# # Button call the change language
# btn_cl = Button(frame, width=14, text='Сменить язык', bg='gray', command=btn_changlang)
# btn_cl.place(x=380, y=90)
# # Button call the convert chars code to bin
# btn_bc = Button(frame, width=14, text='Двоичный ключ', bg='gray', command=btn_symcode)
# btn_bc.place(x=260, y=55)
# # Button call the convert bin code to chars
# btn_sc = Button(frame, width=14, text='Символьный ключ', bg='gray', command=btn_bincode)
# btn_sc.place(x=260, y=90)
# # Button clear
# btn_c = Button(frame, width=14, text='Очистка', bg='gray', command=btn_clear)
# btn_c.place(x=140, y=90)
#
# root.mainloop()