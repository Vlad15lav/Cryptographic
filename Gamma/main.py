import tkinter as tk
from client.interface import MainForm

def main():
    # Init main form
    root = tk.Tk()
    MainForm(root)
    root.mainloop()

if __name__ == '__main__':
    main()
