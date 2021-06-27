from tkinter import *

root = Tk()
root.geometry("500x500")
frame = Frame(root, bg="blue", height=100, width=34)
bt = Button(text="Click", height=5, width=2)
bt.place(x=0, y=101)
frame.place(x=0, y=0)
root.mainloop()