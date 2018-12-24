from Tkinter import *
sp=Tk()
sp.title("START")
sp.config(background="yellow")
img1=PhotoImage(file="pic.gif")
def fun(e):
    sp.destroy()
    import main
L=Label(sp,image=img1,bg="maroon",bd=9)
L.bind('<Motion>',fun)
L.after(2000,fun)
L.grid(row=0,column=0,columnspan=2)
Label(sp,text="KARTIKEY CHANDRA",font="Ariel 35 italic",bg="yellow",fg="purple").grid(row=1,column=0)
Label(sp,text="171B058",font="Ariel 30 italic",bg="yellow",fg="purple").grid(row=2,column=0)
Label(sp,text="B2",font="Ariel 25 italic",bg="yellow",fg="purple").grid(row=3,column=0)
Label(sp,text="kartikeychandraa@gmail.com",font="Ariel 20 italic",bg="yellow",fg="purple").grid(row=4,column=0)


sp.mainloop()
