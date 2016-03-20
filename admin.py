from Tkinter import *
root=Tk()
root.title("Admin")
root.geometry("1600x700")
root.configure(background = 'white')
icon=PhotoImage(file="/home/sharang/WorkSpace/Python/gui/python.png")

label_title=Label(root,text="Sinnvoll",bg="white",fg="black",font = "Helvetica 40 bold italic")
label_title.pack(fill=X)

logo=Label(root,image=icon,bg="white").pack(fill=BOTH)

var1 = StringVar()
var1.set('')

var2 = StringVar()
var2.set('')

var3 = StringVar()
var3.set('')

var4 = StringVar()
var4.set('')

var5 = StringVar()
var5.set('')

def getIndex1(*arg):
	sri=0.0
	for i in arg :
		if i==10 :
			sri=sri+1.0
		elif i==11:
			sri=sri+1.2
		elif i==12:
			sri=sri+1.5
		elif i==13:
			sri=sri+1.9
		elif i==14:
			sri=sri+2.4
		elif i==15:
			sri=sri+3.0
		elif i==16:
			sri=sri+3.7
		elif i==17:
			sri=sri+4.5
		elif i==18:
			sri=sri+5.5
		elif i==19:
			sri=sri+7
		else :
			sri=sri+10
	sri=sri/5
	var1.set(str(sri))
	
def getIndex2(*arg):
	sri=0.0
	for i in arg :
		if i==10 :
			sri=sri+1.0
		elif i==11:
			sri=sri+1.2
		elif i==12:
			sri=sri+1.5
		elif i==13:
			sri=sri+1.9
		elif i==14:
			sri=sri+2.4
		elif i==15:
			sri=sri+3.0
		elif i==16:
			sri=sri+3.7
		elif i==17:
			sri=sri+4.5
		elif i==18:
			sri=sri+5.5
		elif i==19:
			sri=sri+7
		else :
			sri=sri+10
	sri=sri/5
	var2.set(str(sri))
		
def getIndex3(*arg):
	sri=0.0
	for i in arg :
		if i==10 :
			sri=sri+1.0
		elif i==11:
			sri=sri+1.2
		elif i==12:
			sri=sri+1.5
		elif i==13:
			sri=sri+1.9
		elif i==14:
			sri=sri+2.4
		elif i==15:
			sri=sri+3.0
		elif i==16:
			sri=sri+3.7
		elif i==17:
			sri=sri+4.5
		elif i==18:
			sri=sri+5.5
		elif i==19:
			sri=sri+7
		else :
			sri=sri+10
	sri=sri/5
	var3.set(str(sri))
	
def getIndex4(*arg):
	sri=0.0
	for i in arg :
		if i==10 :
			sri=sri+1.0
		elif i==11:
			sri=sri+1.2
		elif i==12:
			sri=sri+1.5
		elif i==13:
			sri=sri+1.9
		elif i==14:
			sri=sri+2.4
		elif i==15:
			sri=sri+3.0
		elif i==16:
			sri=sri+3.7
		elif i==17:
			sri=sri+4.5
		elif i==18:
			sri=sri+5.5
		elif i==19:
			sri=sri+7
		else :
			sri=sri+10
	sri=sri/5
	var4.set(str(sri))
	
def getIndex5(*arg):
	sri=0.0
	for i in arg :
		if i==10 :
			sri=sri+1.0
		elif i==11:
			sri=sri+1.2
		elif i==12:
			sri=sri+1.5
		elif i==13:
			sri=sri+1.9
		elif i==14:
			sri=sri+2.4
		elif i==15:
			sri=sri+3.0
		elif i==16:
			sri=sri+3.7
		elif i==17:
			sri=sri+4.5
		elif i==18:
			sri=sri+5.5
		elif i==19:
			sri=sri+7
		else :
			sri=sri+10
	sri=sri/5
	var5.set(str(sri))
	

