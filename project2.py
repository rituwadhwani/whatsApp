from tkinter import *
import pywhatkit

'''phone=input("Enter number: ")
msg=input("Enter Message: ")
hr=int(input("Enter hour: "))
m=int(input("Enter minute: "))
pywhatkit.sendwhatmsg(phone,msg,hr,m)
print("message send successfully")'''

root=Tk()
root.geometry("400x400")
n1=StringVar()
n2=StringVar()
n3=IntVar()
n4=IntVar()

c=Canvas(root,bg="pink",height=700,width=900)
c.pack()

l1=Label(root,text=" Phone Number:",bg="white",fg="green",font="arial 10 bold")
l2=Label(root,text=" Message:",bg="white",fg="green",font="arial 10 bold")
l3=Label(root,text=" Hour:",bg="white",fg="green",font="arial 10 bold")
l4=Label(root,text=" Minute:",bg="white",fg="green",font="arial 10 bold")
l1.place(x=5,y=50)
Entry(root,textvariable=n1).place(x=150,y=50)
l2.place(x=5,y=85)
Entry(root,textvariable=n2).place(x=150,y=85)
l3.place(x=5,y=120)
Entry(root,textvariable=n3).place(x=150,y=120)
l4.place(x=5,y=155)
Entry(root,textvariable=n4).place(x=150,y=155)

def call():
    pywhatkit.sendwhatmsg(n1.get(),n2.get(),n3.get(),n4.get())
    print("delivered")

b=Button(root,text="Send Message",command=call,bg="green",font="arial 12 bold",fg="white")
b.place(x=100,y=220)
    
    

         
root.mainloop()
