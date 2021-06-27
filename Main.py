from tkinter import *
import mysql.connector
import tksheet
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.figure as Figure
from tkinter import messagebox

my_db = mysql.connector.connect(host="localhost",
                                user="root",
                                password="root",
                                database="inventroy_management")
user_pass = ["a", "b"]
root_option = None
bt_place_x = 0
bt_place_y = 100
count = 0
root_db = None


# Registration Page
def registration_page():
    root_registration = Tk()
    root_registration.resizable(height=False, width=False)
    root_registration.title("Registration")
    root_registration.geometry("700x500")
    root_registration.config(bg="white")
    w_pos = int(root_registration.winfo_screenwidth() / 2 - 700 / 2)
    h_pos = int(root_registration.winfo_screenheight() / 2 - 500 / 2)
    root_registration.geometry("+{}+{}".format(w_pos, h_pos - 40))
    user_db = my_db.cursor()
    from tkinter import messagebox
    def getval(event):
        pass1 = set_pass_enrty.get()
        pass2 = confirm_pass_enrty.get()
        pass3 = username_enrty.get()
        if (pass1 == "" and pass2 == "") or (pass3 == ""):
            messagebox.showinfo("Error", "Kindly fill all the fields")

        elif pass1 != pass2:
            messagebox.showinfo("Error", "Password did not match")

        else:
            print(user_pass)
            data = (pass3, pass2)
            user_db.execute("INSERT INTO user VALUES(1, %s, %s)", data)
            my_db.commit()
            messagebox.showinfo("Success", "Successfully Registered")
            root_registration.destroy()
            login_page()


    Frame(root_registration, bg="#3F6A8A", height=70, width=700).place(x=0, y=0)
    Label(root_registration, text="Register", font=("arial 25 bold"), bg="#3F6A8A", fg="white").place(x=10, y=15)

    username = Label(root_registration, text="Username:", font=("arial 13 bold"), bg="white")
    set_pass = Label(root_registration, text="Set Password:", font=("arial 13 bold"), bg="white")
    confirm_pass = Label(root_registration, text="Confirm Password:", font=("arial 13 bold"), bg="white")

    username.place(x=195, y=170)
    set_pass.place(x=165, y=220)
    confirm_pass.place(x=130, y=270)

    usernamevalue = StringVar
    set_passvalue = StringVar
    comfirm_passvalue = StringVar

    username_enrty = Entry(root_registration, textvariable="usernamevalue", bd=2, font="15", width=15)
    set_pass_enrty = Entry(root_registration, textvariable="set_passvalue", bd=2, font="15", width=15, show="*")
    confirm_pass_enrty = Entry(root_registration, textvariable="comfirm_passvalue", bd=2, font="15", width=15, show="*")

    username_enrty.place(x=290, y=170)
    set_pass_enrty.place(x=290, y=220)
    confirm_pass_enrty.place(x=290, y=270)

    Button(root_registration, text="Submit", font="arial 12 bold",
           command=lambda: [getval(None)], height=1,
           width=9, bg="lightblue").place(x=250, y=310)

    root_registration.bind('<Return>', getval)

    Label(root_registration, bg="#2C3E50", fg="white", height=50, width=700).place(x=0, y=450)


    root_registration.mainloop()



# Login Page


def login_page():
    root_login = Tk()
    root_login.resizable(height=False, width=False)
    root_login.title("Login Page")
    root_login.geometry("700x500")
    root_login.config(bg="white")
    w_pos = int(root_login.winfo_screenwidth() / 2 - 700 / 2)
    h_pos = int(root_login.winfo_screenheight() / 2 - 500 / 2)
    root_login.geometry("+{}+{}".format(w_pos, h_pos))
    from tkinter import messagebox

    def ok(event):
        user_info = my_db.cursor()
        user_info.execute("SELECT * FROM user")
        data_user = user_info.fetchall()
        user = username_enrty.get()
        passw = password_enrty.get()
        for i in data_user:
            if user == "" and passw == "":
                messagebox.showinfo("Error", "Kindly fill all the fields")

            elif user == i[1] and passw == i[2]:
                messagebox.showinfo("Success", "Logged in Successful")
                root_login.destroy()
                database_page()
            else:
                messagebox.showinfo("Error", "Invalid details")

    Frame(root_login, bg="#3F6A8A", height=70, width=700).place(x=0, y=0)
    Label(root_login, text="Login Page", font=("arial 25 bold"), bg="#3F6A8A", fg="white").place(x=10, y=15)

    username = Label(root_login, text="Username:", font=("arial 15 bold"), bg="white")
    password = Label(root_login, text="Password:", font=("arial 15 bold"), bg="white")

    username.place(x=195, y=180)
    password.place(x=195, y=230)

    usernamevalue = StringVar
    passwordvalue = StringVar

    username_enrty = Entry(root_login, textvariable="usernamevalue", font=15)
    password_enrty = Entry(root_login, textvariable="passwordvalue", font=15)
    username_enrty.focus_set()

    username_enrty.place(x=310, y=185)
    password_enrty.place(x=310, y=235)

    password_enrty.config(show="*")

    Button(root_login, text="Login", font=("arial 12 bold"), command=lambda:ok(None), bg="lightblue").place(x=280, y=270)
    root_login.bind('<Return>', ok)

    Label(root_login, bg="#2C3E50", fg="white", height=50, width=700).place(x=0, y=450)

    root_login.mainloop()


