from tkinter import *

user_pass = {}


# Registration Page
def registration_page():
    root = Tk()
    root.resizable(height=False, width=False)
    root.title("Registration")
    root.geometry("700x500")
    root.config(bg="white")
    w_pos = int(root.winfo_screenwidth() / 2 - 700 / 2)
    h_pos = int(root.winfo_screenheight() / 2 - 500 / 2)
    root.geometry("+{}+{}".format(w_pos, h_pos - 40))
    from tkinter import messagebox

    def getval():
        pass1 = set_pass_enrty.get()
        pass2 = confirm_pass_enrty.get()
        pass3 = username_enrty.get()
        if (pass1 == "" and pass2 == "") or (pass3 == ""):
            messagebox.showinfo("Error", "Blank not allowed")

        elif pass1 != pass2:
            messagebox.showinfo("Error", "Password did not match")
        else:
            user_pass.update({1: pass3})
            user_pass.update({2: pass2})
            print(user_pass)
            messagebox.showinfo("", "Registered")
            login_page(user_pass[1], user_pass[2])
            root.quit()

    Frame(root, bg="#3F6A8A", height=70, width=700).place(x=0, y=0)
    Label(root, text="Register", font=("arial 25 bold"), bg="#3F6A8A", fg="white").place(x=10, y=15)

    username = Label(root, text="Username:", font=("arial 13 bold"), bg="white")
    set_pass = Label(root, text="Set Password:", font=("arial 13 bold"), bg="white")
    confirm_pass = Label(root, text="Confirm Password:", font=("arial 13 bold"), bg="white")

    username.place(x=195, y=170)
    set_pass.place(x=165, y=220)
    confirm_pass.place(x=130, y=270)

    usernamevalue = StringVar
    set_passvalue = StringVar
    comfirm_passvalue = StringVar

    username_enrty = Entry(root, textvariable="usernamevalue", bd=2, font="15", width=15)
    set_pass_enrty = Entry(root, textvariable="set_passvalue", bd=2, font="15", width=15, show="*")
    confirm_pass_enrty = Entry(root, textvariable="comfirm_passvalue", bd=2, font="15", width=15, show="*")

    username_enrty.place(x=290, y=170, )
    set_pass_enrty.place(x=290, y=220)
    confirm_pass_enrty.place(x=290, y=270)

    Button(text="Submit", font=("arial 12 bold"), command=lambda:[getval()],height=1,
           width=9, bg="lightblue").place(x=250, y=310)

    Label(root, bg="#2C3E50", fg="white", height=50, width=700).place(x=0, y=450)

    root.mainloop()


# Login Page


def login_page(name, password):
    root2 = Tk()
    root2.resizable(height=False, width=False)
    root2.title("Login Page")
    root2.geometry("800x600")
    from tkinter import messagebox
    def ok():
        user = username_enrty.get()
        passw = password_enrty.get()
        if (user == "" and passw == ""):
            messagebox.showinfo("", "Blank not allowed")

        elif user == name and passw == password:
            messagebox.showinfo("", "Logged in Successful")
            root2.destroy()

        else:
            messagebox.showinfo("", "Invalid details")

    Label(root2, bg="#3F6A8A", height=3, width=120).place(x=0, y=0)
    Label(root2, text="Login Page", font=("arial 25 bold"), bg="#3F6A8A", fg="white").place(x=0, y=0)

    username = Label(root2, text="            Username:", font=("arial 15 bold"))
    password = Label(root2, text="      Password:", font=("arial 15 bold"))

    username.place(x=225, y=200)
    password.place(x=262, y=240)

    usernamevalue = StringVar
    passwordvalue = StringVar

    username_enrty = Entry(root2, textvariable="usernamevalue")
    password_enrty = Entry(root2, textvariable="passwordvalue")

    username_enrty.place(x=410, y=205)
    password_enrty.place(x=410, y=245)

    password_enrty.config(show=".")

    bt = Button(root2, text="Login", font=("arial 15 bold"), command=ok, height=1, width=9, bg="lightblue")
    bt.place(x=360, y=350)

    Label(root2, bg="#2C3E50", fg="white", height=2, width=120).place(x=0, y=564)

    root2.mainloop()


# Option Page


registration_page()
