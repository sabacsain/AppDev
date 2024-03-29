from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions
from tkcalendar import Calendar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame4")


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

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        250,
        215.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_7 = canvas.create_image(
        380,
        490.0,
        image=image_image_7
    )
    
    update_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    update_button = Button(
        image=update_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.update_sleep(window, frame, phone, entry_4, cal),
        relief="flat"
    )
    update_button.place(
        x=163.0,
        y=650.0,
        width=345.0,
        height=86.0
    )

    # canvas.create_text(
    #     183.0,
    #     200,
    #     anchor="nw",
    #     text="DATE",
    #     fill="#000000",
    #     font=("Inter SemiBold", 36 * -1)
    # )

        # Add Calendar
    cal = Calendar(window, selectmode = 'day',
                year = 2023, month = 2,
                day = 17)

    cal.place(
        x = 183.0, 
        y = 250
    )

    # canvas.create_text(
    #     551.0,
    #     266.0,
    #     anchor="nw",
    #     text="YEAR",
    #     fill="#000000",
    #     font=("Inter SemiBold", 36 * -1)
    # )

    # canvas.create_text(
    #     394.0,
    #     266.0,
    #     anchor="nw",
    #     text="DAY",
    #     fill="#000000",
    #     font=("Inter SemiBold", 36 * -1)
    # )

    # canvas.create_text(
    #     183.0,
    #     460.0,
    #     anchor="nw",
    #     text="HOURS OF SLEEP",
    #     fill="#000000",
    #     font=("Inter SemiBold", 36 * -1)
    # )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        629.0,
        76.0,
        image=image_image_1
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    menu_button = Button(
        image=button_image_2,
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

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    about_button = Button(
        image=button_image_3,
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

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    contact_button = Button(
        image=button_image_4,
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

    # entry_image_1 = PhotoImage(
    #     file=relative_to_assets("entry_1.png"))
    # entry_bg_1 = canvas.create_image(
    #     252.0,
    #     339.5,
    #     image=entry_image_1
    # )
    # entry_1 = Entry(
    #     bd=0,
    #     bg="#FFFFFF",
    #     fg="#000716",
    #     highlightthickness=0
    # )
    # entry_1.place(
    #     x=173.0,
    #     y=314.0,
    #     width=158.0,
    #     height=49.0
    # )

    # entry_image_2 = PhotoImage(
    #     file=relative_to_assets("entry_2.png"))
    # entry_bg_2 = canvas.create_image(
    #     432.0,
    #     339.5,
    #     image=entry_image_2
    # )
    # entry_2 = Entry(
    #     bd=0,
    #     bg="#FFFFFF",
    #     fg="#000716",
    #     highlightthickness=0
    # )
    # entry_2.place(
    #     x=353.0,
    #     y=314.0,
    #     width=158.0,
    #     height=49.0
    # )

    # entry_image_3 = PhotoImage(
    #     file=relative_to_assets("entry_3.png"))
    # entry_bg_3 = canvas.create_image(
    #     612.0,
    #     339.5,
    #     image=entry_image_3
    # )
    # entry_3 = Entry(
    #     bd=0,
    #     bg="#FFFFFF",
    #     fg="#000716",
    #     highlightthickness=0
    # )
    # entry_3.place(
    #     x=533.0,
    #     y=314.0,
    #     width=158.0,
    #     height=49.0
    # )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        447.5,
        550.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 24 * -1),
        justify="center"
    )
    entry_4.place(
        x=190.0,
        y=527.0,
        width=515.0,
        height=47.0
    )


    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        129.0,
        76.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        1006.0,
        491.0,
        image=image_image_3
    )
    
    hoverUpdate = PhotoImage(file=relative_to_assets("update.png"))

    # Function to change image when mouse enters button
    def change_imageGetStarted(event):
        update_button.config(image=hoverUpdate)

    # Function to change back to original image when mouse leaves button
    def change_backGetStarted(event):
        update_button.config(image=update_button_image)

    # Bind the <Enter> event to change_image function
    update_button.bind("<Enter>", change_imageGetStarted)

    # Bind the <Leave> event to change_back function
    update_button.bind("<Leave>", change_backGetStarted)
    
    window.resizable(False, False)
    window.mainloop()
    
if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window, phone='11')
