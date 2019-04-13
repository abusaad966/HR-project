from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime


def main():

    root = Tk()

    root.title("New driver register")
    root.geometry("400x300")


    # Labels
    label_1=Label(root,text="Driver name : ",font=20,bg="lightblue")
    label_2=Label(root,text="Natioanl ID number : ",font=20,bg="lightblue")
    label_3=Label(root,text="Address : ",font=20,bg="lightblue")
    label_4=Label(root,text="Phone number : ",font=20,bg="lightblue")
    label_5=Label(root,text="Truck No : ",font=20,bg="lightblue")
    label_6=Label(root,text="AL-SAEDI Transportation Co\n 2007-2019 ",font=20,bg="gray")

    # =================================================Entries==============================================

    entrey_1=Entry(root)
    entrey_2=Entry(root)
    entrey_3=Entry(root)
    entrey_4=Entry(root)
    entrey_5=Entry(root)


    #================================================Labels place==============================================
    label_1.grid(row=0,sticky=E)
    label_2.grid(row=2,sticky=E)
    label_3.grid(row=4,sticky=E)
    label_4.grid(row=6,sticky=E)
    label_5.grid(row=7,sticky=E)
    label_6.place(x=100,y=250)


    #=================================================Entries place=========================================
    entrey_1.grid(row=0,column=1)
    entrey_2.grid(row=2,column=1)
    entrey_3.grid(row=4,column=1)
    entrey_4.grid(row=6,column=1)
    entrey_5.grid(row=7,column=1)

    #=================================================Functions============================================
    def register():
            answer = messagebox.askquestion("Confirm", "Do you want to continue")
            if answer == 'yes':
                name = str(entrey_1.get())
                id = entrey_2.get()
                address=str(entrey_3.get())
                phone=entrey_4.get()
                truck=entrey_5.get()

                # Create a database
                db = sqlite3.connect("database.db")
                db.execute("create table if not exists employees(driverName text,NatioanlID int,address text,Phone int,truckNO int)")
                db.execute("insert into employees (driverName,NatioanlID,address,Phone,truckNO) values (?,?,?,?,?)",(name,id,address,phone,truck))
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

    button_1=Button(root,text="Register",font=20,bg="green",command=register)
    button_2=Button(root,text="Quit",font=20,bg="red",command=root.destroy)
    button_3=Button(root,text="Reset",font=20,bg="orange",command=reset)
    button_4=Button(root,text="check",font=20,bg="orange",)

    button_1.grid(row=8,column=1)
    button_2.place(x=300,y=200)
    button_3.place(x=300,y=150)
    button_4.place(x=300,y=110)




    root.mainloop()

if __name__=="__main__" : main()