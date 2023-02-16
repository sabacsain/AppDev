from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
import register_form, login_form, home, get_started, \
        input_sleep, update, result_good, edit_account, \
        weekly_input, monthly_input, about, weekly_graph, \
        monthly_graph, contact, result_bad, all_records, main
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
def callMain():
    main.start()

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
    sleep = sleepTracker(sleep_value, phone)
    if sleep == 'enough': result_good.start(window, frame, phone)
    elif sleep == 'not enough': result_bad.start(window, frame, phone)
    
def callEditAccount(window, frame, phone):
    edit_account.start(window, frame, phone)

def callWeeklyInput(window, frame, phone):
    weekly_input.start(window, frame, phone)

def callWeeklyGraph(window, frame, month, year, phone):
    weekly_graph.start(window, frame, month, year, phone)

def callMonthlyInput(window, frame, phone):
    monthly_input.start(window, frame, phone)

def callMonthlyGraph(window, frame, year, phone):
    monthly_graph.start(window, frame, year, phone)

def callAbout(window, frame, phone):
    about.start(window, frame, phone)

def callContact(window, frame, phone):
    contact.start(window, frame, phone)

def callView(window, frame, phone):
    all_records.start(window, frame, phone)

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

            #CREATE sleep_tracker TABLE IF DATABASE DOESNT EXIST
            c.execute("""CREATE TABLE IF NOT EXISTS sleep_tracker (
                PHONE text,
                SLEEP FLOAT,
                DATE text,
                WEEK INT,
                DAY INT
                )""")


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

            #CREATE sleep_tracker TABLE IF DATABASE DOESNT EXIST
            c.execute("""CREATE TABLE IF NOT EXISTS sleep_tracker (
                PHONE text,
                SLEEP FLOAT,
                DATE text,
                WEEK INT,
                DAY INT
                )""")

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
        return False
    
    try:
        sleep_value = float(sleep_value)
    except Exception:
        messagebox.showerror("Error","Invalid Input!")
        return False
    
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
            c.execute("UPDATE sleep_tracker SET SLEEP = ?, WEEK = ?, DAY = ? WHERE DATE = ? AND PHONE = ?", [sleep_value, week, DAY, current_date, phone])
            conn.commit()
            conn.close()
    except Exception as error:
        messagebox.showerror("Failed to save sleep value",f'Error: {error}')
        return False
    
    # Condition going to Result Good or Bad Frame
    if sleep_value >=  7: return 'enough'
    else: return 'not enough'

def delete_account_and_records(window, frame, phone):
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
    conn.commit()
    conn.close()
    messagebox.showinfo("Notice!", "Account is Deleted!")
    # callRegister(window, frame)
    window.destroy()
    callMain()
    return

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


def update_sleep(window, frame, phone, hours, cal):
    hours = hours.get()
    try:
        hours = float(hours)
    except:
        messagebox.showerror("Error", 'Invalid Input')
        return

    current_date = datetime.datetime.now()
    DAY = 0
    date = datetime.datetime.strptime(cal.get_date(), f"%m/%d/%y").date()
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
        
    # to get if current_date's day is day 1 or day 2 or day 3... or day 7 of the weeek 
    if date.day % 7 == 0:
        DAY = 7
    else:
        DAY = date.day % 7

    # to get if day is in the first, second, third, or fourth week
    if date.day <= 7 :
        week = 1
    elif date.day <= 14:
        week = 2
    elif date.day <= 21:
        week = 3
    elif date.day <= 28:
        week = 4
    else:
        week = 5

    current_date = current_date.strftime("%Y-%m-%d")
    conn = sql.connect('sleep_database.db')
    c = conn.cursor()
    #check if date is existing
    c.execute("SELECT * FROM sleep_tracker WHERE PHONE = ? AND DATE = ?",[phone, date])
    new = c.fetchone()
    if (new == None):
        c.execute("INSERT into sleep_tracker VALUES (:PHONE, :SLEEP, :DATE, :WEEK, :DAY)",
                  {
                    "PHONE": phone,
                    "SLEEP": hours,
                    "DATE": date,
                    "WEEK": week,
                    "DAY" : DAY
                  }
        )
        conn.commit()
        conn.close()
    #UPDATE the hours 
    else:
        c.execute("UPDATE sleep_tracker SET SLEEP = ?, WEEK = ?, DAY = ? WHERE DATE = ? AND PHONE = ?", [hours, week, DAY, current_date, phone])
        conn.commit()
        conn.close()
    
    messagebox.showinfo("Updated","Press ANY Key to Continue.")
    callHome(window, frame, phone)

