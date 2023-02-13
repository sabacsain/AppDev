from tkinter import *
from tkinter import messagebox
import sqlite3
import register_form, login_form, home, get_started, \
        input_sleep, update, result, edit_account, \
        weekly_input, monthly_input, about
import datetime
import hashlib

def display(entry_1, entry_2):
    try:
        name = entry_1.get()
        age = entry_2.get()
        display = f'The name is {name} and you are {age}'
        return display
    except Exception as error:
        print(f'Error: {error}')
        return str(error)

# Calling all the GUI files
def callRegister(window, frame):
    register_form.start(window, frame)

def callLogin(window, frame):
    login_form.start(window, frame)

def callGetStarted(window, frame, phone):
    get_started.start(window, frame, phone)

def callHome(window, frame, phone):
    home.start(window, frame, phone)

def callInputSleep(window, frame, phone):
    input_sleep.start(window, frame, phone)

def callUpdate(window, frame):
    update.start(window, frame)

def callResult(window, frame, sleep_value, phone):
    sleepTracker(sleep_value, phone)
    result.start(window, frame)

def callEditAccount(window, frame, phone):
    edit_account.start(window, frame, phone)

def callWeeklyInput(window, frame):
    weekly_input.start(window, frame)

def callMonthlyInput(window, frame):
    monthly_input.start(window, frame)

def callAbout(window, frame):
    about.start(window, frame)

# def callGui6(window, frame, sleep_value, phone):
#     sleepTracker(sleep_value, phone)
#     gui6.start(window, frame)


def disable_radioBtn(button1,button2):
    button1["state"] = DISABLED
    button2["state"] = NORMAL

def register(window,frame,fname_entry,lname_entry,phone_entry,birthday_entry,password_entry,male_btn,female_btn):
    fname = fname_entry.get().upper()
    lname = lname_entry.get().upper()
    phone = phone_entry.get().upper()
    birthday = birthday_entry.get()
    password = password_entry.get().encode()
    password = hashlib.md5(password).hexdigest()

    if (male_btn["state"]==DISABLED): sex = "MALE"
    else: sex = "FEMALE"
    
    if len(fname)==0 or len(lname)==0 or len(phone)==0 or len(password)==0 or len(birthday)==0 or (male_btn["state"]==NORMAL and female_btn["state"]==NORMAL) :
        messagebox.showerror("Error", "Please satisfy all the fields")
        return

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

                callGetStarted(window, frame, phone)

        except Exception as error:
            messagebox.showerror("Registration Unsuccessful",f'Error: {error}')
            return str(error)


def login(window, frame, phone_entry, password_entry):
    phone = phone_entry.get()
    password = password_entry.get().encode()
    password = hashlib.md5(password).hexdigest()

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
                callGetStarted(window, frame, phone)
    
        except Exception as error:
            messagebox.showerror("Login Unsuccessful",f'Error: {error}')
            return str(error)

def sleepTracker(sleep, phone):
    current_date = datetime.datetime.now()
    DAY = 0

    # to get if current_date's day is day 1 or day 2 or day 3... or day 7 of the weeek 
    if current_date.day % 7 == 0:
        DAY = 7
    else:
        DAY = current_date.day % 7

    # to get if day is in the first, second, third, or fourth week
    if current_date.day <= 7 :
        week = 1
    elif current_date.day <= 14:
        week = 2
    elif current_date.day <= 21:
        week = 3
    elif current_date.day <= 28:
        week = 4
    else:
        week = 5

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
                DATE text,
                WEEK INT,
                DAY INT
                )""")
            conn.commit()
            #check if phone number (in the database)
            c.execute("SELECT * FROM sleep_tracker where (PHONE=? AND DATE=?)",[phone, current_date])
            user_sleep = c.fetchone()

            if(user_sleep==None):
                c.execute("INSERT into sleep_tracker VALUES (:PHONE, :SLEEP, :DATE, :WEEK, :DAY)",
                    {
                        "PHONE": phone,
                        "SLEEP": sleep_value,
                        "DATE": current_date,
                        "WEEK": week,
                        "DAY" : DAY
                    }
                )
                conn.commit()
                conn.close()
            else:
                c.execute("UPDATE sleep_tracker SET SLEEP = ?, WEEK = ?, DAY = ? WHERE DATE = ? AND PHONE = ?", [sleep_value, week, DAY ,current_date, phone])
                conn.commit()
                conn.close()
        except Exception as error:
            messagebox.showerror("Failed to save sleep value",f'Error: {error}')
            return str(error)
       
    return

def delete_account_and_records(window, phone):
    # Establish a connection to the database
    conn = sqlite3.connect('sleep_database.db')
    c = conn.cursor()

    # Delete the account record from the 'accounts' table
    delete_account_query = "DELETE FROM accounts WHERE phone = ?"
    c.execute(delete_account_query, (phone,))

    # Delete the records associated with the account from the 'records' table
    delete_records_query = "DELETE FROM sleep_tracker WHERE phone = ?"
    c.execute(delete_records_query, (phone,))

    # Commit the changes and close the connection
    messagebox.showinfo("Notice!", "Account is Deleted!")
    conn.commit()
    conn.close()
    window.destroy()

def get_user_profile(phone):
    conn = sqlite3.connect('sleep_database.db')
    c = conn.cursor()
    c.execute('select * from accounts WHERE phone = ?', (phone,))
    res = c.fetchall()
    try:
        conn.commit()
        conn.close()
        return res
    except:
        conn.close()
        print('database error')
        return False

# yung dito guys hindi pa tapos kasi wala pa siyang phone number, password and gender parang sira yung gui or baka sa'kin lang?

def update_profile(phone, fname, lname, phone_number, birthday, password, male_button, female_button):
    fname = fname.get()
    lname = lname.get()
    phone_number = phone_number.get()
    birthday = birthday.get()
    password = password.get().encode()
    password = hashlib.md5(password).hexdigest()
    if (male_button["state"]==DISABLED): sex = "MALE"
    else: sex = "FEMALE"
    conn = sqlite3.connect('sleep_database.db')
    c = conn.cursor()
    c.execute('UPDATE accounts SET FNAME = ?, LNAME = ?, PHONE = ?, BIRTHDAY = ?, PASSWORD = ?, SEX = ? WHERE phone = ?', (fname, lname, phone_number, birthday, password, sex, phone,))
    try:
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        print('database error')
        return False