emp1=Label(root,text="Employee",bg="white",font="20").place(x=0,y=300)
hv1=Label(root,text="Hit Value 1",bg="white",font="20").place(x=150,y=300)
hv2=Label(root,text="Hit Value 2",bg="white",font="20").place(x=300,y=300)
hv3=Label(root,text="Hit Value 3",bg="white",font="20").place(x=450,y=300)
hv4=Label(root,text="Hit Value 4",bg="white",font="20").place(x=600,y=300)
hv5=Label(root,text="Hit Value 5",bg="white",font="20").place(x=750,y=300)
hv6=Label(root,text="Average Risk Index",bg="white",font="20").place(x=900,y=300)

e01=Entry(root)
e01.place(x=0,y=350,width=120)
e02=Entry(root)
e02.place(x=150,y=350,width=50)
e03=Entry(root)
e03.place(x=300,y=350,width=50)
e04=Entry(root)
e04.place(x=450,y=350,width=50)
e05=Entry(root)
e05.place(x=600,y=350,width=50)
e06=Entry(root)
e06.place(x=750,y=350,width=50)
L07=Label(root,textvariable = var1).place(x=900,y=350)

calc1=Button(root,text="calculate",command=lambda: getIndex1(int(e02.get()),int(e03.get()),int(e04.get()),int(e05.get()),int(e06.get()))).place(x=1100,y=350)

e11=Entry(root)
e11.place(x=0,y=400,width=120)
e12=Entry(root)
e12.place(x=150,y=400,width=50)
e13=Entry(root)
e13.place(x=300,y=400,width=50)
e14=Entry(root)
e14.place(x=450,y=400,width=50)
e15=Entry(root)
e15.place(x=600,y=400,width=50)
e16=Entry(root)
e16.place(x=750,y=400,width=50)
L17=Label(root,textvariable = var2).place(x=900,y=400)

calc2=Button(root,text="calculate",command=lambda: getIndex2(int(e12.get()),int(e13.get()),int(e14.get()),int(e15.get()),int(e16.get()))).place(x=1100,y=400)

e21=Entry(root)
e21.place(x=0,y=450,width=120)
e22=Entry(root)
e22.place(x=150,y=450,width=50)
e23=Entry(root)
e23.place(x=300,y=450,width=50)
e24=Entry(root)
e24.place(x=450,y=450,width=50)
e25=Entry(root)
e25.place(x=600,y=450,width=50)
e26=Entry(root)
e26.place(x=750,y=450,width=50)
L27=Label(root,textvariable = var3).place(x=900,y=450)

calc3=Button(root,text="calculate",command=lambda: getIndex3(int(e22.get()),int(e23.get()),int(e24.get()),int(e25.get()),int(e26.get()))).place(x=1100,y=450)

e31=Entry(root)
e31.place(x=0,y=500,width=120)
e32=Entry(root)
e32.place(x=150,y=500,width=50)
e33=Entry(root)
e33.place(x=300,y=500,width=50)
e34=Entry(root)
e34.place(x=450,y=500,width=50)
e35=Entry(root)
e35.place(x=600,y=500,width=50)
e36=Entry(root)
e36.place(x=750,y=500,width=50)
L37=Label(root,textvariable = var4).place(x=900,y=500)

calc4=Button(root,text="calculate",command=lambda: getIndex4(int(e32.get()),int(e33.get()),int(e34.get()),int(e35.get()),int(e36.get()))).place(x=1100,y=500)

e41=Entry(root)
e41.place(x=0,y=550,width=120)
e42=Entry(root)
e42.place(x=150,y=550,width=50)
e43=Entry(root)
e43.place(x=300,y=550,width=50)
e44=Entry(root)
e44.place(x=450,y=550,width=50)
e45=Entry(root)
e45.place(x=600,y=550,width=50)
e46=Entry(root)
e46.place(x=750,y=550,width=50)
L47=Label(root,textvariable = var5).place(x=900,y=550)

calc4=Button(root,text="calculate",command=lambda: getIndex5(int(e42.get()),int(e43.get()),int(e44.get()),int(e45.get()),int(e46.get()))).place(x=1100,y=550)

label_moto=Label(root,text="SOW.REAP.",fg="black",bg="white",font = "Verdana 15 bold").place(x=600,y=650)

root.mainloop()
