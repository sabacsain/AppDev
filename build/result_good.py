from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame14")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def start(window, frame, phone):
    window = window
    frame = frame
    user_profile = functions.get_user_profile(phone)

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
    # canvas.create_text(
    #     93.0,
    #     #708.0,
    #     745.0,
    #     anchor="nw",
    #     text="Do you want to see your weekly or monthly report?",
    #     fill="#000000",
    #     font=("Inter Bold", 24 * -1, 'bold')
    # )

    # canvas.create_text(
    #     163.0,
    #     227.0,
    #     anchor="nw",
    #     text="you’ve done a wonderful job up to this point.",
    #     fill="#000000",
    #     font=("Inter SemiBold", 36 * -1,'bold')
    # )

    canvas.create_text(
        163.0,
        182.0,
        anchor="nw",
        text= str(user_profile[0][0]).upper() + ",",
        fill="#54899E",
        font=("Inter Bold", 40 * -1, 'bold')
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        629.0,
        76.0,
        image=image_image_1
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    menu_button = Button(
        image=button_image_3,
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
    
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    about_button = Button(
        image=button_image_4,
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

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    contact_button = Button(
        image=button_image_5,
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
        76.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        629.0,
        527.0,
        image=image_image_3
    )

    weekly_button_image = PhotoImage(
        file=relative_to_assets("button_4.png"))
    weekly_button = Button(
        image=weekly_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callWeeklyInput(window, frame, phone),
        relief="flat"
    )
    weekly_button.place(
        x=717.0,
        # y=701.0,
        y = 720.0,
        width=219.0,
        height=78.0
    )

    monthly_button_image = PhotoImage(
        file=relative_to_assets("button_5.png"))
    monthly_button = Button(
        image=monthly_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callMonthlyInput(window, frame, phone),
        relief="flat"
    )
    monthly_button.place(
        x=960.0,
        # y=701.0,
        y = 720.0,
        width=219.0,
        height=78.0
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_12.png"))
    image_8 = canvas.create_image(
        628.0,
        270.0,
        image=image_image_8
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        380,
        770,
        image=image_image_10
    )
    
    hoverWeekly = PhotoImage(file=relative_to_assets("weekly.png"))
    hoverMonthly = PhotoImage(file=relative_to_assets("monthly.png"))

    # Function to change image when mouse enters button
    def change_imageWeekly(event):
        weekly_button.config(image=hoverWeekly)
    def change_imageMonthly(event):
        monthly_button.config(image=hoverMonthly)

    # Function to change back to original image when mouse leaves button
    def change_backWeekly(event):
        weekly_button.config(image=weekly_button_image)
    def change_backMonthly(event):
        monthly_button.config(image=monthly_button_image)

    # Bind the <Enter> event to change_image function
    weekly_button.bind("<Enter>", change_imageWeekly)
    monthly_button.bind("<Enter>", change_imageMonthly)

    # Bind the <Enter> event to change_image function
    weekly_button.bind("<Leave>", change_backWeekly)
    monthly_button.bind("<Leave>", change_backMonthly)
    
    # Start the GUI
    window.resizable(False, False)
    window.mainloop()

    
if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window, phone='11')
