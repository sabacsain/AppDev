
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/media/sendoff/sendoff HDD/CS/THIRD YEAR/FIRST SEM/AppDev/hannahGCardiB/build/assets/frame9")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1244x838")
window.configure(bg = "#DEEAEE")


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
    112.0,
    250.0,
    anchor="nw",
    text="Enter date range?",
    fill="#000000",
    font=("Inter Bold", 36 * -1)
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
    x=433.0,
    y=471.0,
    width=413.0,
    height=78.0
)

canvas.create_text(
    600.0,
    361.0,
    anchor="nw",
    text="YEAR",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_rectangle(
    872.0,
    188.0,
    1153.0,
    265.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    872.0,
    204.0,
    anchor="nw",
    text="MONTHLY",
    fill="#000000",
    font=("Inter SemiBold", 36 * -1)
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
    639.5,
    428.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=443.0,
    y=397.0,
    width=393.0,
    height=61.0
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
    x=795.0,
    y=416.0,
    width=43.0,
    height=26.0
)

canvas.create_text(
    589.0,
    405.0,
    anchor="nw",
    text="2022",
    fill="#665F5F",
    font=("Inter ExtraLight", 40 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    140.0,
    76.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