# Option Page


# Database page code

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
                                page_up_down_select_row=True,
                                startup_focus=True)
    table_sheet.enable_bindings('')
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
        table_sheet.set_sheet_data([[f"{i[c]}" for c in range(0,7)] for r in range(len(my_data))])
    j=0
    for row in my_data:
        z=j
        print(z,j)
        table_sheet.set_row_data(z, values=row)
        j=j+1
    table_sheet.height_and_width(height=300, width=720)
    table_sheet.place(x=40, y=140)

    # Database code ends here

    def search(event):
        sr_val = search_entry.get()
        cure = my_db.cursor()
        cure.execute("SELECT * FROM inventory")
        sol = cure.fetchall()
        des = cure.description
        head_lst = []
        val_lst = []
        s = ""
        for j in des:
            for k in j[0]:
                if k=="_":
                    s=s+" "
                else:
                    s=s+k
            hd = s.capitalize()
            head_lst.append(hd)
            s = ""
        print(head_lst)
        pt = 0

        for i in sol:
            if i[1] == sr_val:
                pt=pt+1
                for m in i:
                    val_lst.append(m)

        if pt==0:
            messagebox.showinfo("Error", "No results")
        else:
            root_sr = Tk()
            root_sr.geometry("600x400")
            root_sr.config(bg="white")
            root_sr.title("Search Result")
            root_sr.resizable(width=False, height=False)
            sr_xpos = int(root_sr.winfo_screenwidth() / 2 - 600 / 2)
            sr_ypos = int(root_sr.winfo_screenheight() / 2 - 400 / 2)
            root_sr.geometry("+{}+{}".format(sr_xpos, sr_ypos))
            fr = Frame(root_sr, bg="#3F6A8A", width=600, height=50)
            fr2 = Frame(root_sr, bg="#3F6A8A", width=600, height=40)
            bt = Button(root_sr, text="Back", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15, command=root_sr.destroy)
            fr2.place(x=0, y=360)
            bt.place(x=200, y=300)
            fr.place(x=0, y=0)
            ct = 0
            dum_x = 50
            dum_y = 80
            for p in range(len(val_lst)):
                ct=ct+1
                print(len(val_lst))
                lb = Label(root_sr, text="{}: {}".format(head_lst[p], val_lst[p]), bg="white", font="12")
                if(ct==1):
                    lb.place(x=dum_x, y=dum_y)
                elif(ct==5):
                    dum_y=80
                    lb.place(x=dum_x+200, y=dum_y)
                    dum_x=dum_x+200
                else:
                    lb.place(x=dum_x, y=dum_y+30)
                    dum_y=dum_y+30

            root_sr.mainloop()

    def edit_database():
        rooted_db = Tk()
        rooted_db.geometry("870x500")
        rooted_db.resizable(width=False, height=False)
        rooted_db.title("Edit Database")
        rooted_db.config(bg="white")
        table_sheet = tksheet.Sheet(rooted_db,
                                    show_x_scrollbar=True,
                                    show_y_scrollbar=False,
                                    page_up_down_select_row=True,
                                    startup_focus=True,
                                    table_selected_cells_bg="light blue",
                                    )
        table_sheet.enable_bindings('single_select')
        table_sheet.enable_bindings('row_select')
        table_sheet.enable_bindings('edit_cell')
        table_sheet.enable_bindings('column_select')
        table_sheet.enable_bindings('rc_select')
        table_sheet.enable_bindings("right_click_popup_menu")
        table_sheet.enable_bindings("rc_delete_row")

        headers = ["Product ID", "Product Name", "Quantity", "Wholesale Price", "Retail Price", "Manufacturing date",
                   "Expiry date"]
        table_sheet.headers(headers)
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="root",
                                       database="inventroy_management")
        my_db = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="inventroy_management")

        my_cur = mydb.cursor()
        my_cur.execute("SELECT * FROM inventory")
        my_data = my_cur.fetchall()
        print(len(my_data))
        for i in my_data:
            table_sheet.set_sheet_data([[f"{i[c]}" for c in range(0, 7)] for r in range(len(my_data))])
        j = 0
        for row in my_data:
            z = j
            print(z, j)
            table_sheet.set_row_data(z, values=row)
            j = j + 1
        table_sheet.height_and_width(height=380, width=870)
        table_sheet.place(x=0, y=0)

        def get_data():
            d = table_sheet.get_sheet_data()
            for i in d:
                for k in i:
                    print(k)

        def add_row():
            table_sheet.insert_row(None, idx='end')

        def save():
            ins = mydb.cursor()
            lst = []
            d = table_sheet.get_sheet_data()
            ins.execute("TRUNCATE inventory")
            for i in d:
                for k in i:
                    lst.append(k)

                ins.execute("INSERT INTO inventory VALUES(%s, %s, %s, %s, %s, %s, %s)", lst)
                mydb.commit()
                lst.clear()


        get_bt = Button(rooted_db, text="Save", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15, command=lambda:[rooted_db.destroy(), save(), database_page()])
        add_row = Button(rooted_db, text="Add Row", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15,
                         command=add_row)
        add_row.place(x=200, y=400)
        get_bt.place(x=450, y=400)
        rooted_db.mainloop()

    bottom_frame = Frame(root_db, bg="#2C3E50", height=50, width=800)
    label_database = Label(top_frame, text="Database", bg="#3F6A8A", font="arial 25 bold", fg="white")
    edit_button = Button(root_db, text="Edit Database", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15, command=lambda:[root_db.destroy(), edit_database()])
    logout_button = Button(root_db, text="Logout", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15, command=lambda :[root_db.destroy(),login_page()])
    view_button  = Button(root_db, text="View Statistics", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15, command=stats)
    search_variable = StringVar()
    search_entry = Entry(root_db, width=25, bd=3, font="10", textvariable=search_variable)
    sr_bt = Button(root_db, text="Search", command=lambda:[search(None)])
    root_db.bind('<Return>', search)
    sr_bt.place(x=445, y=89)
    search_entry.place(x=500, y=90)
    view_button.place(x=300, y=480)
    logout_button.place(x=530, y=480)
    edit_button.place(x=70, y=480)

    label_database.place(x=10, y=15)
    bottom_frame.place(x=0, y=550)
    top_frame.place(x=0, y=0)
    root_db.mainloop()


