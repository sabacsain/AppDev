
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame6")


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
    canvas.create_text(
        164.0,
        320.0,
        anchor="nw",
        text="how many hours did you sleep today?",
        fill="#000000",
        font=("Inter SemiBold", 36 * -1)
    )

    enter_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    enter_button = Button(
        image=enter_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callResult(window, frame, entry_1, phone),
        relief="flat"
    )
    enter_button.place(
        x=164.0,
        y=663.0,
        width=218.0,
        height=77.0
    )

    canvas.create_text(
        164.0,
        247.0,
        anchor="nw",
        text="[NAME],",
        fill="#54899E",
        font=("Inter Bold", 40 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        629.0,
        76.0,
        image=image_image_1
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
        x=228.0,
        y=66.0,
        width=93.0,
        height=40.0
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
        x=361.0,
        y=69.0,
        width=106.0,
        height=34.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=508.0,
        y=69.0,
        width=131.0,
        height=37.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=1023.0,
        y=72.0,
        width=136.0,
        height=39.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        431.5,
        470.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=174.0,
        y=445.0,
        width=515.0,
        height=49.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        140.0,
        76.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        966.0,
        659.0,
        image=image_image_3
    )


    hoverEnter = PhotoImage(file=relative_to_assets("enter.png"))

    # Function to change image when mouse enters button
    def change_imageGetStarted(event):
        enter_button.config(image=hoverEnter)

    # Function to change back to original image when mouse leaves button
    def change_backGetStarted(event):
        enter_button.config(image=enter_button_image)


    # Bind the <Enter> event to change_image function
    enter_button.bind("<Enter>", change_imageGetStarted)

    # Bind the <Leave> event to change_back function
    enter_button.bind("<Leave>", change_backGetStarted)

    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window)