def update_profile(window, frame, phone, fname, lname, phone_number, birthday, password, male_button, female_button):
    fname = fname.get()
    lname = lname.get()
    phone_number = phone_number.get()
    birthday = birthday.get()
    password = password.get().encode()
    if not password: messagebox.showwarning('Password Error', 'Please input a password!'); return
    password = hashlib.md5(password).hexdigest()

    if (male_button["state"]==DISABLED): sex = "MALE"
    else: sex = "FEMALE"
    conn = sqlite3.connect('sleep_database.db')
    c = conn.cursor()

    #checks if new phone number entered is already taken
    c.execute("SELECT * FROM accounts WHERE( PHONE = ? AND PHONE != ?)", (phone_number, phone))
    result = c.fetchall()
    if (result):
        print(result)
        messagebox.showerror("Error","Entered phone number is already taken")
        conn.close()
        return phone

    else:
        c.execute('UPDATE accounts SET FNAME = ?, LNAME = ?, PHONE = ?, BIRTHDAY = ?, PASSWORD = ?, SEX = ? WHERE phone = ?', (fname, lname, phone_number, birthday, password, sex, phone,))
        c.execute('UPDATE sleep_tracker SET PHONE = ? WHERE phone = ?', (phone_number, phone,))
        
        try:
            messagebox.showinfo("Account Updated", "Thank you for updating your account!")
            conn.commit()
            conn.close()
            phone = phone_number
            callHome(window, frame, phone)

            return phone
            callHome(window, frame, phone_number)
        except:
            conn.close()
            messagebox.showerror("Error","Database Error")
            return phone
        
def create_weekly_df(window, month, year, phone):
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
    
    # these will be used for computing ave
    count = 0 
    total = 0.00

    # SQL Connection
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

    # Create the Weekly table if it doesn't exist
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
    # Generation of sleep_table  (treeview)

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

    #returns sleep_records dataframe to weekly_graph.py
    return sleep_records


# Create a bar graph using matplotlib
def weekly_bar_graph(sleep_records):
    plt.close()
    fig = plt.figure(figsize=(4.5, 4.5))
    ax = fig.add_subplot(1,1,1)
    ax.bar(sleep_records["Week"], sleep_records["Ave"])
    ax.set_title("Bar Graph")
    ax.set_xlabel("Weeks")
    ax.set_ylabel("Average Sleep")

    # canvas = FigureCanvasTkAgg(fig, window)
    plt.show()
    # canvas.get_tk_widget().grid_forget()
    # canvas.get_tk_widget().grid(row=0, column=1, padx=30, pady=0)

    return fig

# Create a line graph using matplotlib
def weekly_line_graph(sleep_records):
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


