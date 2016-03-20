from Tkinter import *
import MySQLdb

db=MySQLdb.connect("localhost","root","sharang","users")

# prepare a cursor object using cursor() method
cursor = db.cursor()


root = Tk()
root.title("Sign In")
root.geometry("1600x700")
root.configure(background = 'white')
icon=PhotoImage(file="/home/sharang/WorkSpace/Python/gui/python.png")
var = StringVar()
var.set('')

var2 = StringVar()
var2.set('')


def insert(name,email,username,password):
	insert= "INSERT INTO details(name,email,username,password) VALUES('"+name+"',"+"'"+email+"',"+"'"+username+"',"+"'"+password+"')"
	try:
		cursor.execute(insert)
		db.commit()
		var.set('registered.')
	except:
		db.rollback()
	
		
def retrieve(username,password):
	get="SELECT * FROM details WHERE username= '"+username+"'"
	try:
		cursor.execute(get)
		result=cursor.fetchone()
		if result[4]==password :
			var2.set("logged in")
			print username
			
		
	except:
		print "Error: unable to fetch data"	

def signup():
	window=Toplevel()
	window.title("Sign Up")
	window.geometry("1600x700")
	window.configure(background="white")
	img=PhotoImage(file="/home/sharang/python2.png")
	window_title=Label(window,text="Sinnvoll",bg="white",fg="black",font = "Helvetica 40 bold italic")
	window_title.pack(fill=X)
	logo=Label(window,image=icon,bg="white").pack(fill=BOTH)
	window_name=Label(window,text="   Name   ").place(x=50,y=180)
	window_email=Label(window,text="   Email    ").place(x=50,y=210)
	window_username=Label(window,text="Username").place(x=50,y=240)
	window_password=Label(window,text=" Password").place(x=50,y=270)
	entry1=Entry(window)
	entry1.place(x=118,y=180)
	entry2=Entry(window)
	entry2.place(x=118,y=210)
	entry3=Entry(window)
	entry3.place(x=118,y=240)
	entry4=Entry(window,show="*")
	entry4.place(x=118,y=270)
	func1(entry1, entry2, entry3, entry4, lamb1)
	register=Button(window,text="REGISTER", command=lambda: insert(entry1.get(),entry2.get(),entry3.get(),entry4.get())).place(x=125,y=300)
	l=Label(window,textvariable = var,bg="white",fg="red")
	l.place(x=125,y=330)
	window.update_idletasks()
	window_moto=Label(window,text="SOW.REAP.",fg="black",bg="white",font = "Verdana 15 bold").place(x=650,y=600)
	window.mainloop()

label_title=Label(root,text="Sinnvoll",bg="white",fg="black",font = "Helvetica 40 bold italic")
label_title.pack(fill=X)

logo=Label(root,image=icon,bg="white").pack(fill=BOTH)

label_name=Label(root,text="username")
label_password=Label(root,text="password")

entry_name=Entry(root)
entry_password=Entry(root,show="*")

label_name.place(x=50,y=210)

label_password.place(x=50,y=240)
label_password.config(padx=3)

entry_name.place(x=118,y=210)
entry_password.place(x=118,y=240)

signIn=Button(root,text="SIGN IN",command=lambda: retrieve(entry_name.get(),entry_password.get())).place(x=50,y=270)
signUp=Button(root,text="SIGN UP",command=signup).place(x=140,y=270)

l=Label(root,textvariable = var2,bg="white",fg="red")
l.place(x=50,y=300)

label_moto=Label(root,text="SOW.REAP.",fg="black",bg="white",font = "Verdana 15 bold").place(x=650,y=600)

root.mainloop()
