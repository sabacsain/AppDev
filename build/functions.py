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

def disable_radioBtn(button1,button2):
    button1["state"] = DISABLED
    button2["state"] = NORMAL

def register(window,frame,fname_entry,lname_entry,phone_entry,birthday_entry,password_entry,male_btn,female_btn):

    fname = fname_entry.get().upper()
    lname = lname_entry.get().upper()
    phone = phone_entry.get().upper()
    birthday = birthday_entry.get()
    password = password_entry.get()

    if (male_btn["state"]==DISABLED): sex = "MALE"
    else: sex = "FEMALE"
    
    if len(fname)==0 or len(lname)==0 or len(phone)==0 or len(password)==0 or len(birthday)==0 or (male_btn["state"]==NORMAL and female_btn["state"]==NORMAL) :
        messagebox.showerror("Error", "Please satisfy all the fields")
        return

    # print(fname,lname,phone,birthday,password,sex)
    else:
        try:
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
                messagebox.showerror("Error","Entered phone number is already taken. Try using another number or try logging in.")
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

                messagebox.showinfo("Registration","Congratulations! You have successfully registered!")
                conn.commit()

                #this is to see if record has been added to the database. delete laturrr
                c.execute("SELECT * FROM accounts")
                accounts = c.fetchall()
                print(accounts)

                conn.commit()
                conn.close()

                callGui4(window,frame)
                return
        
        except Exception as error:
            print(f'Error: {error}')
            return str(error)


def login():
    return
