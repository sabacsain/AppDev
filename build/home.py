
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame3")


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
    canvas.create_text(
        73.0,
        346.0,
        anchor="nw",
        text="HELLO, " + str(user_profile[0][0]).upper() + "!",
        fill="#1E343D",
        font=("Inter Bold", 50 * -1, 'bold')
    )

    logout_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    logout_button = Button(
        image=logout_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callLogin(window, frame),
        relief="flat"
    )
    logout_button.place(
        x=41.0,
        # y=644.0,
        y = 700,
        width=1174.0,
        height=106.0
    )

    edit_button_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    edit_button = Button(
        image=edit_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callEditAccount(window, frame, phone),
        relief="flat"
    )
    edit_button.place(
        x=68.0,
        y=415.0,
        width=195.0,
        height=41.0
    )

    weekly_button_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    weekly_button = Button(
        image=weekly_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callWeeklyInput(window, frame, phone),
        relief="flat"
    )
    weekly_button.place(
        x=651.0,
        # y=298.0,
        y = 334,
        width=554.0,
        height=94.0
    )

    update_button_image = PhotoImage(
        file=relative_to_assets("updateRecords.png"))
    update_button = Button(
        image=update_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callUpdate(window, frame, phone),
        relief="flat"
    )
    update_button.place(
    x=649.0,
    # y=191.0,
    y = 227.0,
    width=554.0,
    height=94.0
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
        x=652.0,
        # y=405.0,
        y = 441.0,
        width=554.0,
        height=94.0
    )

    view_button_image = PhotoImage(
    file=relative_to_assets("view_all.png"))
    view_button = Button(
        image=view_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callView(window, frame, phone),
        relief="flat"
    )
    view_button.place(
        x=653.0,
        # y=512.0,
        y = 548.0,
        width=554.0,
        height=94.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        629.0,
        76.0,
        image=image_image_1
    )

    menu_button_image = PhotoImage(
        file=relative_to_assets("button_6.png"))
    menu_button = Button(
        image=menu_button_image,
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

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    about_button = Button(
        image=button_image_7,
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

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    contact_button = Button(
        image=button_image_8,
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

    hoverLogout = PhotoImage(file=relative_to_assets("logout.png"))
    hoverUpdate = PhotoImage(file=relative_to_assets("updateSleep.png"))
    hoverWeekly = PhotoImage(file=relative_to_assets("generateWeekly.png"))
    hoverMonthly = PhotoImage(file=relative_to_assets("generateMonthly.png"))
    hoverEdit = PhotoImage(file=relative_to_assets("edit_details.png"))
    hoverView = PhotoImage(file=relative_to_assets("view_all_blue.png"))

    # Function to change image when mouse enters button
    def change_imageGetStarted(event):
        logout_button.config(image=hoverLogout)
    def change_imageUpdate(event):
        update_button.config(image=hoverUpdate)
    def change_imageWeekly(event):
        weekly_button.config(image=hoverWeekly)
    def change_imageMonthly(event):
        monthly_button.config(image=hoverMonthly)
    def change_imageEdit(event):
        edit_button.config(image=hoverEdit)
    def change_imageView(event):
        view_button.config(image=hoverView)

    # Function to change back to original image when mouse leaves button
    def change_backGetStarted(event):
        logout_button.config(image=logout_button_image)
    def change_backUpdate(event):
        update_button.config(image=update_button_image)
    def change_backWeekly(event):
        weekly_button.config(image=weekly_button_image)
    def change_backMonthly(event):
        monthly_button.config(image=monthly_button_image)
    def change_backEdit(event):
        edit_button.config(image=edit_button_image)
    def change_backView(event):
        view_button.config(image=view_button_image)
    
    # Bind the <Enter> event to change_image function
    logout_button.bind("<Enter>", change_imageGetStarted)
    update_button.bind("<Enter>", change_imageUpdate)
    weekly_button.bind("<Enter>", change_imageWeekly)
    monthly_button.bind("<Enter>", change_imageMonthly)
    edit_button.bind("<Enter>", change_imageEdit)
    view_button.bind("<Enter>", change_imageView)

    # Bind the <Leave> event to change_back function
    logout_button.bind("<Leave>", change_backGetStarted)
    update_button.bind("<Leave>", change_backUpdate)
    weekly_button.bind("<Leave>", change_backWeekly)
    monthly_button.bind("<Leave>", change_backMonthly)
    edit_button.bind("<Leave>", change_backEdit)
    view_button.bind("<Leave>", change_backView)
    
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window, phone='11')