def create_monthly_df(window, year, phone):

    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    months_list = []

    # SQL Connection
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "sleep_database.db")

    conn = sql.connect(db_path)
    c = conn.cursor()

    for i in months:
        c.execute("SELECT AVG(SLEEP) FROM sleep_tracker WHERE PHONE = ? AND strftime('%Y', DATE) = ? AND strftime('%m', DATE) = ? ", [phone, year, i])
        results = c.fetchone()

        if results == None:
            months_list.append('-')
        else:
            months_list.append(results)

    # Drop table if it exists
    drop_table = ("DROP TABLE IF EXISTS Monthly")
    c.execute(drop_table)

    # Create the Monthly table if it doesn't exist
    create_table = """ CREATE table Monthly (
                        AVE text, 
                        JAN float, 
                        FEB float, 
                        MAR float, 
                        APR float, 
                        MAY float, 
                        JUN float, 
                        JUL float, 
                        AUG float, 
                        SEPT float, 
                        OCT float, 
                        NOV float, 
                        DEC float);"""
    c.execute(create_table)
    conn.commit()


    #convert months_list tuple to list
    months_list = list(months_list)

    #converts each tuple in the months_list list to list 
    for i in range(0,12):
        months_list[i] = list(months_list[i])
        if months_list[i][0] == None:
            months_list[i][0] = 0.00  # assign 0.00 if ave sleep hours for the month is null
    
    c.execute("INSERT into Monthly (AVE, JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEPT, OCT, NOV, DEC) values (?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                "AVE",
                "{:.2f}" .format(months_list[0][0]),
                "{:.2f}" .format(months_list[1][0]),
                "{:.2f}" .format(months_list[2][0]),
                "{:.2f}" .format(months_list[3][0]),
                "{:.2f}" .format(months_list[4][0]),
                "{:.2f}" .format(months_list[5][0]),
                "{:.2f}" .format(months_list[6][0]),
                "{:.2f}" .format(months_list[7][0]),
                "{:.2f}" .format(months_list[8][0]),
                "{:.2f}" .format(months_list[9][0]),
                "{:.2f}" .format(months_list[10][0]),
                "{:.2f}" .format(months_list[11][0]),      
                ))
    conn.commit()
              
    #####################################################################
    # Generation of sleep_table  (treeview)
    sleep_records = pd.read_sql_query("SELECT * FROM Monthly",conn)
    conn.commit()
    conn.close()

    # print(sleep_records)
    # print(type(sleep_records))
    # print(sleep_records["JAN"])
    # print(type(sleep_records["JAN"]))
    # exit(0)
    # Create the treeview widget
    sleep_table = ttk.Treeview(window, columns=('Ave', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEPT', 'OCT', 'NOV', 'DEC'), show='headings')
    sleep_table.heading('Ave', text="")
    sleep_table.heading('JAN', text="JAN")
    sleep_table.heading('FEB', text="FEB")
    sleep_table.heading('MAR', text="MAR")
    sleep_table.heading('APR', text="APR")
    sleep_table.heading('MAY', text="MAY")
    sleep_table.heading('JUN', text="JUN")
    sleep_table.heading('JUL', text="JUL")
    sleep_table.heading('AUG', text="AUG")
    sleep_table.heading('SEPT', text="SEPT")
    sleep_table.heading('OCT', text="OCT")
    sleep_table.heading('NOV', text="NOV")
    sleep_table.heading('DEC', text="DEC")

    # Set Initial Width of Columns
    for col in sleep_table['columns']:
        sleep_table.column(col, width=75)
    
    # Populate the treeview with data from the dataframe
    for index, row in sleep_records.iterrows():
        sleep_table.insert(parent='',index='end', values=list(row))     

    # Show the Sleep Table
    sleep_table.grid(row=0, column=0, padx=128, pady=350)

    # Returns sleep_records dataframe to monthly_graph.py
    return sleep_records

# Create a line graph using matplotlib
def monthly_line_graph(sleep_records):
        plt.close()
        fig, ax = plt.subplots(figsize=(7,7))
        ax.plot(["JAN","FEB","MAR","APR","MAY","JUN","JUL",'AUG',"SEPT","OCT","NOV","DEC"],
                [sleep_records["JAN"],
                sleep_records["FEB"],
                sleep_records["MAR"],
                sleep_records["APR"],
                sleep_records["MAY"],
                sleep_records["JUN"],
                sleep_records["JUL"],
                sleep_records["AUG"],
                sleep_records["SEPT"],
                sleep_records["OCT"],
                sleep_records["NOV"],
                sleep_records["DEC"]])
        ax.set_title("LINE GRAPH")
        ax.set_xlabel("MONTHS")
        ax.set_ylabel("AVERAGE SLEEP")
        plt.show()

        # canvas = FigureCanvasTkAgg(fig, window)
        # canvas.get_tk_widget().grid_forget()
        # canvas.get_tk_widget().grid(row=0, column=1, padx=30, pady=0)

        return fig


# Create a bar graph using matplotlib
def monthly_bar_graph(sleep_records):
    plt.close()
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(1,1,1)
    ax.bar(["JAN","FEB","MAR","APR","MAY","JUN","JUL",'AUG',"SEPT","OCT","NOV","DEC"],
            [sleep_records.loc[0, "JAN"],
            sleep_records.loc[0, "FEB"],
            sleep_records.loc[0, "MAR"],
            sleep_records.loc[0, "APR"],
            sleep_records.loc[0, "MAY"],
            sleep_records.loc[0, "JUN"],
            sleep_records.loc[0, "JUL"],
            sleep_records.loc[0, "AUG"],
            sleep_records.loc[0, "SEPT"],
            sleep_records.loc[0, "OCT"],
            sleep_records.loc[0, "NOV"],
            sleep_records.loc[0, "DEC"],
        ])
    ax.set_title("BAR GRAPH")
    ax.set_xlabel("MONTHS")
    ax.set_ylabel("AVERAGE SLEEP")

    plt.show()
    # canvas.get_tk_widget().grid_forget()
    # canvas.get_tk_widget().grid(row=0, column=1, padx=30, pady=0)

    return fig
