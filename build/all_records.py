import sqlite3 as sql
import tkinter as tk
import pandas as pd
import os
from tkinter import ttk
import datetime
import functions

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame15")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def start(window, frame, phone):
    window = window
    frame = frame


    canvas = Canvas(
        window,
        bg = "#DEEAEE",
        height = 838,
        width = 1244,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        629.0,
        76.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    menu_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callHome(window, frame, phone),
        relief="flat"
    )
    menu_button.place(
        x=228.0,
        y=66.0,
        width=93.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    about_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callAbout(window, frame, phone),
        relief="flat"
    )
    about_button.place(
        x=361.0,
        y=69.0,
        width=106.0,
        height=34.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    contact_button = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callContact(window, frame, phone),
        relief="flat"
    )
    contact_button.place(
        x=508.0,
        y=69.0,
        width=131.0,
        height=37.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        140.0,
        77.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        229.0,
        266.0,
        image=image_image_3
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        625.0,
        600.0,
        image=image_image_6
    )
    
    def show_records(phone, month, year):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "sleep_database.db")

        conn = sql.connect(db_path)

        # sleep_records = pd.read_sql_query("SELECT DATE, SLEEP FROM sleep_tracker WHERE PHONE = ?",conn, params=(phone,))
        sleep_records = pd.read_sql_query("SELECT DATE, SLEEP FROM sleep_tracker WHERE PHONE = ? AND strftime('%m', DATE) = ? \
                                             AND strftime('%Y', DATE) = ? ORDER BY DATE",conn, params=(phone,month, year))
        conn.close()
        # print(sleep_records)

        # Create the treeview widget
        sleep_table = ttk.Treeview(window, columns=('DATE', 'SLEEP_HOURS'), show='headings', height=10)
        sleep_table.heading('DATE', text="DATE")
        sleep_table.heading('SLEEP_HOURS', text="SLEEP HOURS")


        # Set Initial Width of Columns
        for col in sleep_table['columns']:
            sleep_table.column(col, width=160, anchor='center')

        for item in sleep_table.get_children():
            sleep_table.delete(item)

        sleep_table.tag_configure("oddrow", background="lightblue")

        # Populate the treeview with data from the dataframe
        for index, row in sleep_records.iterrows():
            if index % 2 == 0: sleep_table.insert(parent='',index='end', values=list(row))
            else: sleep_table.insert(parent='',index='end', values=list(row), tags = 'oddrow')

        # Show the Sleep Table
        sleep_table.place(anchor='center', relx=.5, rely=.5)


    def click(event):
        show_records(phone, cbx_month.get(), cbx_year.get())


    cbx_year_options = [str(i) for i in range(2010,datetime.datetime.today().year + 1)]
    cbx_year  = ttk.Combobox(values=cbx_year_options)
    cbx_year.current(cbx_year_options.index(str(datetime.datetime.today().year)))
    cbx_year.bind("<<ComboboxSelected>>", click)
    cbx_year.place(
        x=648.0,
        y=650.0,
        width=182,
        height=56,
        )
    cbx_year.config(
        font=("Inter ExtraLight", 25 * -1),
        justify="center",
        state="readonly"
        )

    cbx_month_options = ["01", "02", "03","04","05","06","07","08","09","10","11","12"]
    cbx_month  = ttk.Combobox(values=cbx_month_options)
    cbx_month.current(cbx_month_options.index(datetime.datetime.today().strftime('%m')))
    cbx_month.bind("<<ComboboxSelected>>", click)
    cbx_month.place(
        x=430.0,
        y=650.0,
        width=184,
        height=56,
        )
    cbx_month.config(
        font=("Inter ExtraLight", 25 * -1),
        justify="center",
        state="readonly"
        )



    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "white", background= "#DEEAEE")

    # # in case the user doesn't click the comboboxes
    click("<<ComboboxSelected>>")
    window.resizable(False, False)
    window.mainloop()
    
if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window, phone='123')



