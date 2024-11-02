from tkinter import *
import mysql.connector
from tkinter import messagebox

top = Tk()


def Registerme():
    snm=e1.get().strip()
    sunm=e2.get().strip()
    spass=e3.get().strip()
    scpass=e4.get().strip()
    
    if spass==scpass:
        db = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="pgcdharamshala") 
        qry = "insert into registration values(%s,%s,%s,%s)"
        values=(snm,sunm,spass,scpass)
        cursor = db.cursor()
        cursor.execute(qry,values)
        db.commit()


        qry = "insert into users values(%s,%s)"
        values=(sunm,spass)
        cursor = db.cursor()
        cursor.execute(qry,values)
        db.commit()
        print(cursor.rowcount, "  Records inserted ")
        messagebox.showinfo("REGISTER","one record register")
        top.destroy()
    else:
        messagebox.showinfo("REGISTER","Password does not match")

 






nme = Label(top,text ="Name").grid(row =0,column =0)
e1 = Entry(top)
e1.grid(row =0,column =1)
username = Label(top,text ="Username").grid(row =1,column =0)
e2 = Entry(top)
e2.grid(row =1,column =1)
password = Label(top,text = "Password")
password.grid(row =2,column =0)
e3 = Entry(top)
e3.grid(row =2,column =1)
cpassword = Label(top,text = "Confirm Password")
cpassword.grid(row =3,column =0)
e4 = Entry(top)
e4.grid(row =3,column =1)
register = Button(top,text ="Register",command=Registerme)
register.grid(row =4,column =1)
top.mainloop()
 
