from tkinter import *
from tkinter import ttk

window = Tk()
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text = "Tab 1")
notebook.add(tab2, text = "Tab 2")
notebook.pack(expand=TRUE)
Label(tab1, text = "Good morning").pack()
Label(tab2, text = "Good evening").pack()


window.mainloop()