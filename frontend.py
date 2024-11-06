from tkinter import *
import backend
window = Tk()
window.title("form")
window.geometry("600x400")
window.iconbitmap('icon/Mainicon.icon')



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
e1 = Entry(window, textvariable=author_text)
e1.grid(row=0, column=3)

year_text = StringVar()
e1 = Entry(window, textvariable=year_text)
e1.grid(row=1, column=1)

isbn_text = StringVar()
e1 = Entry(window, textvariable=isbn_text)
e1.grid(row=1, column=3)

list1 =Listbox(window, height=18, width=50,bg="#BFCC94",fg="black")
list1.grid(row=2, column=1, rowspan=12, columnspan=3)
sb1 = Scrollbar(window)
sb1.grid(row=2, column=5, rowspan=20, columnspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View All",width=15,bg="#B4CDED")
b1.grid(row=2, column=50, columnspan=20)

b2 = Button(window, text="Search Entry",width=15,bg="#B4CDED")
b2.grid(row=4, column=50, columnspan=20)

b3 = Button(window, text=" Add Entry",width=15,bg="#B4CDED")
b3.grid(row=6, column=50, columnspan=20)

b4 = Button(window, text="Update Selection",width=15,bg="#B4CDED")
b4.grid(row=8, column=50, columnspan=20)

b5 = Button(window, text="Delete Selection",width=15,bg="#B4CDED")
b5.grid(row=10, column=50, columnspan=20)

b6 = Button(window, text="close",width=15,bg="#B4CDED")
b6.grid(row=12, column=50, columnspan=20)
window.mainloop()