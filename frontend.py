from tkinter import *
import backend
window = Tk()
window.title("form")
window.geometry("600x400")
window.iconbitmap('icon/Mainicon.icon')

def clear_list():
    list1.delete(0, END)

def fill_list(books):
    for book in books:
        list1.insert(END, book)

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 =Listbox(window, height=18, width=50,bg="#BFCC94",fg="black")
list1.grid(row=2, column=1, rowspan=12, columnspan=3)
sb1 = Scrollbar(window)
sb1.grid(row=2, column=5, rowspan=20, columnspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

def get_selected_row(event):
    global selected_book

    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected_book = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_book[1])
        e2.delete(0, END)
        e2.insert(END, selected_book[2])
        e3.delete(0, END)
        e3.insert(END, selected_book[3])
        e4.delete(0, END)
        e4.insert(END, selected_book[4])


list1.bind('<<ListboxSelect>>', get_selected_row)

def view_command():
    clear_list()
    books = backend.view()
    fill_list(books)

b1 = Button(window, text="View All",width=15,bg="#B4CDED",command=lambda :view_command())
b1.grid(row=2, column=50, columnspan=20)

def search_command():
    clear_list()
    books = backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_list(books)

b2 = Button(window, text="Search Entry",width=15,bg="#B4CDED",command=lambda :search_command())
b2.grid(row=4, column=50, columnspan=20)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

b3 = Button(window, text=" Add Entry",width=15,bg="#B4CDED",command=lambda :add_command())
b3.grid(row=6, column=50, columnspan=20)

def update_command():
    backend.update(selected_book[0], title_text.get(),author_text.get(), year_text.get(), isbn_text.get())
    view_command()

b4 = Button(window, text="Update Selection",width=15,bg="#B4CDED",command=lambda :view_command())
b4.grid(row=8, column=50, columnspan=20)

def delete_command():
    backend.delete(selected_book[0])
    view_command()

b5 = Button(window, text="Delete Selection",width=15,bg="#B4CDED",command=lambda :delete_command())
b5.grid(row=10, column=50, columnspan=20)

b6 = Button(window, text="close",width=15,bg="#B4CDED",command=window.destroy)
b6.grid(row=12, column=50, columnspan=20)

view_command()
window.mainloop()