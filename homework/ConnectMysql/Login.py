import tkinter
from tkinter import messagebox
import mysql.connector
import pyodbc

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="UserAccount")


class Form(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_interface()

    def initialize_interface(self):
        self.parent.title("Login")
        self.parent.config(background="lavender")
        self.parent.geometry("350x200")
        self.parent.resizable(False, False)

        global username
        global password

        username = tkinter.StringVar()
        password = tkinter.StringVar()

        '''create label Username and entry Username'''
        self.labelUser = tkinter.Label(self.parent, text="Username: ", foreground="Black", font="Arial 12 bold")
        self.labelUser.place(x=25, y=25)
        self.entryUser = tkinter.Entry(self.parent, textvariable=username)
        self.entryUser.place(x=150, y=25)

        '''create label Password and entry Password'''
        self.labelPass = tkinter.Label(self.parent, text="Password: ", foreground="Black", font="Arial 12 bold")
        self.labelPass.place(x=25, y=70)
        self.entryPass = tkinter.Entry(self.parent, textvariable=password)
        self.entryPass.place(x=150, y=70)

        '''create button Login'''
        self.buttonLogin = tkinter.Button(self.parent, text="LOGIN", font="Arial 12 bold", command=logs)
        self.buttonLogin.place(height=35, width=100, x=120, y=130)


def logs():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM login WHERE BINARY username = '%s' AND BINARY password = '%s'" % (username.get(), password.get())

    mycursor.execute(sql)

    '''nếu mà nó trả về được bản ghi duy nhất'''
    if mycursor.fetchone():
        messagebox.showinfo("Notification", "Successfully Divided Data")

    else:
        messagebox.showinfo("Notification", "Invalid Credentials")

def main():
    root = tkinter.Tk()
    b = Form(root)
    b.mainloop()


if __name__ == "__main__":
    main()