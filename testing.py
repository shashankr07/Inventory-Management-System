import tkinter
import os
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.filedialog import *
from typing import AsyncGenerator

t = Tk()
t.title('HOME')
t.geometry("600x400")
t.configure(bg="beige")
t = Text(t, width=40, height=1, font=("Times", "30", "bold"), fg="white", bg="blue", wrap=WORD)
t.insert(END, "EXPENSE TRACKER")
t.pack(side=TOP)


# --------------------------------------------------------------------------------------------------------------------------------------------------------

def login():
    f1 = Frame(bg="black")
    f1.place(width=600, height=400)
    f1 = Toplevel()
    f1.title("LOGIN")

    l1 = Label(f1, text='Username:', width=14, height=1, font=("Times", "14", "bold"))
    l2 = Label(f1, text='Password:', width=14, height=1, font=("Times", "14", "bold"))
    e1 = Entry(f1, width=14, font=("Times", "15", "bold"))
    e2 = Entry(f1, width=14, show='*', font=("Times", "15", "bold"))
    e1.get()
    e2.get()
    b1 = Button(f1, text='Login', width=20, height=3, bg="green2", activebackground="aquamarine", command=menu)
    b2 = Button(f1, text='BACK', width=20, height=3, bg="orangered", activebackground="aquamarine", command=home)
    l1.grid(row=0, column=0, padx=10)
    e1.grid(row=0, column=2)
    l2.grid(row=1, column=0, pady=10, padx=10)
    e2.grid(row=1, column=2)
    b1.grid(row=2, column=0, pady=20)
    b2.grid(row=2, column=2)


# --------------------------------------------------------------------------------------------------------------------------------------------------------

def signup():
    f2 = Frame(bg="black")
    f2.place(width=600, height=400)
    f2 = Toplevel()
    f2.title("SIGNUP")

    l1 = Label(f2, text='Username:', width=14, height=1, font=("Times", "14", "bold"))
    l2 = Label(f2, text='Password:', width=14, height=1, font=("Times", "14", "bold"), pady=10)
    l3 = Label(f2, text='Confirm Password:', width=14, height=1, font=("Times", "14", "bold"), pady=10)
    l4 = Label(f2, text='Age:', width=14, height=1, font=("Times", "14", "bold"), pady=10)
    l5 = Label(f2, text='Gender:', width=14, height=1, font=("Times", "14", "bold"), pady=10)
    l6 = Label(f2, text='Mobile Number:', width=14, height=1, font=("Times", "14", "bold"), pady=10)

    e1 = Entry(f2, width=14, font=("Times", "14", "bold"))
    e2 = Entry(f2, width=14, show='*', font=("Times", "14", "bold"))
    e3 = Entry(f2, width=14, show='*', font=("Times", "14", "bold"))
    e4 = Entry(f2, width=14, font=("Times", "14", "bold"))

    i = StringVar()

    r1 = Radiobutton(f2, text='Male', value="male", variable=i, font=("Times", "14", "bold"), bg="yellow",
                     activebackground="magenta")
    r2 = Radiobutton(f2, text='Female', value="female", variable=i, font=("Times", "14", "bold"), bg="yellow",
                     activebackground="magenta")

    e6 = Entry(f2, width=14, font=("Times", "14", "bold"))

    e1.get()
    e2.get()
    e3.get()
    e4.get()
    e6.get()

    username = e1.get()
    age = e4.get()
    gender = i.get()
    mobileno = e6.get()
    password = e3.get()

    import mysql.connector as c
    con = c.connect(host="mysql@localhost3306", user="root", passwd="yash", database="expense")
    cursor = con.cursor()
    query = "Insert into signup values('{}', {}, '{}', {}, {})".format(username, age, gender, mobileno, password)

    cursor.execute(query)
    con.commit()

    b1 = Button(f2, text='ADD ACCOUNT', width=15, height=3, bg="dodgerblue", activebackground="azure", command=login)
    b2 = Button(f2, text='BACK', width=15, height=3, bg="orangered", activebackground="azure", command=home)

    l1.grid(row=0, column=0)
    e1.grid(row=0, column=3)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=3)
    l3.grid(row=2, column=0)
    e3.grid(row=2, column=3)
    l4.grid(row=3, column=0)
    e4.grid(row=3, column=3)
    l5.grid(row=5, column=0)
    r1.grid(row=5, column=2)
    r2.grid(row=5, column=3)
    l6.grid(row=7, column=0)
    e6.grid(row=7, column=3)
    b1.grid(row=9, column=0)
    b2.grid(row=9, column=3)


# --------------------------------------------------------------------------------------------------------------------------------------------------------

