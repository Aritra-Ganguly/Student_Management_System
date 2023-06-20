# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:40:02 2023

@author: GANGULY
"""

from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

# Functionality Part


def iexit():
    result = messagebox.askyesno('Confirm','Do you Want to Exit?')
    if result:
        root.destroy()
    else:
        pass


def export_data():
    url = filedialog.asksaveasfile(defaultextension = '.csv')
    print(url)
    indexing = studentTable.get_children()
    #print(indexing)
    newlist = []
    for index in indexing:
        content = studentTable.item(index)
        datalist = content['values']
        #print(datalist)
        newlist.append(datalist)
    #print(newlist)
    
    table = pandas.DataFrame(newlist, columns=['Id', 'Name', 'Department', 'Mobile', 'Email', 'Address', 'Gender', 'DOB', 'Added Date', 'Added Time'])
    table.to_csv(url, index = False)
    messagebox.showinfo('Success','Data is saved successfully')


def toplevel_data(title,button_text,command):
    
    global idEntry,nameEntry,deptEntry,mobileEntry,emailEntry,addressEntry,genderEntry,dobEntry,screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False,False)
    
    idLabel = Label(screen,text='Id',font=('arial',18,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry = Entry(screen,font=('arial',18,'italic bold'),width=25)
    idEntry.grid(row=0,column=1,padx=10,pady=15)
    
    nameLabel = Label(screen,text='Name',font=('arial',18,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry = Entry(screen,font=('arial',18,'italic bold'),width=25)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    
    deptLabel = Label(screen,text='Dept',font=('arial',18,'bold'))
    deptLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    deptEntry = Entry(screen,font=('arial',18,'italic bold'),width=25)
    deptEntry.grid(row=2,column=1,padx=10,pady=15)
    
    mobileLabel = Label(screen,text='Mobile',font=('arial',18,'bold'))
    mobileLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    mobileEntry = Entry(screen,font=('arial',18,'italic bold'),width=25)
    mobileEntry.grid(row=3,column=1,padx=10,pady=15)
    
    emailLabel = Label(screen,text='Email',font=('arial',18,'bold'))
    emailLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    emailEntry = Entry(screen,font=('arial',18,'italic bold'),width=25)
    emailEntry.grid(row=4,column=1,padx=10,pady=15)
    
    addressLabel = Label(screen,text='Address',font=('arial',18,'bold'))
    addressLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    addressEntry = Entry(screen,font=('arial',18,'italic bold'),width=25)
    addressEntry.grid(row=5,column=1,padx=10,pady=15)
    
    genderLabel = Label(screen,text='Gender',font=('arial',18,'bold'))
    genderLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    genderEntry = Entry(screen,font=('arial',18,'italic bold'),width=25)
    genderEntry.grid(row=6,column=1,padx=10,pady=15)
    
    dobLabel = Label(screen,text='D.O.B',font=('arial',18,'bold'))
    dobLabel.grid(row=7,column=0,padx=30,pady=15,sticky=W)
    dobEntry = Entry(screen,font=('arial',18,'italic bold'),width=25)
    dobEntry.grid(row=7,column=1,padx=10,pady=15)
    
    student_button = ttk.Button(screen,text = button_text, command = command)
    student_button.grid(row=8,columnspan=2,pady=15)
    
    if title == 'Update Student':
        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']
        #print(listdata)
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        deptEntry.insert(0, listdata[2])
        mobileEntry.insert(0, listdata[3])
        emailEntry.insert(0, listdata[4])
        addressEntry.insert(0, listdata[5])
        genderEntry.insert(0, listdata[6])
        dobEntry.insert(0, listdata[7])



    
def update_data():
    query = 'update student set name=%s, dept=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(), deptEntry.get(), mobileEntry.get(),
                            emailEntry.get(), addressEntry.get(), genderEntry.get(),
                            dobEntry.get(), date, currenttime, idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()
    



def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)



def delete_student():
    indexing = studentTable.focus()
    #print(indexing)
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)



def search_data():
    query = 'select * from student where id=%s or name=%s or dept=%s or address=%s or gender=%s'
    mycursor.execute(query,(idEntry.get(), nameEntry.get(), deptEntry.get(), addressEntry.get(),genderEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)
        
    

def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or deptEntry.get()=='' or mobileEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','All Feilds are required!',parent = screen)
        
    else:
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(), nameEntry.get(), deptEntry.get(),
                                    mobileEntry.get(), emailEntry.get(), addressEntry.get(),
                                    genderEntry.get(), dobEntry.get(), date, currenttime))
            con.commit()
            
            result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent = screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                deptEntry.delete(0,END)
                mobileEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return
            
            
        query = 'select * from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        
        for data in fetched_data:
            datalist = list(data)
            studentTable.insert('', END, values=datalist)
            


def connect_database():
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host='localhost',
                                  user='root',password=passwordEntry.get())
            mycursor = con.cursor()
            
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
            
        try:
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query = 'create table student(id int not null primary key, name varchar(30),dept varchar(30), mobile varchar(20), email varchar(45), address varchar(45),gender varchar(10), dob varchar(20), date varchar(20), time varchar(20))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        
        messagebox.showinfo('Success','Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportdataButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        
        
    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+650+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)
    
    hostnameLabel = Label(connectWindow,text='Host Name',font=('arial',18,'bold'))
    hostnameLabel.grid(row=0, column=0 ,padx=20)
    
    hostEntry = Entry(connectWindow,font=('calibri',15,'bold'),bd=2)
    hostEntry.grid(row=0, column=1, pady=20, padx=40)
    
    usernameLabel = Label(connectWindow,text='User Name',font=('arial',18,'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)
    
    usernameEntry = Entry(connectWindow,font=('calibri',15,'bold'),bd=2)
    usernameEntry.grid(row=1, column=1, pady=20, padx=40)
    
    passwordLabel = Label(connectWindow,text='Password',font=('arial',18,'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)
    
    passwordEntry = Entry(connectWindow,font=('calibri',15,'bold'),bd=2)
    passwordEntry.grid(row=2, column=1, pady=20, padx=40)
    
    connectButton = ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)


count = 0
text = ''

def clock():
    global date,currenttime
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)

    
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text = text + s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(200, slider)



# GUI Part

root = ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('radiance')

root.resizable(0,0)
root.geometry('1174x700+20+10')
root.title('Student Management System')

datetimeLabel = Label(root,text='Hello',font=('adabi',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s = 'Student Management System'
sliderLabel = Label(root,text=s,font=('arial',25,'italic bold'),width=34)
sliderLabel.place(x=250,y=5)
slider()

connectButton = ttk.Button(root,text='Connect Database',command=connect_database)
connectButton.place(x=1000,y=5)

leftFrame = Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_img = PhotoImage(file='student.png')
logo_Label = Label(leftFrame,image=logo_img)
logo_Label.grid(row=0,column=0)

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED,
                              command = lambda :toplevel_data('Add Student','ADD',add_data))
addstudentButton.grid(row=1,column=0,pady=20)


searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED,
                                 command = lambda :toplevel_data('Search Student','SEARCH',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)


deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=25,state=DISABLED,
                                 command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)


updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=25, state=DISABLED,
                                 command = lambda :toplevel_data('Update Student','UPDATE',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)


showstudentButton = ttk.Button(leftFrame, text='Show Student', width=25,state=DISABLED,
                               command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)


exportdataButton = ttk.Button(leftFrame, text='Export Data', width=25, state=DISABLED, 
                              command=export_data)
exportdataButton.grid(row=6,column=0,pady=20)


exitButton = ttk.Button(leftFrame, text='Exit', width=25, command = iexit)
exitButton.grid(row=7,column=0,pady=20)


rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollbarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbarY = Scrollbar(rightFrame,orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame,columns=('Id','Name','Department','Mobile No.','Email',
                                                'Address','Gender','D.O.B',
                                                'Added Date','Added Time'),
                            xscrollcommand=scrollbarX.set,
                            yscrollcommand=scrollbarY.set)

scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Department', text='Department')
studentTable.heading('Mobile No.', text='Mobile No.')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')

studentTable.column('Id', width=70,anchor=CENTER)
studentTable.column('Name', width=150,anchor=CENTER)
studentTable.column('Department', width=200,anchor=CENTER)
studentTable.column('Mobile No.', width=200,anchor=CENTER)
studentTable.column('Email', width=250,anchor=CENTER)
studentTable.column('Address', width=200,anchor=CENTER)
studentTable.column('Gender', width=150,anchor=CENTER)
studentTable.column('D.O.B', width=200,anchor=CENTER)
studentTable.column('Added Date', width=200,anchor=CENTER)
studentTable.column('Added Time', width=200,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview', rowheight=30,font=('arial',12,'bold'),foreground='black')
style.configure('Treeview.Heading', font=('arial',14,'bold'),foreground='black')


studentTable.config(show='headings')


root.mainloop()


