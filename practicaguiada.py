from tkinter import *
from tkinter import messagebox
import sqlite3

tk=Tk()
barramenu=Menu(tk)
tk.config(menu=barramenu,width=300, height=300)
filemenu =Menu(barramenu, tearoff=0)
filemenu.add_command(label="Conectar")
filemenu.add_command(label="Salir")

barramenu.add_cascade(label="bddd", menu=filemenu)



tk.mainloop()