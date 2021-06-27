from tkinter import *
import mysql.connector
import tksheet
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


def database_page():
    root_db = Tk()
    root_db.title("Database")
    root_db.geometry("800x600")
    root_db.config(bg="White")
    root_db.resizable(height=False, width=False)
    pos_wd = int(root_db.winfo_screenwidth()/2 - 700/2)
    pos_hg = int(root_db.winfo_screenheight()/2 - 500/2)
    root_db.geometry("+{}+{}".format(pos_wd, pos_hg-70))
    top_frame = Frame(root_db, bg="#3F6A8A", height=70, width=800)


    # Database Code starts from here
    table_sheet = tksheet.Sheet(root_db,
                                show_x_scrollbar=True,
                                show_y_scrollbar=False,
                                )
    headers = ("Product ID", "Product Name", "Quantity", "Wholesale Price", "Retail Price", "Manufacturing date", "Expiry date")
    table_sheet.headers(headers)
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="root",
                                   database="inventroy_management")

    my_cur = mydb.cursor()
    my_cur.execute("SELECT * FROM inventory")
    my_data = my_cur.fetchall()
    print(len(my_data))
    for i in my_data:
        table_sheet.set_sheet_data([[f"{i[c]}" for c in range(0,7)] for r in range(6)])
    j=0
    for row in my_data:
        z=j
        print(z,j)
        table_sheet.set_row_data(z, values=row)
        j=j+1
    table_sheet.height_and_width(height=300, width=720)
    table_sheet.place(x=40, y=140)

    # Database code ends here '''

    bottom_frame = Frame(root_db, bg="#2C3E50", height=50, width=800)
    label_database = Label(top_frame, text="Database", bg="#3F6A8A", font="arial 25 bold", fg="white")
    edit_button = Button(root_db, text="Edit Database", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15)
    logout_button = Button(root_db, text="Logout", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15)
    view_button  = Button(root_db, text="View Statistics", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15)
    search_variable = StringVar()
    search_entry = Entry(root_db, width=25, bd=3, font="10", textvariable=search_variable)
    search_variable.set("Search")
    search_entry.place(x=500, y=90)
    view_button.place(x=300, y=480)
    logout_button.place(x=530, y=480)
    edit_button.place(x=70, y=480)

    label_database.place(x=10, y=15)
    bottom_frame.place(x=0, y=550)
    top_frame.place(x=0, y=0)
    root_db.mainloop()

database_page()