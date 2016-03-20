#!/usr/bin/env python
from Tkinter import *
import ScrolledText as st
root =Tk()
root.title("ScratchPad")
root.geometry("1280x720")
root.configure(background = 'black')

scratchpad = st.ScrolledText(root,width="1280",height="720")
scratchpad.pack()

text="error"

def create_and_save(filename):
	f=open(filename,"w")
	f.write(text)
	f.close()

def save():
	global text
	text = scratchpad.get(1.0,END)
	window = Toplevel()
	window.title("save")
	window.geometry("430x150")
	window.configure(background="white")
	prompt=Label(window,text="enter file name with extension to save as",bg="white")
	prompt.place(x=0,y=50)
	filename=Entry(window)
	filename.place(x=250,y=50)
	save=Button(window,text="Save",command=lambda:create_and_save(filename.get())).place(x=0,y=100)
	


menu=Menu(root)
root.config(menu=menu)

submenu=Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New",command=save)
submenu.add_command(label="Open",command=save)
submenu.add_command(label="Save",command=save)
submenu.add_separator()
submenu.add_command(label="Close",command=save)

editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Append",command=save)

root.mainloop()

