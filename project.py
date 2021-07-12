from tkinter import *
from pytube import YouTube
root=Tk()
root.geometry("600x500")
root.resizable(0,0)
link=StringVar()
Label(root,text="Link: ",font="arial 15 bold").place(x=270,y=60)
entry=Entry(root,width=70,textvariable=link).place(x=100,y=100)
def downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    Label(root,text="Downloaded")

Button(root,text="Download",bg="black",fg="white",font="arial 12 bold",command=downloader).place(x=250,y=150)
