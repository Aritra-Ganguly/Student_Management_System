# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:42:47 2023

@author: GANGULY
"""

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passEntry.get()=='':
        messagebox.showerror('Error!','Fields cannot be empty')
    
    elif usernameEntry.get()=='Aritra' and passEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms
        
    else:
        messagebox.showerror('Error','Please enter correct credentials')

window=Tk()

window.geometry('1300x700+0+0')
window.resizable(False,False)
window.title('Login Page for Student Management System')

bgImg = ImageTk.PhotoImage(file='bg.jpg')

bglabel = Label(window,image=bgImg)
bglabel.place(x=0,y=0)

loginFrame = Frame(window,bg='white')
loginFrame.place(x=350,y=100)

logoImg = PhotoImage(file='logo.png')

logoLabel = Label(loginFrame,image=logoImg)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImg = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame,image=usernameImg,text='Username',compound=LEFT,
                      font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry = Entry(loginFrame,font=('times new roman',20),bd=5)
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


passImg = PhotoImage(file='pass.png')
passLabel = Label(loginFrame,image=passImg,text='Password',compound=LEFT,
                      font=('times new roman',20,'bold'),bg='white')
passLabel.grid(row=2,column=0,pady=10,padx=20)

passEntry = Entry(loginFrame,font=('times new roman',20),bd=5)
passEntry.grid(row=2,column=1,pady=10,padx=20)


loginButton = Button(loginFrame,text='Login',font=('times new roman',15),width=15,
                     fg='white',bg='cornflowerblue',activebackground='cornflowerblue',
                     activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)



window.mainloop()