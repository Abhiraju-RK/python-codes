from tkinter import*
a=Tk()
a.title("droplist")

cv=("londan","japan","australia")
x=StringVar()
aa=OptionMenu(a,x,*cv)
aa.config(width=15)
x.set("choose the country")
aa.pack()
