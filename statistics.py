from tkinter import *

import mysql.connector
import tksheet
import matplotlib.pyplot as ploting
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.figure as Figure
import sys


def stats():
    root_stats = Tk()
    root_stats.title("Statistics")
    root_stats.config(bg="white")
    root_stats.resizable(width=FALSE, height=False)
    st_w = int(root_stats.winfo_screenwidth()/2 - root_stats.winfo_reqwidth()/2)
    st_h = int(root_stats.winfo_screenheight()/2 - root_stats.winfo_reqheight()/2)
    root_stats.geometry("+{}+{}".format(st_w-250, st_h-250))
    fr = Frame(root_stats, bg="white", height=50, width=root_stats.winfo_reqwidth())
    lb = Label(root_stats, text="Quantity", font="arial 12 bold", bg="white").pack()
    bt = Button(fr, text="Back", bg="#3F6A8A", font="arial 14 bold", fg="white").place(x=30, y=5)
    bt2 = Button(fr, text="Next", bg="#3F6A8A", font="arial 14 bold", fg="white", command=lambda:[root_stats.destroy(),stats2()]).place(x=120, y=5)
    fr.pack(side=BOTTOM)
    dbs = mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="inventroy_management")
    curse = dbs.cursor()
    curse.execute("SELECT product_name, quantity FROM inventory")
    rs = curse.fetchall()
    lst1 = []
    lst2 = []
    for i in rs:
        for j in range(len(i)):
            if j==0:
                lst1.append(i[j])
            else:
                lst2.append(i[j])
    fg = Figure.Figure(figsize=(7,5), dpi=100)
    y=[i**2 for i in range(101)]
    plt = fg.add_subplot(111)
    x = np.array([])
    y = np.array([])
    arr1 = np.append(x, lst1)
    arr2 = np.append(y, lst2)
    plt.bar(arr1,arr2)
    canvas = FigureCanvasTkAgg(fg, master=root_stats)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, root_stats)
    toolbar.update()
    canvas.get_tk_widget().pack()
    root_stats.mainloop()


def stats2():
    root_st2 = Tk()
    root_st2.title("Statistics")
    root_st2.config(bg="white")
    root_st2.resizable(width=FALSE, height=False)
    st_w = int(root_st2.winfo_screenwidth() / 2 - root_st2.winfo_reqwidth() / 2)
    st_h = int(root_st2.winfo_screenheight() / 2 - root_st2.winfo_reqheight() / 2)
    root_st2.geometry("+{}+{}".format(st_w, st_h))
    lb = Label(root_st2, text="Profit per Product", font="arial 12 bold", bg="white").pack()
    bt = Button(root_st2, text="Back", bg="#3F6A8A", font="arial 14 bold", fg="white", command=lambda:[root_st2.destroy(), stats()]).pack(side=BOTTOM)
    dbs = mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="inventroy_management")
    curse = dbs.cursor()
    curse.execute("SELECT product_name, wholesale_price, retail_price FROM inventory")
    rs = curse.fetchall()
    lst1 = []
    lst2 = []
    lst3 = []
    for i in rs:
        for j in range(len(i)):
            if j == 0:
                lst1.append(i[j])
            elif j==1:
                lst2.append(i[j])
            else:
                lst3.append(i[j])

    fin_lst = []
    zip_obj = zip(lst3, lst2)
    for a, b in zip_obj:
        fin_lst.append(a-b)
    print(fin_lst)
    fg = Figure.Figure(figsize=(8, 5), dpi=100)
    y = [i ** 2 for i in range(101)]
    plt = fg.add_subplot(111)
    x = np.array([])
    y = np.array([])
    arr1 = np.append(x, lst1)
    arr2 = np.append(y, fin_lst)
    plt.plot(lst1, fin_lst, marker='o')
    plt.grid()
    canvas = FigureCanvasTkAgg(fg, master=root_st2)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, root_st2)
    toolbar.update()
    canvas.get_tk_widget().pack()
    root_st2.mainloop()


stats()