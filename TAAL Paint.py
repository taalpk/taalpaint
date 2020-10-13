import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

window=tkinter.Tk()
window.title("TAAL Paint")

#def new_tab(event):
#    tab=ttk.Frame(tab_control)
#    tab_control.add(tab,text="Untitled File")
#    tab_control.pack(expand="yes",fill="both")
#    canvas=tkinter.Canvas(tab,bg="white")
#    canvas.pack(expand="yes",fill="both")

def text():
    root = tkinter.Tk()
    TX = Text(root)
    TX.pack(side="right",expand="yes")
    tkinter.messagebox.askyesnocancel("Text","Do you want to save file?")

S = tkinter.Scale(window,orient="vertical")
S.pack(side="left")
#def Scale():
#    S = tkinter.Scale(window,orient="vertical")
#    S.pack(side="left")
   
def save_file():
    f=filedialog.asksaveasfile(mode="w",filetypes=(("text files",".txt"),("all files",".*")))
    file = input("enter lines : ")
    f.write(file)
    f.close()

def open_file():
    result=filedialog.askopenfile(title="Select File Directory")
    for i in result:
        print(i)

def close():
    exit()

def help():
    tkinter.messagebox.showinfo("Help","Muhammad Asad Ullah")

def dev_info():
    tkinter.messagebox.showinfo("Developer's Information","This Program is Developed By TAAL")

main_menu=tkinter.Menu(window,tearoff=0)

file_menu=tkinter.Menu(main_menu,tearoff=0)

file_menu.add_command(label="New File")

file_menu.add_command(label="Open File",command=open_file)

file_menu.add_command(label="Save File",command=save_file)

file_menu.add_separator()

file_menu.add_command(label="Exit",command=close)

main_menu.add_cascade(label="File",menu=file_menu)

main_menu.add_command(label="Help",command=help)

main_menu.add_separator()

main_menu.add_command(label="About",command=dev_info)

icon_frame=tkinter.Frame(window)
icon_frame.pack(fill="both")

new_file=tkinter.Button(icon_frame,text="New File")
new_file.pack(side="left")

open_file=tkinter.Button(icon_frame,text="Open File",command=open_file)
open_file.pack(side="left")

save_file=tkinter.Button(icon_frame,text="Save File",command=save_file)
save_file.pack(side="left")

text_area=tkinter.Button(icon_frame,text="Text Box",command=text)
text_area.pack(side="right")

exit_file=tkinter.Button(icon_frame,text="Exit",command=close)
exit_file.pack(side="right")

#tab_control=ttk.Notebook(window)

#tab=ttk.Frame(tab_control)

#tab_control.add(tab,text="Untitled File")
#tab_control.pack(expand="yes",fill="both")

canvas=tkinter.Canvas(window,bg="white")
canvas.pack(expand="yes",fill="both")

tool_frame=tkinter.LabelFrame(window,text="Tools")
tool_frame.pack(fill="both")

def clrscr():
    canvas.delete("all")

color = 0

def color_red():
    global color
    color = "red"

def color_green():
    global color
    color = "green"

def color_blue():
    global color
    color = "blue"

def pen(event):
    x1=event.x
    y1=event.y
    x2=event.x
    y2=event.y
    canvas.create_oval(x1,y1,x2,y2,fill=color,width=S.get())

button1=tkinter.Button(window,text="Red",bg="red",fg="white",command=color_red)
canvas.bind("<B1-Motion>",pen)
button1.pack(side="left")

button2=tkinter.Button(window,text="Green",bg="green",fg="white",command=color_green)
canvas.bind("<B1-Motion>",pen)
button2.pack(side="left")

button3=tkinter.Button(window,text="Blue",bg="blue",fg="white",command=color_blue)
canvas.bind("<B1-Motion>",pen)
button3.pack(side="left")

clear_screen=tkinter.Button(tool_frame,text="Clear Screen",command=clrscr)
clear_screen.pack(side="left")

window.config(menu=main_menu)

#from PIL import ImageTk,Image

#img=ImageTk.PhotoImage(Image.open("unnamed (1).jpg"))
#my_label=Label(new_file,image=img)
#my_label.pack()

#img2=ImageTk.PhotoImage(Image.open("folder-icon.jpg"))
#my_label=Label(open_file,image=img2)
#my_label.pack()

#img3=ImageTk.PhotoImage(Image.open("download (1).jpg"))
#my_label=Label(save_file,image=img3)
#my_label.pack()

#window.bind("<Control_L><n>")
#window.bind("<Control_R><n>")
#window.bind("<Control_L><N>")
#window.bind("<Control_R><N>")

#window.bind("<Control_L><o>")
#window.bind("<Control_R><o>")
#window.bind("<Control_L><O>")
#window.bind("<Control_R><O>")

#window.bind("<Control_L><s>")
#window.bind("<Control_R><s>")
#window.bind("<Control_L><S>")
#window.bind("<Control_R><S>")

#window.bind("<Control_L><d>")
#window.bind("<Control_R><d>")
#window.bind("<Control_L><D>")
#window.bind("<Control_R><D>")

#window.bind("<Control_L><q>",close)
#window.bind("<Control_R><q>",close)
#window.bind("<Control_L><Q>",close)
#window.bind("<Control_R><Q>",close)

#window.bind("<Alt_L><F4>",close)
#window.bind("<Alt_R><F4>",close)
#window.bind("<Alt_L><F4>",close)
#window.bind("<Alt_R><F4>",close)

window.mainloop()