# Button Functions Below


def stats():
    root_stats = Tk()
    root_stats.title("Statistics")
    root_stats.config(bg="white")
    root_stats.resizable(width=FALSE, height=False)
    st_w = int(root_stats.winfo_screenwidth()/2 - root_stats.winfo_reqwidth()/2)
    st_h = int(root_stats.winfo_screenheight()/2 - root_stats.winfo_reqheight()/2)
    root_stats.geometry("+{}+{}".format(st_w-250, st_h-250))
    fr = Frame(root_stats, bg="white", height=50, width=root_stats.winfo_reqwidth())
    lb = Label(root_stats, text="Stock", font="arial 12 bold", bg="white").pack()
    bt = Button(fr, text="Back", bg="#3F6A8A", font="arial 14 bold", fg="white", command=lambda:[root_stats.destroy()]).place(x=30, y=5)
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
    fg = Figure.Figure(figsize=(9,5), dpi=100)
    # y=[i**2 for i in range(101)]
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
    root_st2.geometry("+{}+{}".format(st_w-250, st_h-250))
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
    fg = Figure.Figure(figsize=(10, 5), dpi=100)
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


my_cu = my_db.cursor()
my_cu.execute("SELECT * FROM user")
my_rs = my_cu.fetchall()
'''
for i in my_rs:
    print(i)
'''

if len(my_rs)==0:
    registration_page()
else:
    login_page()
