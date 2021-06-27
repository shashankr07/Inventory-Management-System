from tkinter import *


def login_page(name, password):
    root = Tk()
    root.resizable(height=False, width=False)
    root.title("Login Page")
    root.geometry ("700x500")
    root.config(bg="white")
    w_pos = int(root.winfo_screenwidth()/2 - 700/2)
    h_pos = int(root.winfo_screenheight()/2 - 500/2)
    root.geometry("+{}+{}".format(w_pos, h_pos))
    from tkinter import messagebox

    def ok():
        user= username_enrty.get()
        passw= password_enrty.get()
        if (user == "" and passw ==""):
            messagebox.showinfo("","Blank not allowed")

        elif user == name and passw == password:
            messagebox.showinfo("","Logged in Successful")
            root.destroy()

        else:
            messagebox.showinfo("","Invalid details")

    Frame(root ,bg="#3F6A8A",height=70, width=700).place(x=0, y=0)
    Label(root,text="Login Page" , font=("arial 25 bold") ,bg="#3F6A8A",  fg="white").place(x=10, y=15)

    username= Label(root,text="Username:", font=("arial 15 bold"), bg="white")
    password= Label(root,text= "Password:", font=("arial 15 bold"), bg="white")

    username.place(x=195, y=180)
    password.place(x=195, y=230)

    usernamevalue = StringVar
    passwordvalue = StringVar

    username_enrty = Entry(root, textvariable="usernamevalue", font=15)
    password_enrty = Entry(root, textvariable="passwordvalue", font=15)

    username_enrty.place(x=310,y=185)
    password_enrty.place(x=310,y=235)

    password_enrty.config(show="*")

    Button(text="Login", font=("arial 12 bold"),command=ok,bg="lightblue").place(x=280,y=270)

    Label(root, bg="#2C3E50",fg="white", height=50, width=700).place(x=0, y=450)

    root.mainloop()


login_page("Shashank", "12345")