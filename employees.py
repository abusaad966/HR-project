from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime


def main():

    root = Tk()

    root.title("New driver register")
    root.geometry("600x500")

    #=================================================Frames==============================================

    label_frame=Frame(root)
    label_frame.grid(row=0,rowspan=5)

    entrey_frame=Frame(root)
    entrey_frame.grid(row=0,column=1)

    button_frame=Frame(root)
    button_frame.grid(row=2,column=1,columnspan=3)



    #=================================================Labels==============================================
    label_1=Label(label_frame,text="Driver name : ",font=20,bg="lightblue")
    label_2=Label(label_frame,text="Natioanl ID number : ",font=20,bg="lightblue")
    label_3=Label(label_frame,text="Address : ",font=20,bg="lightblue")
    label_4=Label(label_frame,text="Phone number : ",font=20,bg="lightblue")
    label_5=Label(label_frame,text="Truck No : ",font=20,bg="lightblue")
    label_6=Label(label_frame,text="AL-SAEDI Transportation Co\n 2007-2019 ",font=20,bg="gray")


    # =================================================Entries==============================================

    entrey_1=Entry(entrey_frame)
    entrey_2=Entry(entrey_frame)
    entrey_3=Entry(entrey_frame)
    entrey_4=Entry(entrey_frame)
    entrey_5=Entry(entrey_frame)


    #================================================Labels place==============================================
    label_1.grid(row=1,sticky=E,pady=10)
    label_2.grid(row=2,sticky=E,pady=10)
    label_3.grid(row=3,sticky=E,pady=10)
    label_4.grid(row=4,sticky=E,pady=10)
    label_5.grid(row=5,sticky=E,pady=10)
    label_6.grid(row=6,pady=10)



    #=================================================Entries place=========================================
    entrey_1.grid(row=1,pady=10)
    entrey_2.grid(row=2,pady=15)
    entrey_3.grid(row=3,pady=10)
    entrey_4.grid(row=4,pady=15)
    entrey_5.grid(row=5,pady=10)

    #=================================================Functions============================================
    def register():
        if len(entrey_1.get()) and len(entrey_2.get()) and len(entrey_3.get()) and len(entrey_4.get()) and len(entrey_5.get()) > 1 :
                answer = messagebox.askquestion("Confirm", "Do you want to continue")
                if answer == 'yes':
                    name = str(entrey_1.get())
                    id = entrey_2.get()
                    address=str(entrey_3.get())
                    phone=entrey_4.get()
                    truck=entrey_5.get()

                    # Create a database
                    db = sqlite3.connect("database.db")
                    db.execute("create table if not exists employees(driverName text,NatioanlID int,address text,Phone int,\
                     truckNO int)")
                    db.execute("insert into employees (driverName,NatioanlID,address,Phone,truckNO) values (?,?,?,?,?)",(name,id,address,phone,truck))
                    db.commit()
                    db.close()
                    messagebox.showinfo("completed","Registered successfully!")
                else :
                    entrey_1.delete(0,END)
                    entrey_2.delete(0,END)
                    entrey_3.delete(0,END)
                    entrey_4.delete(0,END)
                    entrey_5.delete(0,END)
    def reset():
        entrey_1.delete(0, END)
        entrey_2.delete(0, END)
        entrey_3.delete(0, END)
        entrey_4.delete(0, END)
        entrey_5.delete(0, END)





    #============================================Buttons========================================

    button_1=Button(button_frame,text="Register",font=20,bg="green",command=register)
    button_2=Button(button_frame,text="Quit",font=20,bg="red",command=root.destroy)
    button_3=Button(button_frame,text="Reset",font=20,bg="orange",command=reset)
    button_4=Button(button_frame,text="check",font=20,bg="orange",)

    button_1.grid(row=0,column=1,padx=10)
    button_2.grid(row=0,column=2,padx=10)
    button_3.grid(row=0,column=3,padx=10)
    button_4.grid(row=0,column=4,padx=10)




    root.mainloop()

if __name__=="__main__" : main()