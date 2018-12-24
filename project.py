   
import random

from Tkinter import *

root=Tk()
root.title('BLACK_JACK')
root.config(background="purple")
a=Entry(root,font="Ariel 25 italic",justify='center',bd=5,width=4)                  #Input
a.grid(row=0,column=0,columnspan=2)
b=Entry(root,font="Ariel 25 italic",justify='center',bd=5,width=4)                  #Input
b.grid(row=0,column=2,columnspan=2)



player1=0
player2=0
def add():                                                                          #box,hit1
    global player1
    a.delete(0,END)
    player1=player1+random.randint(2,11)
    score1=player1
    a.insert(16,score1)
    if(player1>21):
        player1=0
        player2=0
        root=Tk()
        root.config(background="purple")
        root.title("WINNER")
        Label(root,text="player2 wins the blackjack",font='Ariel 35 bold',bg='purple',fg='Yellow').pack()
        def exit0():
            a.delete(0,END)
            b.delete(0,END)
            root.destroy()
        Button(root,text="EXIT",bg='purple',fg='Yellow',command=lambda:exit0(),font="Ariel 25 underline").pack()
        root.mainloop()
count=0


def stop():
    
    res1=a.get()
    res2=b.get()
    global count
    count=count+1
    if count%2==0:
        player1=0
        player2=0
        root=Tk()
        root.config(background="purple")
        if res1==res2:
            Label(root,text="No one wins blackjack",font="Ariel 35 bold",bg='purple',fg='Yellow').pack()
        elif res1>res2:
            Label(root,text="player1 wins blackjack",font="Ariel 35 bold",bg='purple',fg='Yellow').pack()
        elif res1<res2:
            Label(root,text="player2 wins blackjack",font="Ariel 35 bold",bg='purple',fg='Yellow').pack()
        def exitst():
            a.delete(0,END)
            b.delete(0,END)
            root.destroy()
        Button(root,text="EXIT",command=lambda:exitst(),font="Ariel 25 underline",bg='purple',fg='Yellow').pack()
        root.mainloop()
    Button(root,text="HIT",bg='purple',font='Ariel 15 ',fg='Yellow',bd=3).grid(row=1,column=0)
def stop1():                                                                            #stop2
    res1=a.get()
    res2=b.get()
    global count
    count=count+1
    if count%2==0:
        player1=0
        player2=0
        root=Tk()
        root.config(background="purple")
        if res1==res2:
            Label(root,text="No one wins blackjack",bg='purple',fg='Yellow',font="Ariel 35 bold").pack()
        elif res1>res2:
            Label(root,text="player1 wins blackjack",bg='purple',fg='Yellow',font="Ariel 35 bold").pack()
        elif res1<res2:
            Label(root,text="player2 wins blackjack",bg='purple',fg='Yellow',font="Ariel 35 bold").pack()
        def exitst1():
            a.delete(0,END)
            b.delete(0,END)
            root.destroy()
        Button(root,text="EXIT",command=lambda:exitst1(),font="Ariel 25 italic",bg='purple',fg='Yellow').pack()
        root.mainloop()
        
    
    Button(root,text="HIT",bg='purple',font='Ariel 15 ',fg='Yellow',bd=3).grid(row=1,column=2)
    
def add1():                                                                                         #box,hit2
    global player2
    b.delete(0,END)
    score2=player2+random.randint(2,11)
    player2=score2
    b.insert(16,score2)
    if(player2>21):
        player1=0
        player2=0
        root=Tk()
        root.config(background="purple")
        root.title("WINNER")
        def exit1():
            a.delete(0,END)
            b.delete(0,END)
            root.destroy()
            
            
        Label(root,text="player1 wins the blackjack",font='Ariel 35 bold',bg='purple',fg='Yellow').pack()
        Button(root,text="EXIT",command=lambda:exit1(),font="Ariel 25 italic",bg='purple',fg='Yellow').pack()
        
        root.mainloop()
        
Button(root,text="HIT",bg='purple',font='Ariel 15 ',fg='Yellow',bd=3,command=lambda:add()).grid(row=1,column=0)
Button(root,text="PASS",bg='purple',font='Ariel 15 ',fg='Yellow',bd=3,command=lambda:stop()).grid(row=2,column=1)
Button(root,text="HIT",bg='purple',font='Ariel 15 ',fg='Yellow',bd=3,command=lambda:add1()).grid(row=1,column=2)
Button(root,text="PASS",bg='purple',font='Ariel 15 ',fg='Yellow',bd=3,command=lambda:stop1()).grid(row=2,column=3)
imag=PhotoImage(file="gme.gif")
Label(root,image=imag,bg="maroon",bd=9).grid(row=3,column=0,columnspan=5)

root.mainloop()



