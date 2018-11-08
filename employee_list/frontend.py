from tkinter import *
import backend
#create window object
window = Tk()

#define 4labels
l1=Label(window, text="Name")
l1.grid(row=0,column=0)

l2=Label(window, text="Age")
l2.grid(row=0,column=2)

l3=Label(window, text="DOJ")
l3.grid(row=1,column=0)

l4=Label(window, text="Email")
l4.grid(row=1,column=2)

#define Entries
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

age_text=StringVar()
e2=Entry(window,textvariable=age_text)
e2.grid(row=0,column=3)

doj_text=StringVar()
e3=Entry(window,textvariable=doj_text)
e3.grid(row=1,column=1)

email_text=StringVar()
e4=Entry(window,textvariable=email_text)
e4.grid(row=1,column=3)

#define ListBox
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#Attach scrollbar to the list
sbl=Scrollbar(window)
sbl.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sbl.set)
sbl.configure(command=list1.yview)

#Define buttons
bl=Button(window,text="View All", width=12)
bl.grid(row=2,column=3)

bl=Button(window,text="Search", width=12)
bl.grid(row=3,column=3)

bl=Button(window,text="Add", width=12)
bl.grid(row=4,column=3)

bl=Button(window,text="Update", width=12)
bl.grid(row=5,column=3)

bl=Button(window,text="Delete", width=12)
bl.grid(row=6,column=3)

bl=Button(window,text="Close", width=12)
bl.grid(row=7,column=3)

window.mainloop()
