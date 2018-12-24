from Tkinter import *
import sqlite3
con=sqlite3.Connection('databaa.db')
cur=con.cursor()
cur.execute("create table if not exists game(player_1 varchar(20),age_1 varchar(3),player_2 varchar(20),age_2 varchar(3))")
con.commit()
m=Tk()
m.title('MAIN')
m.config(background='purple')
Label(m,text="WELCOME TO CASINO ROYALE",justify='center',font='Ariel 30 italic',bg='purple',fg='yellow').grid(row=0,column=0,columnspan=3,)
w=Label(m,text=" ",bg='purple')############################
w.grid(row=1,column=2)
Label(m,text="Enter first Player name:-",bg='purple',font='Ariel 15 ',fg='Yellow',justify='center').grid(row=2,column=1)
global pl1
pl1=Entry(m,font="Ariel 15 italic",justify="center",bd=5)
pl1.grid(row=2,column=2)
Label(m,text=" ",bg='purple').grid(row=3,column=2)
Label(m,text="Enter first Player age:-",bg='purple',font='Ariel 15 ',fg='Yellow',justify='center').grid(row=4,column=1)
global al1
al1=Entry(m,font="Ariel 15 italic",justify="center",bd=5)
al1.grid(row=4,column=2)
Label(m,text=" ",bg='purple').grid(row=5,column=2)
Label(m,text="Enter second Player name:-",bg='purple',font='Ariel 15 ',fg='Yellow',justify='center').grid(row=6,column=1)
global pl2
pl2=Entry(m,font="Ariel 15 italic",justify="center",bd=5)
pl2.grid(row=6,column=2)
q=Label(m,text=" ",bg='purple')
q.grid(row=7,column=2)
Label(m,text="Enter second Player age:-",bg='purple',font='Ariel 15 ',fg='Yellow',justify='center').grid(row=8,column=1)
global age2
age2=Entry(m,font="Ariel 15 italic",justify="center",bd=5)
age2.grid(row=8,column=2)
##################
img=PhotoImage(file='black.gif')
Label(m,image=img,bd=9,bg='maroon',justify="center").grid(row=1,column=1,columnspan=2)
def help1():
    m.destroy()
    import help1
    Button(m,text="RULES",bg="purple",fg="yellow",font='Ariel 15 italic',bd=4).grid(row=9,column=0)            #instructions to play games
                                                        
Button(m,text="RULES",bg="purple",fg="yellow",command=help1,font='Ariel 15 italic',bd=4).grid(row=9,column=0)
def sub():
    a=pl1.get()
    a1=al1.get()
    b=pl2.get()
    b1=age2.get()
    cur=con.cursor()
    cur.execute("insert into game values(?,?,?,?)",(a,a1,b,b1))
    con.commit()
    m.destroy()
    import project
def data():
    a=pl1.get()
    a1=al1.get()
    b=pl2.get()
    b1=age2.get()
    cur=con.cursor()
    cur.execute("insert into game values(?,?,?,?)",(a,a1,b,b1))
    con.commit()
    cur=con.cursor()
    cur.execute("select * from game")
    adm=cur.fetchall()
    ad=Tk()
    ad.config(background="purple")
    Label(ad,text=adm,bg="purple",fg="yellow",font="Ariel 15 italic").pack()
    def exit2():
        ad.destroy()
        
    Button(ad,text="EXIT",command=exit2,bg="purple",fg="yellow",font='Ariel 15 italic',bd=4).pack()
    ad.mainloop()
    con.commit()
Button(m,text="SUBMIT",bg="purple",command=sub,fg="yellow",font='Ariel 15 italic',bd=4).grid(row=9,column=2)
Button(m,text="FOR ADMIN",bg="purple",command=data,fg="yellow",font='Ariel 15 italic',bd=4).grid(row=10,column=1)



m.mainloop()

