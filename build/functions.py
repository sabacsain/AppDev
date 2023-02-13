from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
import register_form, login_form, home, get_started, \
        input_sleep, update, result, edit_account, \
        weekly_input, monthly_input, about, \
        weekly_graph, monthly_graph

import datetime
import hashlib
import os
import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

def callUpdate(window, frame, phone):
    update.start(window, frame, phone)

def callResult(window, frame, sleep_value, phone):
    sleepTracker(sleep_value, phone)
    result.start(window, frame, phone)

def callEditAccount(window, frame, phone):
    edit_account.start(window, frame, phone)

def callWeeklyInput(window, frame, phone):
    weekly_input.start(window, frame, phone)

def callWeeklyGraph(window, frame, month, year, phone):
    weekly_graph.start(window, frame, month, year, phone)

def callMonthlyInput(window, frame, phone):
    monthly_input.start(window, frame, phone)

def callMonthlyGraph(window, frame, phone):
    monthly_graph.start(window, frame, phone)

def callAbout(window, frame,phone):
    about.start(window, frame, phone)

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

def update_profile(phone, fname, lname, birthday):
    fname = fname.get()
    lname = lname.get()
    birthday = birthday.get()
    conn = sqlite3.connect('sleep_database.db')
    c = conn.cursor()
    c.execute('UPDATE accounts SET FNAME = ?, LNAME = ?, BIRTHDAY = ? WHERE phone = ?', (fname, lname, birthday, phone,))
    try:
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        print('database error')
        return False
    callHome(window, frame)


def create_weekly_df(window, month, year, phone):

    #####################################################################
    # User's Input starts here
    print("MONTH: ", month, "\nYEAR: ", year, "\nPHONE: ", phone)

    #list of weeks, and days
    weeks = [1,2,3,4,5]
    days = [1,2,3,4,5,6,7]

    week1 = []
    week2 = []
    week3 = []
    week4 = []
    week5 = []
    ave= []

    days_list = (week1,week2,week3,week4,week5)
    
    #these will be used for computing ave
    count = 0 
    total = 0.00

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "sleep_database.db")

    conn = sql.connect(db_path)
    c = conn.cursor()

    # gets all sleep hours per day per week
    for week in weeks:
        for day in days :
            c.execute("SELECT SLEEP FROM sleep_tracker WHERE PHONE = ? and strftime('%m', DATE) = ? and strftime('%Y', DATE) = ? and WEEK = ? and DAY = ?", [
                phone,
                month,
                year,
                week,
                day]
            )
            
            result = c.fetchone()
            if result == None:
                days_list[week-1].append(list('-'))
                
            else: days_list[week-1].append(list(result))

    # computes average sleep hours for each week
    for i in days_list: # i = week in bracket []
        for j in i:   # j is hours in bracket. ex: [1.2]
            for k in j:
                # print(k)  # K IS HOURS
                if type(k) == float:
                    total += k
                    count += 1
                else: continue
        try:
            ave.append("{:.2f}" .format(total/count))
        except:
            ave.append(0)
        total = 0.0
        count = 0.0  

    # Drop table if it exist
    drop_table = ("DROP TABLE IF EXISTS Weekly")
    c.execute(drop_table)
    conn.commit()

    # Create the table if it doesn't exist
    create_table = """ CREATE table Weekly (Week text, Day1 int, 
        Day2 int, Day3 int, Day4 int, Day5 int, Day6 int, Day7 int, Ave float);
        """
    c.execute(create_table)
    conn.commit()

    #TO STORE VALUES FROM sleep_tracker table to Weekly table ! ! ! ! !
    for i in range(5):
        c.execute('INSERT into Weekly(Week, Day1, Day2, Day3, Day4, Day5, Day6, Day7, Ave) values (?,?,?,?,?,?,?,?,?)',(
            i+1, 
            days_list[i][0][0],
            days_list[i][1][0],
            days_list[i][2][0],
            days_list[i][3][0],
            days_list[i][4][0],
            days_list[i][5][0],
            days_list[i][6][0],
            ave[i]))
        conn.commit()
        print("WEEK# : ", i+1, "\nDAY 1: ", days_list[i][0][0], "\nDAY 2: ", days_list[i][1][0], "\nDAY 3: ", days_list[i][2][0] , "\nDAY 4: ", days_list[i][3][0] 
        , "\nDAY 5: ", days_list[i][4][0] , "\nDAY 6: ", days_list[i][5][0], "\nDAY 7: ", days_list[i][6][0])

 
    #####################################################################
    # Generation of sleep_table 

    #shan's code
    # SQL Connection
    # conn = sql.connect(db_path)
    sleep_records = pd.read_sql_query("SELECT * FROM Weekly",conn)
    conn.commit()
    conn.close()

    print(sleep_records)

    # Create the treeview widget
    sleep_table = ttk.Treeview(window, columns=('Week', 'Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7', 'Ave'), show='headings')
    sleep_table.heading('Week', text="Week")
    sleep_table.heading('Day1', text="Day 1")
    sleep_table.heading('Day2', text="Day 2")
    sleep_table.heading('Day3', text="Day 3")
    sleep_table.heading('Day4', text="Day 4")
    sleep_table.heading('Day5', text="Day 5")
    sleep_table.heading('Day6', text="Day 6")
    sleep_table.heading('Day7', text="Day 7")
    sleep_table.heading('Ave', text="Avg")


    # Set Initial Width of Columns
    for col in sleep_table['columns']:
        sleep_table.column(col, width=80)

    sleep_table.tag_configure("oddrow", background="lightblue")

    # Populate the treeview with data from the dataframe
    for index, row in sleep_records.iterrows():
        if index % 2 == 0: sleep_table.insert(parent='',index='end', values=list(row))
        else: sleep_table.insert(parent='',index='end', values=list(row), tags = 'oddrow')

    # Show the Sleep Table
    sleep_table.grid(row=0, column=0, padx=270, pady=350)

    
    return sleep_records


# Create a bar graph using matplotlib
def bar_graph(sleep_records, window):
        plt.close()
        fig = plt.figure(figsize=(4.5, 4.5))
        ax = fig.add_subplot(1,1,1)
        ax.bar(sleep_records["Week"], sleep_records["Ave"])
        ax.set_title("Bar Graph")
        ax.set_xlabel("Weeks")
        ax.set_ylabel("Average Sleep")

        canvas = FigureCanvasTkAgg(fig, window)
        plt.show()
        # canvas.get_tk_widget().grid_forget()
        # canvas.get_tk_widget().grid(row=0, column=1, padx=30, pady=0)

        return fig

# Create a line graph using matplotlib
def line_graph(sleep_records, window):
    plt.close()
    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    ax.plot(sleep_records["Week"], sleep_records["Ave"])
    ax.set_title("Line Graph")
    ax.set_xlabel("Weeks")
    ax.set_ylabel("Average Sleep")
    plt.show()

    # canvas = FigureCanvasTkAgg(fig, window)
    # canvas.get_tk_widget().grid_forget()
    # canvas.get_tk_widget().grid(row=0, column=1, padx=30, pady=0)

    return fig
