from tkinter import *
from tkinter import messagebox
import sqlite3
import gui2, gui3, gui4, gui5, gui6, gui7, gui8
import datetime
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
    
def callGui4(window, frame, phone):
    gui4.start(window, frame, phone)

def callGui5(window, frame, phone):
    gui5.start(window, frame, phone)

def callGui6(window, frame, sleep_value, phone):
    sleepTracker(sleep_value, phone)
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
            
            #CREATE TABLE IF DATABASE DOESNT EXIST
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

                callGui4(window,frame, phone)

        except Exception as error:
            messagebox.showerror("Registration Unsuccessful",f'Error: {error}')
            return str(error)


def login(window,frame,phone_entry,password_entry):
    phone = phone_entry.get()
    password = password_entry.get()

    if len(phone)==0 or len(password)==0:
        messagebox.showerror("Error","Please satisfy all the fields")
    
    else:
        try:
            conn = sqlite3.connect('sleep_database.db')
            c = conn.cursor()

            #CREATE TABLE IF DATABASE DOESNT EXIST
            c.execute("""CREATE TABLE IF NOT EXISTS accounts (
                FNAME text,
                LNAME text,
                SEX text,
                PHONE text,
                BIRTHDAY text,
                PASSWORD text )""")
            conn.commit()

            #check if phone number and password are correct (in the database)
            c.execute("SELECT * FROM accounts where (PHONE=? AND PASSWORD=?)",[phone,password])
            account = c.fetchone()
            if(account==None):
                messagebox.showerror("Error", "Login Failed. Invalid phone number/password was entered.")
                conn.commit()
                conn.close()
            
            else:
                messagebox.showinfo("Login", "Login Successful!")
                conn.commit()
                conn.close()
                callGui4(window, frame, phone)
    
        except Exception as error:
            messagebox.showerror("Login Unsuccessful",f'Error: {error}')
            return str(error)

def sleepTracker(sleep, phone):
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d")
    sleep_value = sleep.get()

    if len(sleep_value) == 0:
        messagebox.showerror("Error","Please satisfy all the fields")
    else:
        try:
            conn = sqlite3.connect('sleep_database.db')
            c = conn.cursor()

            #CREATE TABLE IF DATABASE DOESNT EXIST
            c.execute("""CREATE TABLE IF NOT EXISTS sleep_tracker (
                PHONE text,
                SLEEP FLOAT,
                DATE text)""")
            conn.commit()
            #check if phone number (in the database)
            c.execute("SELECT * FROM sleep_tracker where (PHONE=? AND DATE=?)",[phone, current_date])
            user_sleep = c.fetchone()

            if(user_sleep==None):
                c.execute("INSERT into sleep_tracker VALUES (:PHONE, :SLEEP, :DATE)",
                    {
                        "PHONE": phone,
                        "SLEEP": sleep_value,
                        "DATE": current_date
                    }
                )
                conn.commit()
                conn.close()
            else:
                c.execute("UPDATE sleep_tracker SET SLEEP = ? WHERE DATE = ? AND PHONE = ?", [sleep_value, current_date, phone])
                conn.commit()
                conn.close()
        except Exception as error:
            messagebox.showerror("Failed to save sleep value",f'Error: {error}')
            return str(error)
       
    return
