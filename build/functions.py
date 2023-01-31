from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import gui2, gui3, gui4, gui5, gui6, gui7, gui8
#  ,,, gui9

def display(entry_1, entry_2):
    try:
        name = entry_1.get()
        age = entry_2.get()
        display = f'The name is {name} and you are {age}'
        return display
    except Exception as error:
        print(f'Error: {error}')
        return str(error)

def callGui2(window, frame):
    gui2.start(window, frame)

def callGui3(window, frame):
    gui3.start(window, frame)
    
def callGui4(window, frame):
    gui4.start(window, frame)

def callGui5(window, frame):
    gui5.start(window, frame)

def callGui6(window, frame):
    gui6.start(window, frame)

def callGui7(window, frame):
    gui7.start(window, frame)

def callGui8(window, frame):
    gui8.start(window, frame)

# gui8.py
def disable_radioBtn(button1,button2):
    button1["state"] = DISABLED
    button2["state"] = NORMAL

def register(fname_entry,phone_entry,password_entry,birthday_entry,lname_entry,male_btn,female_btn):
    # print(fname_entry.get('1.0',END).upper())
    # print(phone_entry.get('1.0',END))
    # print(password_entry.get('1.0',END))
    # print(birthday_entry.get('1.0',END))
    # print(lname_entry.get('1.0',END))
    # print(male_btn["state"]==DISABLED)
    # print(female_btn["state"]==DISABLED)

    fname = fname_entry.get('1.0',END).upper()
    lname = lname_entry.get('1.0',END).upper()
    phone = phone_entry.get('1.0',END)
    password = password_entry.get('1.0',END)
    birthday = birthday_entry.get('1.0',END)
    
    if (male_btn["state"]==DISABLED):
        sex = "MALE"
    else:
        sex = "FEMALE"

    if len(fname)==1 or len(lname)==1 or len(phone)==1 or len(password)==1 or len(birthday)==1 or (male_btn["state"]==NORMAL and female_btn["state"]==NORMAL) :
        messagebox.showerror("Error", "Please satisfy all the fields")
    else: 
        conn = sqlite3.connect('sleep_database.db')
        c = conn.cursor()

        #CREATE TABLE IF DATABASE DOESNT EXIT
        c.execute("""CREATE TABLE IF NOT EXISTS accounts (
            FNAME text,
            LNAME text,
            SEX text,
            PHONE text,
            BIRTHDAY text,
            PASSWORD text )""")
        conn.commit()
        
        #check if phone number is already taken
        c.execute("SELECT * FROM accounts where (PHONE=?)",[phone])
        accounts = c.fetchall()

        if(len(accounts)!=0):
            messagebox.showerror("Error","Entered phone number is already in the database. Try using another number or try logging in.")
            conn.commit()
            conn.close()
            return
        
        else:
            c.execute("INSERT into accounts VALUES (:FNAME, :LNAME, :SEX, :PHONE, :BIRTHDAY, :PASSWORD)",
                {
                "FNAME": fname,
                "LNAME": lname,
                "SEX": sex,
                "PHONE": phone,
                "BIRTHDAY": birthday,
                "PASSWORD": password
                }
            )
            messagebox.showinfo("Registration","Congratulations! You have successfully signed up! wiw")
            conn.commit()

            #this is to see if record has been added to the database. delete laturrr
            c.execute("SELECT * FROM accounts")
            accounts = c.fetchall()
            print(accounts)

            conn.commit()
            conn.close()


            return

def login():
    return
