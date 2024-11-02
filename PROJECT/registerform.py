def doReset():
    messagebox.showinfo("hello","you can reset")

def doNextpage():
    messagebox.showinfo("hello","you are on next page")
Id=Label(parent,text="Student ID").grid(row=1,column=0)
e0=Entry(parent)
e0.grid(row=1,column=1)


'''Name Entry and Label'''
name=Label(parent,text="Name").grid(row=1,column=0)
e1=Entry(parent)
e1.grid(row=1,column=1)

'''Date of birth Label and Entry'''
dob=Label(parent,text="DOB").grid(row=2,column=0)
e2=Entry(parent)
e2.grid(row=2,column=1)

'''Age SpinBox'''
age=Label(parent,text="Age").grid(row=3,column=0)
s1=Spinbox(parent,from_=18, to=27)
s1.grid(row=3,column=1)

'''Fathers name Label and Entry'''
fname=Label(parent,text="Fathers name").grid(row=4,column=0)
e3=Entry(parent)
e3.grid(row=4,column=1)

'''Mothers name Entry and Label'''
mname=Label(parent,text="Mothers name").grid(row=5,column=0)
e4=Entry(parent)
e4.grid(row=5,column=1)

'''Gender Radiobutton'''
var=IntVar()
gender=Label(parent,text="Gender" ).grid(row=6,column=0)
R1=Radiobutton(parent,text="Male",variable=var,value=1).grid(row=6, column=1)
R2=Radiobutton(parent,text="Female",variable=var,value=2).grid(row=6 ,column=2)
R3=Radiobutton(parent,text="Others",variable=var,value=3).grid(row=6, column=3)

'''Checkbutton Qualification'''
CheckVar1=IntVar()
CheckVar2=IntVar()
CheckVar3=IntVar()
CheckVar4=IntVar()
qualification=Label(parent ,text="Educational qualification").grid(row=7,column=0)
C1=Checkbutton(parent,text="10th pass",variable=CheckVar1,onvalue=1,offvalue=0)
C1.grid(row=7,column=1)
C2=Checkbutton(parent,text="12th pass",variable=CheckVar2,onvalue=1,offvalue=0)
C2.grid(row=7,column=2)
C3=Checkbutton(parent,text="Graduate",variable=CheckVar3,onvalue=1,offvalue=0)
C3.grid(row=7,column=3)
C4=Checkbutton(parent,text="PG",variable=CheckVar4,onvalue=1,offvalue=0)
C4.grid(row=7,column=4)

'''Combobox in Course'''
course=Label(parent,text="Courses").grid(row=8,column=0)
n = tk.StringVar()
courses = ttk.Combobox(parent, width = 27, textvariable = n)
courses['values'] =('Python','Java','Html','FSD','C','C++','php','Javascript')
courses.grid(column = 1, row = 8) 

'''Listbox for timings'''
timing=Label(parent,text="Timings" ).grid(row=9,column=0)
listbox=Listbox(parent,selectmode=MULTIPLE)
listbox.insert(1,"9am to 11am")
listbox.insert(2,"10am to 12noon")
listbox.insert(3,"12noon to 2pm")
listbox.insert(4,"1pm to 3pm")
listbox.insert(5,"3pm to 5pm")
listbox.grid(row=9,column=1)

'''Buttons for submit etc'''
submit=Button(parent,text="register",command=doSubmit).grid(row=10,column=0)
reset=Button(parent,text="Reset",command=doReset).grid(row=10,column=1)
nextpage=Button(parent,text="Next page",command=doNextpage).grid(row=10,column=2)

image=Label(parent,text="Upload your passport size photo in jpeg format")
image.grid(row=11,column=0)
imgbtn=Button(parent,text="upload photo",command=openFile).grid(row=12,column=1)


parent.mainloop()




