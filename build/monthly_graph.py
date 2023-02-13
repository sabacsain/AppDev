
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import sqlite3 as sql
import tkinter as tk
import pandas as pd
import os
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame13")


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
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=228.0,
        y=66.0,
        width=93.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=361.0,
        y=69.0,
        width=106.0,
        height=34.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
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

    line_button_image = PhotoImage(
        file=relative_to_assets("button_4.png"))
    line_button = Button(
        image=line_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: line_graph(),
        relief="raised"
    )
    line_button.place(
        x=330.0,
        y=631.0,
        width=270.0384521484375,
        height=65.0
    )

    bar_button_image = PhotoImage(
        file=relative_to_assets("button_5.png"))
    bar_button = Button(
        image=bar_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: bar_graph(),
        relief="raised"
    )
    bar_button.place(
        x=615.0,
        y=631.0,
        width=270.03857421875,
        height=65.0
    )

    # Save Button
    # button_image_6 = PhotoImage(
    #     file=relative_to_assets("button_6.png"))
    # save_button = Button(
    #     image=button_image_6,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_6 clicked"),
    #     relief="flat"
    # )
    # save_button.place(
    #     x=470.0,
    #     y=715.0,
    #     width=270.0384521484375,
    #     height=65.0
    # )

    image_image_3 = PhotoImage(
        file=relative_to_assets("month.png"))
    image_3 = canvas.create_image(
        204.0,
        242.0,
        image=image_image_3
    )


#####################################################################
# User's Input starts here

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "sleep_database.db")

    #shan's code
    # SQL Connection
    conn = sql.connect(db_path)

    conn = sql.connect('sleep_database.db')
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

    # Create a bar graph using matplotlib
    def bar_graph():
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

    # Create a line graph using matplotlib
    def line_graph():
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

    # Save the figure
    # def save():
    #     file_path = filedialog.asksaveasfilename(defaultextension='.svg')
    #     figure.savefig(file_path)


    hoverLine = PhotoImage(file=relative_to_assets("line.png"))
    hoverBar = PhotoImage(file=relative_to_assets("bar.png"))

    # Function to change image when mouse enters button
    def change_imageLine(event):
        line_button.config(image=hoverLine)
    def change_imageBar(event):
        bar_button.config(image=hoverBar)

    # Function to change back to original image when mouse leaves button
    def change_backLine(event):
        line_button.config(image=line_button_image)
    def change_backBar(event):
        bar_button.config(image=bar_button_image)

    # Bind the <Enter> event to change_image function
    line_button.bind("<Enter>", change_imageLine)
    bar_button.bind("<Enter>", change_imageBar)

    # Bind the <Leave> event to change_back function
    line_button.bind("<Leave>", change_backLine)
    bar_button.bind("<Leave>", change_backBar)

    # Start the Tkinter event loop
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window)
