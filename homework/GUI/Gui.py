from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

def readFile():
    duongdan = path.get()
    f = open(duongdan, 'r', encoding="utf8")
    str = f.read()
    linedata.set(str)
    return linedata

def Openfile():
    datafolder = filedialog.askopenfilename()
    path.set(datafolder)
    return datafolder

def openImage():
    x = Openfile()
    img = Image.open(x)
    img = img.resize((170, 170), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lableImage = Label(Gui, image=img, bd=2, borderwidth=2, relief="ridge")
    lableImage.image = img
    lableImage.place(x=10, y=150)

Gui = tk.Tk()
Gui.geometry("550x400")
Gui.title("GUI")

Title = Label(Gui, text="Gui Python", fg="red", font=("Arial", 16)).place(x=150, y=5)

# Thực hiện chức năng mở 1 file text
btnOpenFolder = Button(Gui, text="1.Brower", command=Openfile, fg="black").place(x=10, y=40)
path = StringVar()
txtPath = Entry(Gui,textvariable=path, width=40).place(x=140, y=45)


# thực hiện chức năng mở ảnh lên để test
openfile = StringVar()
btnOpenFile = Button(Gui, text="3. Open Image", command=openImage).place(x=10, y=115)
lableImage = Label(Gui, bd=2, text="Choose photos to check", borderwidth=2, width=20, height=10, relief="ridge").place(x=10, y=150)

# thực hiện lấy thời gian train trung bình của một ảnh
btnReadFile = Button(Gui, text="2.ReadFile", command=readFile, fg="black").place(x=10, y=80)
linedata = StringVar()
txtLine = Entry(Gui,textvariable=linedata, width=40).place(x=140, y=80)

Gui.mainloop()