from tkinter import *


root = None
canv = None
db_frame = None
bt_place_x = 20
bt_place_y = 100
a=None

def option_page():
    root=Tk()
    root.resizable(height=False, width=False)
    root.title("Option Page")
    root.geometry("800x600")
    root.config(bg="white")

    # Scroll code
    db_frame = Frame(root, bg="blue", height=400, width=800)
    canv = Canvas(db_frame, height=400, width=780, bg="WHITE", bd=0)
    canv.pack(side=LEFT)
    scr_frame = Scrollbar(canv)
    db_frame.place(x=0, y=78)
    scr_frame.pack(side=RIGHT, fill=Y)
    scroll_list = Listbox(canv, height=400, width=700, yscrollcommand=scr_frame.set)
    scroll_list.pack(side = LEFT)
    for i in range(100):
        scroll_list.insert(END, "Hello")
    scroll_list.pack(side = LEFT)
    scr_frame.config(command=scroll_list.yview)
    # End scroll code

    w_pos = int(root.winfo_screenwidth()/2 - 800/2)
    h_pos = int(root.winfo_screenheight()/2 - 600/2)
    root.geometry("+{}+{}".format(w_pos, h_pos-40))
    frame = Frame(root, bg="#09174B", width=800, height=80)
    label = Label(frame, text="Option Page", font=("Arial bold", 30), bg="#09174B", fg="white")

    button_AddDatabase = Button(root, text="Add Database", bg="green", fg="White", font=("Arial bold", 15), height=1,
                                width=15, command=add_database)
    button_DeleteDatabase = Button(root, text="Delete Database ", bg="red", fg="White", font=("Arial bold", 15),
                                   height=1, width=15, command=delete_database)
    button_logout = Button(root, text="Logout", bg="blue", fg="White", font=("Arial bold", 15), height=1, width=15)
    frame2 = Frame(root, bg="#09174B", width=800, height=50)
    frame2.place(x=0, y=550)

    button_AddDatabase.place(x=50, y=490)
    button_DeleteDatabase.place(x=300, y=490)
    button_logout.place(x=550, y=490)
    label.place(x=10, y=15)
    frame.place(x=0, y=0)

    root.mainloop()


'''Button functions below'''

def add_database():
    def func():
        bt_db = Button(db_frame, text=entry_database_name.get(), bg="black", fg="White", font=("Arial bold", 15), height=4, width=20)
        bt_db.place(x=20, y=100)
        bt_db = Button(canv, text=entry_database_name.get(), bg="black", fg="White", font=("Arial bold", 15), height=4,
                       width=20)
        bt_db.place(x=20, y=300)
        bt_db = Button(canv, text=entry_database_name.get(), bg="black", fg="White", font=("Arial bold", 15), height=4,
                       width=20)
        bt_db.place(x=20, y=500)

    add_database_name = Tk()
    add_database_name.title("Add Name")
    add_database_name.geometry("400x200")
    wad_pos = int(add_database_name.winfo_screenwidth()/2 - 400/2)
    had_pos = int(add_database_name.winfo_screenheight()/2 - 200/2)
    add_database_name.geometry("+{}+{}".format(wad_pos, had_pos-50))
    label_database_name = Label(add_database_name, text="Database Name:", font="15")
    entry_database_name = Entry(add_database_name)
    label_database_name.place(x=50, y=58)
    entry_database_name.place(x=180, y=60)
    bt_ok = Button(add_database_name, text="Ok", command=lambda:[func(), add_database_name.destroy()] , font="10", width=10)
    bt_ok.place(x=140, y=120)
    add_database_name.mainloop()

def delete_database():
    root_deldb = Tk()
    root_deldb.title("Delete Database")
    root_deldb.geometry("500x300")
    root_deldb.geometry("+{}+{}".format(int(root_deldb.winfo_screenwidth()/2 - 500/2),
                                  int(root_deldb.winfo_screenheight()/2 - 300/2)-40))

    root_deldb.mainloop()

option_page()