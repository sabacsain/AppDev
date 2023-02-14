
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame11")


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

    canvas.create_text(
        178.0,
        247.0,
        anchor="nw",
        text="About here....................................",
        fill="#000000",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_text(
        111.0,
        734.0,
        anchor="nw",
        text="Bacsain,\nShan Allen",
        fill="#000000",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_text(
        1007.0,
        734.0,
        anchor="nw",
        text="Bacsain,\nShan Allen",
        fill="#000000",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_text(
        335.0,
        728.0,
        anchor="nw",
        text="Bacsain,\nShan Allen",
        fill="#000000",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_text(
        559.0,
        728.0,
        anchor="nw",
        text="Bacsain,\nShan Allen",
        fill="#000000",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_text(
        783.0,
        734.0,
        anchor="nw",
        text="Bacsain,\nShan Allen",
        fill="#000000",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_text(
        377.0,
        186.0,
        anchor="nw",
        text="Lalagay ba tayo about us or about app lang?",
        fill="#000000",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_rectangle(
        73.0,
        548.0,
        275.0,
        718.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        297.0,
        548.0,
        499.0,
        718.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        521.0,
        548.0,
        723.0,
        718.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        745.0,
        548.0,
        947.0,
        718.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        969.0,
        548.0,
        1171.0,
        718.0,
        fill="#D9D9D9",
        outline="")
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window)