#Importing Required Modules:
import tkinter
from tkinter import *

#Creating the Main Window:
root = Tk()
root.title("Calculator")
root.geometry('500x530+500+200')
root.resizable(False,False)
root.configure(bg = "cornsilk2")

#Creating Widgets and Global Variables:
label_result = Label(root, width=35, height=3, text = "",font=('Times',20))
label_result.pack(pady=0)
equation = ""

#Defining Functions:
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text = equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
        label_result.config(text = result)

#Creating Buttons:
Button(root,text="AC", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'dark goldenrod', command=lambda: clear()).place(x=10, y= 120)
Button(root,text="/", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'indian red', command = lambda: show("/")).place(x=140, y= 120)
Button(root,text="%", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'indian red', command = lambda: show("%")).place(x=270, y= 120)
Button(root,text="x", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'indian red', command = lambda: show("x")).place(x=400, y= 120)

Button(root,text="7", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral', command = lambda: show("7")).place(x=10, y= 200)
Button(root,text="8", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral', command = lambda: show("8")).place(x=140, y= 200)
Button(root,text="9", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral', command = lambda: show("9")).place(x=270, y= 200)
Button(root,text="+", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'indian red', command = lambda: show("+")).place(x=400, y= 200)

Button(root,text="4", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral', command = lambda: show("4")).place(x=10, y= 280)
Button(root,text="5", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral',command = lambda: show("5")).place(x=140, y= 280)
Button(root,text="6", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral',command = lambda: show("6")).place(x=270, y= 280)
Button(root,text="-", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'indian red', command = lambda: show("-")).place(x=400, y= 280)

Button(root,text="1", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral', command = lambda: show("1")).place(x=10, y= 360)
Button(root,text="2", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral', command = lambda: show("2")).place(x=140, y= 360)
Button(root,text="3", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral', command = lambda: show("3")).place(x=270, y= 360)

Button(root,text="0", width=11, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral', command = lambda: show("0")).place(x=10, y= 440)
Button(root,text=".", width=4, height = 1, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'coral', command = lambda: show(".")).place(x=270, y= 440)
Button(root,text="=", width=4, height = 3, font=('Times',25,"bold"), bd=1, fg= '#fff', bg = 'dark goldenrod', command = lambda: calculate()).place(x=400, y= 365)

#Running the Application:
root.mainloop()
