from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector
top=Tk()
top.title("Student Management System")

cn = []
crsnm=""
def showcourses(event):
    deptmnt = event.widget.get()
    list.clear(cn)

    
    db = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="pgcdharamshala")
    qry="select Coursename from courses where Departmentname='"+deptmnt+"'"
    cursor=db.cursor()
    cursor.execute(qry)
    record =cursor.fetchall()
    for row in record:
        cn.append(row[0])
    courses = ttk.Combobox(top, width = 20, values = cn)
    courses.grid(row = 5,column=1)  
   

def addnew():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e5.delete(0,END)
    dptnm=dpts.get()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="pgcdharamshala")
    qry="select max(sroll) from stuinfo where Departmentname='"+dptnm+"'"
    cursor=db.cursor()
    cursor.execute(qry)
    record =cursor.fetchall()
    for row in record:
        oldno=row[0]
        newno=oldno+1
        e1.insert(0,newno)    
    '''e1.configure(state=DISABLED)'''

def retrieve():
      
    rl=entrol.get().strip()
    dnm=dpts.get().strip()
    rdpe.delete(0,END)
    rrle.delete(0,END)
    rnme.delete(0,END)
 
    rage.delete(0,END)
    rcoe.delete(0,END)
    rfe.delete(0,END)
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="pgcdharamshala")
    qry="select * from stuinfo where sroll='"+rl+"' and Departmentname='"+dnm+"'" 
    

    cursor=db.cursor()
    cursor.execute(qry)
    record =cursor.fetchall()
    for row in record:
        rdpe.insert(0,row[0])
        rrle.insert(0,row[1])
        rnme.insert(0,row[2])
        rage.insert(0,row[3])
        rcoe.insert(0,row[4])
        rfe.insert(0,row[5])
    db.commit()
   


def delete():
    rl=entrol.get().strip()
   
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="pgcdharamshala") 
    qry = "delete from stuinfo where sroll="+rl
  
    cursor = db.cursor()
    cursor.execute(qry)
    db.commit()

    messagebox.showinfo("SUCCESS","One record deleted ")





def modify():

    rl=entrol.get().strip()
    dnm=rdpe.get()
    nam=rnme.get().strip()
    ag=rage.get().strip()
    cour=rcoe.get().strip()
    fe=rfe.get().strip()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="pgcdharamshala") 
    
    qry2 = "update stuinfo set stuname='"+nam+"' where sroll='"+rl+"' and Departmentname='"+dnm+"'"
    qry3 = "update stuinfo set stuage='"+ag+"'where sroll='"+rl+"' and Departmentname='"+dnm+"'"
    qry4 = "update stuinfo set stucourse='"+cour+"' where sroll='"+rl+"' and Departmentname='"+dnm+"'"
    qry5 = "update stuinfo set stufee='"+fe+"' where sroll='"+rl+"' and Departmentname='"+dnm+"'"
    
    cursor = db.cursor()
    cursor.execute(qry2)
    cursor.execute(qry3)
    cursor.execute(qry4)
    cursor.execute(qry5)
    db.commit()
    messagebox.showinfo("SUCCESS","One record modify  ")


def insert():
    dnm=dpts.get()
    rl=e1.get().strip()
    name=e2.get().strip()
    age=e3.get().strip()
    course=crsnm
    fee=e5.get().strip()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="pgcdharamshala") 
    qry = "insert into stuinfo values(%s,%s,%s,%s,%s,%s)"
    valus=(dnm,rl,name,age,course,fee)
    cursor = db.cursor()
    cursor.execute(qry,valus)
    db.commit()
    messagebox.showinfo("SUCCESS","One record inserted ")

    









form= Label(top,text= "FORM").grid(row=0,column=1)
d1 = Label(top,text="Department").grid(row =1, column = 0)
'''Combobox in Course'''

dn = []

db = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="pgcdharamshala")
qry="select Deptname from department"

cursor=db.cursor()
cursor.execute(qry)
record =cursor.fetchall()
for row in record:
    dn.append(row[0])

dpts = ttk.Combobox(top, width = 20, values = dn)  
dpts.grid(row = 1, column = 1)
dpts.current()
dpts.bind("<<ComboboxSelected>>", showcourses)




r1 = Label(top,text="Rollnumber").grid(row =2, column = 0)
e1=Entry(top)
e1.grid(row=2,column=1)
nm = Label(top,text="Name").grid(row = 3, column = 0)
e2=Entry(top)
e2.grid(row=3,column=1)
ag=Label(top,text="Age").grid(row= 4,column=0)
e3=Entry(top)
e3.grid(row=4,column=1)

co=Label(top,text="Course").grid(row=5,column=0)

fe=Label(top,text="Fee").grid(row=6,column=0)
e5=Entry(top)
e5.grid(row=6,column=1)
addnew=Button(top,text= "Add new",command=addnew)
addnew.grid(row=7,column=0)
save=Button(top,text="Save",command=insert).grid(row=7,column=1)
entrol=Label(top,text="Enter Roll no.").grid(row=8,column=0)
entrol=Entry(top)
entrol.grid(row=8,column=1)
dele=Button(top,text="Delete",command=delete).grid(row=9,column=0)
ret=Button(top,text="Retrieve",command=retrieve).grid(row=9,column=1)
mod=Button(top,text="Modify",command=modify).grid(row=9,column=2)
ext=Button(top,text="Exit",command=exit).grid(row=10,column=0)


rform= Label(top,text= "RETREIVED RECORD ").grid(row=0,column=1)
d1 = Label(top,text="Department").grid(row =15, column = 0)
'''Combobox in Course'''
rdpe=Entry(top)
rdpe.grid(row=15,column=1)

rrl = Label(top,text="Rollnumber").grid(row =16, column = 0)
rrle=Entry(top)
rrle.grid(row=16,column=1)
rnm = Label(top,text="Name").grid(row = 17, column = 0)
rnme=Entry(top)
rnme.grid(row=17,column=1)
rag=Label(top,text="Age").grid(row= 18,column=0)
rage=Entry(top)
rage.grid(row=18,column=1)

rco=Label(top,text="Course").grid(row=19,column=0)
rcoe=Entry(top)
rcoe.grid(row=19,column=1)
rfe=Label(top,text="Fee").grid(row=20,column=0)
rfe=Entry(top)
rfe.grid(row=20,column=1)


top.mainloop()
