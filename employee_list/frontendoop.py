"""
Here, I've taken frontend.py, the BookStore app, and re-formatted the code to be more
OOP-friendly.
"""

import tkinter
from tkinter import *
from backend import Database

database = Database("company.db")

class Window(object):

    def __init__(self, window):

        self.window = window
        self.window.wm_title("Employee_list")

        l1 = Label(window, text="Name")
        l1.grid(row=0,column=0)

        l2 = Label(window, text="age")
        l2.grid(row=0,column=2)

        l3 = Label(window, text="DOJ")
        l3.grid(row=1,column=0)

        l4 = Label(window, text="Email")
        l4.grid(row=1,column=2)

        self.name_text = StringVar()
        self.e1 = Entry(window,textvariable=self.name_text)
        self.e1.grid(row=0,column=1)

        self.age_text = StringVar()
        self.e2 = Entry(window,textvariable=self.age_text)
        self.e2.grid(row=0,column=3)

        self.doj_text = StringVar()
        self.e3 = Entry(window,textvariable=self.doj_text)
        self.e3.grid(row=1,column=1)

        self.email_text = StringVar()
        self.e4 = Entry(window,textvariable=self.email_text)
        self.e4.grid(row=1,column=3)

        self.list1 = Listbox(window, height=6,width=35)
        self.list1.grid(row=2,column=0, rowspan=6, columnspan=2)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        b1 = Button(window, text="View All", width=12, command=self.view_command)
        b1.grid(row=2,column=3)

        b2 = Button(window, text="Search", width=12, command=self.search_command)
        b2.grid(row=3,column=3)

        b3 = Button(window, text="Add", width=12, command=self.add_command)
        b3.grid(row=4,column=3)

        b4 = Button(window, text="Update", width=12, command=self.update_command)
        b4.grid(row=5,column=3)

        b5 = Button(window, text="Delete", width=12, command=self.delete_command)
        b5.grid(row=6,column=3)

        b6 = Button(window, text="Close", width=12, command=self.window.destroy)
        b6.grid(row=7,column=3)

    def get_selected_row(self, event):
        index=self.list1.curselection()[0]
        self.selected_tuple=self.list1.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[4])

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.name_text.get(),self.age_text.get(),self.doj_text.get(),self.email_text.get()):
            self.list1.insert(END,row)

    def add_command(self):
        database.insert(self.name_text.get(),self.age_text.get(),self.doj_text.get(),self.email_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.name_text.get(),self.age_text.get(),self.doj_text.get(),self.email_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0],self.name_text.get(),self.age_text.get(),self.doj_text.get(),self.email_text.get())

window = Tk()
Window(window)
window.mainloop()
