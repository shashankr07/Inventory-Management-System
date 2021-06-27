from tkinter import *
import tksheet
import mysql.connector

ct=0

def edit_database():
    rooted_db = Tk()
    rooted_db.geometry("870x500")
    rooted_db.resizable(width=False, height=False)
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
        p = mydb.cursor()
        lst = []
        d = table_sheet.get_sheet_data()
        p.execute("TRUNCATE inventory")
        for i in d:
            for k in i:
                lst.append(k)

            ins.execute("INSERT INTO inventory VALUES(%s, %s, %s, %s, %s, %s, %s)", lst)
            mydb.commit()
            lst.clear()


    get_bt = Button(rooted_db, text="Save", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15, command=save)
    add_row = Button(rooted_db, text="Add Row", bg="#3F6A8A", fg="white", font="arial 14 bold", width=15, command=add_row)
    add_row.place(x=200, y=400)
    get_bt.place(x=450, y=400)
    rooted_db.mainloop()


edit_database()
