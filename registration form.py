from tkinter import*
a=Tk()
a.geometry("500x500")
a.title("Registration Form")

l1=Label(a,text="Registration Form",fg="red",font=("bold",20))
l1.pack()


l1=Label(a,text="Name:",font=("bold",15)).place(x=50,y=100)
l2=Label(a,text="Address:",font=("bold",15)).place(x=50,y=140)
l3=Label(a,text="Email:",font=("bold",15)).place(x=50,y=200)
l4=Label(a,text="Sex:",font=("bold",15)).place(x=50,y=240)
c1=Checkbutton(a,text="male",font=("bold",12)).place(x=180,y=240)
c2=Checkbutton(a,text="female",font=("bold",12)).place(x=250,y=240)
l5=Label(a,text="Education:",font=("bold",15)).place(x=50,y=280)
l6=Label(a,text="Phn No:",font=("bold",15)).place(x=50,y=320)

e1=Entry(a)
e1.place(x=200,y=105)
e2=Entry(a)
e2.place(x=200,y=145,width=250,height=50)
e3=Entry(a)
e3.place(x=200,y=205)
e5=Entry(a)
e5.place(x=200,y=285)
e6=Entry(a)
e6.place(x=200,y=325)

b1=Button(a,text="submit",fg="blue",font=("bold",12))
b1.place(x=150,y=380)
mainloop()
