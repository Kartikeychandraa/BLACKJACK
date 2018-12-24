from Tkinter import *
hel=Tk()
hel.title('HELP')
hel.config(background='purple')
img=PhotoImage(file='hel.gif')

Label(hel,image=img,bd=9,bg='maroon',justify='center').grid(row=0,column=0,columnspan=2)
Label(hel,text='',font="Ariel 15 italic",bg='purple',fg='yellow').grid(row=1,column=1)
Label(hel,text='!! Random number would be added if you press hit !!',font="Ariel 15 italic",bg='purple',fg='yellow').grid(row=1,column=0)
Label(hel,text=' !! if you pass you will not recieve rondom numbers !!',font="Ariel 15 italic",bg='purple',fg='yellow').grid(row=2,column=0)
Label(hel,text='!! Beware score should not go above 21 !!',font="Ariel 15 italic",bg='purple',fg='yellow').grid(row=3,column=0)
Label(hel,text='!! players should have alternate chance to hit or pass !!',font="Ariel 15 italic",bg='purple',fg='yellow').grid(row=4,column=0)
Label(hel,text='Lets begin the Game , Goodluck players ',font="Ariel 15 italic",bg='purple',fg='yellow').grid(row=5,column=0)

hel.mainloop()
