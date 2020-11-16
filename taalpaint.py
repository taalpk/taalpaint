from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image,ImageTk

window=Tk()
window.title("TAAL Paint")
my_image=None
def close():
    exit()

def open_file():
    global my_image
    filename=filedialog.askopenfilename(title="select a file",filetypes=(("Jpeg files",".jpg"),("png files",".png"),("all files","*.*")))
    pic=Image.open(filename)
    resized_pic=pic.resize((800,600))
    my_image=ImageTk.PhotoImage(resized_pic)
    my_image_label=Label(canvas,image=my_image).pack()

def save_file():
    filename=filedialog.asksaveasfilename(title="save as",filetypes=(("postscript_files",".ps"),("all_files","*.*")))
    canvas.update()
    canvas.postscript(file=filename+".ps", colormode='color')
    
def help():
    messagebox.showinfo("Help","Call 1122")

def dev_info():
    messagebox.showinfo("Developer's Information","This Program is Developed By TAAL")
    
main_menu = Menu(window,tearoff=0)
file_menu = Menu(main_menu,tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=close)
main_menu.add_cascade(label="File",menu=file_menu)

help_menu = Menu(main_menu,tearoff=0)
help_menu.add_command(label="About",command=dev_info)
help_menu.add_separator()
help_menu.add_command(label="Help",command=help)
main_menu.add_cascade(label="Help",menu=help_menu)
window.config(menu=main_menu)

iconbar = LabelFrame(window,text="IconBar",bd=4,relief=RIDGE)
iconbar.pack(side="top",fill="both")

img1=ImageTk.PhotoImage(Image.open("file_icon.png"))
icon1 = Button(iconbar,text="",image=img1)
icon1.pack(side="left")

img2=ImageTk.PhotoImage(Image.open("folder-icon.png"))
icon2 = Button(iconbar,text="",image=img2,command=open_file)
icon2.pack(side="left")

img3=ImageTk.PhotoImage(Image.open("floppy_icon.png"))
icon3 = Button(iconbar,text="",image=img3,command=save_file)
icon3.pack(side="left")

scale = Scale(window,from_=20,to=0,orient='vertical',tickinterval=1)
scale.pack(side='left',fill="y")
scale.get()

    
def erase():
    global color
    color = "white"

def clear():
    canvas.delete("all")

x1 = 0
y1 = 0

color = 'black'

def point_1(event):
    global x1
    global y1    
    x1 = event.x
    y1 = event.y

def movement(event):
    global x1
    global y1
    x2=event.x
    y2=event.y
    canvas.create_line((x1,y1,x2,y2),fill=color,width=scale.get())
    x1 = event.x
    y1 = event.y

def line_color(new_color):
    global color
    color = new_color   

canvas=Canvas(window,bg="white")
canvas.pack(expand="yes",fill="both")

colorFrame=LabelFrame(window,text="Colors",bd=4)
colorFrame.pack(side="left")

redButton = Button(colorFrame,text="",bg="red",width=2,command=lambda : line_color('red'))
canvas.bind("<Button-1>",point_1)
canvas.bind("<B1-Motion>",movement)
redButton.pack(side="left")

greenButton = Button(colorFrame,text= "",bg="green",width=2,command=lambda : line_color('green'))
canvas.bind("<Button-1>",point_1)
canvas.bind("<B1-Motion>",movement)
greenButton.pack(side="left")

blueButton = Button(colorFrame,text= "",bg="blue",width=2,command=lambda : line_color('blue'))
canvas.bind("<Button-1>",point_1)
canvas.bind("<B1-Motion>",movement)
blueButton.pack(side="left")

eraseButton = Button(window,text="Erase",height=2,command=erase)
canvas.bind("<B1-Motion>",movement)
eraseButton.pack(side="right")

clearButton = Button(window,text="Clear",height=2,command=clear)
clearButton.pack(side="right")

window.mainloop()
