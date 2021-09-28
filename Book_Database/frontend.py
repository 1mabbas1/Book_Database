''' This program is a desktop app allowing a user to view and search for specific books, update or delete entries.'''

from tkinter import *
import backend

def viewcom():
    listbox.delete(0,END)
    for row in backend.view():
        listbox.insert(END, row )
        
def searchcom():
    listbox.delete(0,END)
    for row in backend.search(title_text.get(), auth_text.get(), year_text.get(), isbn_text.get()):
        listbox.insert(END, row)

def addcom():
    backend.insert(title_text.get(), auth_text.get(), year_text.get(), isbn_text.get()) 
    listbox.delete(0, END)
    listbox.insert(END, (title_text.get(), auth_text.get(), year_text.get(), isbn_text.get()))

def get_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    
def deletecom():
    backend.delete(selected_tuple[0])
    
def updatecom():
    backend.update(selected_tuple[0],title_text.get(), auth_text.get(), year_text.get(), isbn_text.get())    
    
window = Tk()
#create the labels
l1 = Label(window, text = 'Title')
l1.grid(row = 0, column = 0)

l2 = Label(window, text = 'Author')
l2.grid(row = 0, column = 2)

l3 = Label(window, text = 'Year')
l3.grid(row = 1, column = 0)

l4 = Label(window, text = 'ISBN')
l4.grid(row = 1, column = 2)

#create the entry boxes
title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0 , column = 1)

auth_text = StringVar()
e2 = Entry(window, textvariable = auth_text)
e2.grid(row = 0 , column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1 , column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1 , column = 3)
#listbox and scroll wheel
listbox = Listbox(window, height=6, width = 35 )
listbox.grid(row = 2, column  = 0, rowspan = 6, columnspan = 2)

scroll = Scrollbar(window)
scroll.grid(row = 2, column = 2, rowspan = 6)

listbox.configure(yscrollcommand = scroll.set)
scroll.configure(command = listbox.yview)

listbox.bind('<<ListboxSelect>>', get_row)


#buttions
b1 = Button(window, text = 'View All', width = 12, command = viewcom)
b1.grid(row = 2, column = 3 )

b2 = Button(window, text = 'Search Entry', width = 12, command = searchcom)
b2.grid(row = 3, column = 3 )

b3 = Button(window, text = 'Add Entry', width = 12, command = addcom)
b3.grid(row = 4, column = 3 )

b4= Button(window, text = 'Update', width = 12, command = updatecom)
b4.grid(row = 5, column = 3 )

b5 = Button(window, text = 'Delete', width = 12, command = deletecom )
b5.grid(row = 6, column = 3 )

b6 = Button(window, text = 'Close', width = 12, command = window.destroy)
b6.grid(row = 7, column = 3 )

window.mainloop()

