from tkinter import *
import mysql.connector
from tkinter import messagebox
top = Tk()

def logmein():
    uid=e1.get().strip()
    pwd=e2.get().strip()
    db = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="pgcdharamshala")
    cursor = db.cursor()

    RetPass = "select upass from users where uname='"+uid+"'"
    cursor.execute(RetPass)
    myresult = cursor.fetchall()
    passw=myresult[0][0]
    passw=passw.strip()
    if passw == pwd:
        messagebox.showinfo("LOGIN","Welcome to Student Administration System")
        top.destroy()
        import pgcformstu
        
    else:
        messagebox.showinfo("LOGIN","Wrong Password ")
    
            
    
    
def  register():
     import pgcregister
    
    



nme = Label(top,text ="Name").grid(row =0,column =0)
e1 = Entry(top)
e1.grid(row =0,column =1)
password = Label(top,text = "Password")
password.grid(row =1,column =0)
e2 = Entry(top)
e2.grid(row =1,column =1)
reg = Button(top,text ="Register",command=register)
reg.grid(row =4,column =0)
login = Button(top,text ="Login",command=logmein)
login.grid(row =4,column =1)
msg = Label(top,text = "Please Register yourself before First Login")
msg.grid(row =6,column =1)
top.mainloop()
 
