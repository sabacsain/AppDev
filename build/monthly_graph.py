from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions
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


def start(window, frame, year, phone):
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

    #creates dataframe
    sleep_records = functions.create_monthly_df(window, year, phone)

    line_button_image = PhotoImage(
        file=relative_to_assets("button_4.png"))
    line_button = Button(
        image=line_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.monthly_line_graph(sleep_records),
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
        command=lambda: functions.monthly_bar_graph(sleep_records),
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
