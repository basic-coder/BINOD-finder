import os
from tkinter import *
from tkinter import ttk

Finder = Tk()
Finder.geometry("700x400")

Finder.title("Text Finder")
Finder.wm_iconbitmap("1.ico")

def isfind(filename):
    h = r.get()
    with open(filename,"r") as f:
        fileContent = f.read()

    #detect all forms
    if h in fileContent.lower():
        return True
    else:
        return False


def ok():
    f = formatText.get()
    #listing the content of this folder
    dir_cont = os.listdir()
    #result.insert(INSERT, dir_cont)

    nop = 0
    #for each text file run isBinod function
    for item in dir_cont:
        if item.endswith(f):
            result.insert(INSERT, f"dectecting words in {item} \n")
            flag = isfind(item)
            if (flag):
                result.insert(INSERT, f"!!!word found in {item}!!!\n\n")
                nop+=1
            else:
                result.insert(INSERT, f"word not found {item}\n\n")


    result.insert(INSERT,"text detector summary \n")
    result.insert(INSERT, f"{nop} files found \n\n")



T = Label(Finder,text=" Enter Text : ",
              font=("arial",20,"bold"),fg="blue")
T.grid(row=1,column=0,pady=20)

r = Entry(Finder,font=("calibri",20))
r.grid(row=1,column=1,pady=20)

T = Label(Finder,text=" File Format: ",
              font=("arial",20,"bold"),fg="blue")
T.grid(row=2,column=0,pady=20)

formatText = Entry(Finder,font=("calibri",20))
formatText.grid(row=2,column=1,pady=20)



n = Label(Finder,text=" Result : ",
              font=("arial",20,"bold"),fg="blue")
n.grid(row=3,column=0,pady=20)

result = Text(Finder,height=10,width=50,
              font=("arial",20,"bold"),bd=5)
result.grid(row=3,column=1,columnspan=10,pady=20)

button = Button(Finder,text=" Find ",fg="blue",
              font=("calibri",20),bg="powder blue",command=ok)
button.grid(row=5,column=1,pady=20)

mainloop()




