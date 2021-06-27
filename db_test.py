from tkinter import *
import mysql.connector
import tksheet
root = Tk("Welcome")
root.geometry("1500x600")
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="root",
                               database="test_database")
sht = tksheet.Sheet(root)
sht.set_sheet_data([[f'{cf*rf}' for cf in range(1,21)] for rf in range(1,20)])
sht.headers("Hello")
sht.height_and_width(height=600, width=1300)
sht.place(x=0, y=0)

my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM student")
my_data = my_cursor.fetchall()
for i in my_data:
    print(i)
root.mainloop()