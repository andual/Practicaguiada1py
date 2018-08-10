from tkinter import *
from tkinter import messagebox
import sqlite3

tk=Tk()
barramenu=Menu(tk)
tk.config(menu=barramenu,width=300, height=300)
bddmenu=Menu(barramenu, tearoff=0)
bddmenu.add_command(label="Conectar")
bddmenu.add_command(label="Salir")

barramenu.add_cascade(label="bddd", menu=bddmenu)

borrarmenu=Menu(barramenu, tearoff=0)
borrarmenu.add_command(label="borra campos")

bddmenu=Menu(barramenu, tearoff=0)
bddmenu.add_command(label="Conectar")
bddmenu.add_command(label="Salir")

barrarmenu.add_cascade(label="Borrar", menu=borrar)

barramenu.add_cascade(label="bddd", menu=bddmenu)








tk.mainloop()