def menu():
    f3 = Frame(bg="black")
    f3.place(width=600, height=400)
    f3 = Toplevel()
    f3.title("LOGIN")
    b1 = Button(f3, text='DASHBOARD', width=23, height=3, bg="green1", activebackground="azure")
    b2 = Button(f3, text='ADD INCOME/EXPENSE', width=23, height=3, bg="orange", activebackground="azure", command=addie)
    b3 = Button(f3, text='STATISTICS', width=23, height=3, bg="orange", activebackground="azure")
    b4 = Button(f3, text='DELETE INCOME/EXPENSE', width=23, height=3, bg="green1", activebackground="azure")
    b5 = Button(f3, text='NOTES', width=23, height=3, bg="green1", activebackground="azure")
    b6 = Button(f3, text='ACC INFO', width=23, height=3, bg="orange", activebackground="azure")
    b7 = Button(f3, text='FAQs', width=23, height=3, bg="dodgerblue", activebackground="yellow")
    b8 = Button(f3, text='LOGOUT!', width=23, height=3, bg="red", activebackground="yellow", command=home)
    b1.grid(row=0, column=0, pady=5)
    b2.grid(row=0, column=1, pady=5, padx=20)
    b3.grid(row=2, column=0, pady=5)
    b4.grid(row=2, column=1, pady=5)
    b5.grid(row=4, column=0, pady=5)
    b5.grid(row=4, column=0, pady=5)
    b6.grid(row=4, column=1, pady=5)
    b7.grid(row=6, column=0, pady=5)
    b8.grid(row=6, column=1, pady=5)


# --------------------------------------------------------------------------------------------------------------------------------------------------------

def addie():
    f4 = Frame(bg="black")
    f4.place(width=600, height=400)
    f4 = Toplevel()
    f4.title("LOGIN")
    l1 = Label(f4, text='Date', width=14, height=1, font=("Times", "14", "bold"), pady=5)
    l2 = Label(f4, text='Beneficiary Name', width=14, height=1, font=("Times", "14", "bold"), pady=5)
    l3 = Label(f4, text='Category:', width=14, height=1, font=("Times", "14", "bold"), pady=5)
    l4 = Label(f4, text='Amount (in ₹):', width=14, height=1, font=("Times", "14", "bold"), pady=5)
    l5 = Label(f4, text='Mode:', width=14, height=1, font=("Times", "14", "bold"), pady=5)

    i = StringVar()

    r1 = Radiobutton(f4, text='Income', value="income", variable=i, font=("Times", "14", "bold"), bg="yellow",
                     activebackground="magenta")
    r2 = Radiobutton(f4, text='Expense', value="expense", variable=i, font=("Times", "14", "bold"), bg="yellow",
                     activebackground="magenta")
    e1 = Entry(f4, width=14, font=("Times", "14", "bold"))
    e2 = Entry(f4, width=14, show='*', font=("Times", "14", "bold"))
    e3 = Entry(f4, width=14, show='*', font=("Times", "14", "bold"))
    e4 = Entry(f4, width=14, show='*', font=("Times", "14", "bold"))
    e5 = Entry(f4, width=14, show='*', font=("Times", "14", "bold"))

    b1 = Button(f4, text='ADD INOME/EXPENSE', width=20, height=2, bg="dodgerblue", activebackground="azure",
                command=addie)
    b2 = Button(f4, text='BACK', width=15, height=2, bg="orangered", activebackground="azure", command=menu)

    r1.grid(row=0, column=0, pady=10)
    r2.grid(row=0, column=3, pady=10)

    l1.grid(row=1, column=0)
    e1.grid(row=1, column=3)
    l2.grid(row=2, column=0)
    e2.grid(row=2, column=3)
    l3.grid(row=3, column=0)
    e3.grid(row=3, column=3)
    l4.grid(row=4, column=0)
    e4.grid(row=4, column=3)
    l5.grid(row=5, column=0)
    e5.grid(row=5, column=3)

    b1.grid(row=7, column=1, pady=20)
    b2.grid(row=7, column=3, pady=20)


# --------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------

def home():
    f = Frame(bg="black")
    f.place(width=600, height=400)
    b1 = Button(f, text='EXISTING USER', width=20, height=3, bg="green2", activebackground="aquamarine", command=login)
    b2 = Button(f, text='NEW USER', width=20, height=3, bg="coral", activebackground="aquamarine", command=signup)
    b3 = Button(f, text='EXIT', width=20, height=3, bg="red", activebackground="aquamarine", command=f.destroy)
    b1.grid(row=1, column=0, padx=30)
    b2.grid(row=1, column=1, padx=30)
    b3.grid(row=2, column=0, padx=30)
    f.pack()


home()
t.mainloop()





