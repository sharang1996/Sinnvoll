import urllib2
from Tkinter import *


root = Tk()
root.title("File Splitter")
root.geometry("1600x700")
root.configure(background = 'black')
icon=PhotoImage(file="/home/sharang/WorkSpace/Python/gui/python.png")

noOfChunks=0
var = StringVar()
var.set('')

label_title=Label(root,text="Sinnvoll File Splitter",bg="black",fg="white",font = "Helvetica 40 bold italic")
label_title.pack(fill=X)

logo=Label(root,image=icon,bg="black").pack(fill=BOTH)

label_link=Label(root,text="enter download link or file path")
label_size=Label(root,text="enter size of each part in MBs")

entry_link=Entry(root)
entry_size=Entry(root)

label_link.place(x=500,y=310)

label_size.place(x=500,y=340)
label_size.config(padx=3)

entry_link.place(x=700,y=310)
entry_size.place(x=700,y=340)


def get_file(link):
	req=urllib2.Request("http://localhost:8080/welcome/static/down.mp4")
	var.set('Downloading file...')
	response = urllib2.urlopen(req)
	data=response.read()
	fout=open("new.mp4","wb")
	fout.write(data)
	var.set('Downloaded file !!!')
	
def split_file(inputFile,chunkSize):
	fin=open(inputFile,"rb")
	byts=len(fin.read())
	fin.seek(0,0)
	global noOfChunks
	noOfChunks=byts/chunkSize
	if(byts%chunkSize):
		++noOfChunks
	print(noOfChunks)
	var.set('splitting file...')
	for i in range(noOfChunks+1):
		
		of="spf%d" % i
		fout=open(of, "wb")
		part=fin.read(chunkSize)
		fout.write(part)
		fout.close()
	var.set('file split!!!')
	fin.close()
	

def join_file(joinFile):
	fout=open(joinFile,"ab")
	var.set('joining file...')
	print(noOfChunks)
	for i in range(noOfChunks+1):
		sf="spf%d" % i
		spf = open(sf,"rb")
		data=spf.read()
		fout.write(data)
		var.set('split files joint!!')
		
		
Split=Button(root,text="Split",command=lambda: split_file("new.mp4",1000000*int(entry_size.get()))).place(x=500,y=370)
Join=Button(root,text="Join",command=lambda: join_file("joint.mp4")).place(x=570,y=370)
Get=Button(root,text="Get File",command=lambda: get_file(entry_link.get())).place(x=870,y=310)
l=Label(root,textvariable = var,bg="black",fg="red").place(x=670,y=380)
label_moto=Label(root,text="SOW.REAP.",fg="white",bg="black",font = "Verdana 15 bold").place(x=610,y=600)
#link is http://localhost:8080/welcome/static/down.mp4
root.mainloop()

