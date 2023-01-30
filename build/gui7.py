
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/media/sendoff/sendoff HDD/CS/THIRD YEAR/FIRST SEM/AppDev/Panda/figma/Tkinter-Designer/build/assets/frame7")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1247x845")
window.configure(bg = "#E2EAFC")


canvas = Canvas(
    window,
    bg = "#E2EAFC",
    height = 845,
    width = 1247,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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
    y=71.0,
    width=72.0,
    height=29.0
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
    x=359.0,
    y=71.0,
    width=87.0,
    height=29.0
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
    x=503.0,
    y=71.0,
    width=120.0,
    height=29.0
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
    x=41.0,
    y=409.0,
    width=212.0,
    height=72.0
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
    x=106.0,
    y=256.0,
    width=212.0,
    height=72.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=446.0,
    y=254.0,
    width=212.0,
    height=72.0
)

canvas.create_rectangle(
    41.0,
    36.0,
    163.0,
    134.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    41.0,
    164.0,
    anchor="nw",
    text="Enter the starting and ending dates.",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    318.0,
    250.0,
    anchor="nw",
    text="to",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
