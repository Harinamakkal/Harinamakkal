from tkinter import *
from tkinter import Entry
from tkinter import ttk
from db import Database
from tkinter import messagebox
db=Database("Employee.db")

root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="green")
root.state("zoomed")
name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()
entries_frame = Frame(root, bg="yellow")
entries_frame.pack(side=TOP,fill=X)
title = Label(entries_frame, text="CREATED BY HARI ",font=("Calibri",18,"bold"),bg="yellow",fg="red")
title.grid(row=0,columnspan=1,padx=10,pady=10)
labelname=Label(entries_frame,text="Name",font=("Calibri",14),bg="yellow",fg="red")
labelname.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtname=Entry(entries_frame,textvariable=name,font=("Calibri",14),width=30)
txtname.grid(row=1,column=1,padx=10,pady=10,sticky="w")
labelage =Label(entries_frame,text = "Age",font=("Calibri",14),bg = "yellow",fg = "red")
labelage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtage = Entry(entries_frame,textvariable=age,font=("Calibri",14,),width =30)
txtage.grid(row=1,column=3,padx=10,pady=10,sticky="w")
labeldoj=Label(entries_frame,text="D.O.J",font =("Calibri",14),bg="yellow",fg="red")
labeldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtdoj=Entry(entries_frame,textvariable= doj, font=("Calibri",14),width=30)
txtdoj.grid(row=2,column = 1,padx=10,pady=10,sticky="w")
labelemail=Label(entries_frame,text="Email",font =("Calibri",14),bg="yellow",fg="red")
labelemail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtEmail =Entry(entries_frame,textvariable= email, font=("Calibri",14),width=30)
txtEmail.grid(row=2,column = 3,padx=10,pady=10,sticky="w")
labelContact=Label(entries_frame,text="Contact No",font =("Calibri",14),bg="yellow",fg="red")
labelContact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtcontact =Entry(entries_frame,textvariable= email, font=("Calibri",14),width=30)
txtcontact.grid(row=3,column = 3,padx=10,pady=10,sticky="w")
labelgender=Label(entries_frame,text="Gender",font =("Calibri",14),bg="yellow",fg="red")
labelgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entries_frame,font=("Calibri",14),width=28,textvariable=gender,state ="readonly")
comboGender['values']=("Male","Female","Others")
comboGender.grid(row=3,column=1,padx=10,sticky="w")
labeladdress=Label(entries_frame,text="Address",font=("Calibri",14),bg ="yellow",fg="red")
labeladdress.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtaddress=Text(entries_frame,width=85,height=5,font=("Calibri",16))
txtaddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0, END)
    txtaddress.insert(END, row[7])
def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def add_employee():
    if txtname.get() == "" or txtage.get() == "" or txtdoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" \
            or txtcontact.get() == "" or txtaddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Data", "Please Enter valid Details")
        return
    db.insert(txtname.get(), txtage.get(), txtdoj.get(), txtEmail.get(), comboGender.get(), txtcontact.get(),
              txtaddress.get(
                  1.0, END))
    messagebox.showinfo("Added", "Record Created")
    clearAll()
    displayall()

def update_employee():
    if txtname.get() == "" or txtage.get() == "" or txtdoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtcontact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0], txtname.get(), txtage.get(), txtdoj.get(), txtEmail.get(), comboGender.get(), txtcontact.get(),
              txtaddress.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    displayall()
def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtaddress.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)
tree_frame=Frame(root,bg="violet")
tree_frame.place(x=0,y=450,width=1980,height=500)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("Calibri",18),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=("calibri",18))
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8))
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="D.O.B")
tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.column("6", width=10)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)
displayall()






root.mainloop()
