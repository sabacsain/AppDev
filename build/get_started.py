

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame2")


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
        80.0,
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
        y=70.0,
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
        y=70.0,
        width=131.0,
        height=37.0
    )

    getStarted_button_image = PhotoImage(
        file=relative_to_assets("button_4.png"))
    get_started_button = Button(
        image=getStarted_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callInputSleep(window, frame, phone),
        relief="flat"
    )
    get_started_button.place(
        x=138.0,
        y=612.0,
        width=223.0,
        height=78.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        127.0,
        76.0,
        image=image_image_2
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        580.0,
        380.0,
        image=image_image_4
    )

    hoverGetStarted = PhotoImage(file=relative_to_assets("getStarted.png"))

    # Function to change image when mouse enters button
    def change_imageGetStarted(event):
        get_started_button.config(image=hoverGetStarted)

    # Function to change back to original image when mouse leaves button
    def change_backGetStarted(event):
        get_started_button.config(image=getStarted_button_image)


    # Bind the <Enter> event to change_image function
    get_started_button.bind("<Enter>", change_imageGetStarted)

    # Bind the <Leave> event to change_back function
    get_started_button.bind("<Leave>", change_backGetStarted)

    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window, phone='11')
