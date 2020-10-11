from tkinter import *
from tkinter import messagebox

window = Tk()
window.title( "Paint" )

# Heading
frame=LabelFrame(window,text="Painting Program",font=" bold 32 italic",bd=5,relief=GROOVE,bg="light grey")
frame.pack(side="top",fill=BOTH)
label=Label(frame,text="RED  ,  GREEN  ,  BLUE  ",font="arial 20 bold")
label.pack()

# Screen
canvas = Canvas(window,width=600,height=480,bg="white")
canvas.pack(expand = YES, fill = BOTH)

# Different Colours
color = 0
def color_red(event):
    global color
    color = "red"

def color_green(event):
    global color
    color = "green"

def color_blue(event):
    global color
    color = "blue"

# Movement
def paint_1(event):
    x1=event.x
    y1=event.y
    x2=event.x
    y2=event.y
    canvas.create_oval(x1,y1,x2,y2,fill=color)

def paint_2(event):
    x1=event.x
    y1=event.y
    x2=event.x
    y2=event.y
    canvas.create_oval(x1,y1,x2,y2,fill=color)

def paint_3(event):
    x1=event.x
    y1=event.y
    x2=event.x
    y2=event.y
    canvas.create_oval(x1,y1,x2,y2,fill=color)

# Buttons
button1 = Button(window,text="red",width=4,height=2,font=" bold 16 italic",bg="Red",fg="white")
button1.bind("<Button-1>",color_red)
canvas.bind("<B1-Motion>",paint_1)
button1.pack(side="left")

button2 = Button(window,text="green",width=4,height=2,font=" bold 16 italic",bg="Green",fg="white")
button2.bind("<Button-1>",color_green)
canvas.bind("<B1-Motion>",paint_2)
button2.pack(side="left")

button3 = Button(window,text="blue",width=4,height=2,font=" bold 16 italic",bg="Blue",fg="white")
button3.bind("<Button-1>",color_blue)
canvas.bind("<B1-Motion>",paint_3)
button3.pack(side="left")

# Developers Information
def dev_info():
    messagebox.showinfo("Developer's Information","This Program is made by Muhammad Talha.")

button5 = Button(window,text="Developer Information",width=18,font=" bold 16 italic",bg="dark blue",fg="white",command=dev_info)
button5.pack(side="right")


def close(event):
    exit()
canvas.bind("<Double-Button-1>",close)

window.mainloop()