
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/media/sendoff/sendoff HDD/CS/THIRD YEAR/FIRST SEM/AppDev/shiela/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1247x845")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 845,
    width = 1247,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1013.0,
    426.0,
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
    x=203.0,
    y=71.0,
    width=74.0,
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
    x=341.0,
    y=71.0,
    width=86.0,
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
    x=478.0,
    y=71.0,
    width=134.0,
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
    x=192.0,
    y=616.0,
    width=383.0,
    height=99.0
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
    217.0,
    anchor="nw",
    text="Sleep is essential!",
    fill="#C94C4C",
    font=("Inter Bold", 40 * -1)
)

canvas.create_text(
    41.0,
    283.0,
    anchor="nw",
    text="Sleep is not only a biological necessity but also a physiological drive.",
    fill="#000000",
    font=("Inter Regular", 32 * -1)
)

canvas.create_text(
    32.0,
    454.0,
    anchor="nw",
    text="Want to track your sleeping habits?",
    fill="#000000",
    font=("Inter Medium", 40 * -1)
)

canvas.create_text(
    32.0,
    503.0,
    anchor="nw",
    text="Register Below!",
    fill="#000000",
    font=("Inter Bold", 36 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    835.0,
    641.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
