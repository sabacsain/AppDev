from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def start(window, frame):
    window = window
    frame = frame

    global gender
    gender = None

    canvas = Canvas(
        window,
        bg="#DEEAEE",
        height=838,
        width=1244,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    # canvas.create_text(
    #     78.0,
    #     203.0,
    #     anchor="nw",
    #     text="HOW DID YOUR SLEEP GO?",
    #     fill="#000000",
    #     font=("Inter Medium", 40 * -1)
    # )

    # canvas.create_text(
    #     78.0,
    #     252.0,
    #     anchor="nw",
    #     text="WELCOME!",
    #     fill="#000000",
    #     font=("Inter Bold", 36 * -1)
    # )

    # canvas.create_rectangle(
    #     159.0,
    #     315.0,
    #     788.0,
    #     721.0,
    #     fill="#92A8D1",
    #     outline="")

    rectangle_image = PhotoImage(                                       # Rounded Rectangle
        file=relative_to_assets("rectangle.png"))
    rectangle = canvas.create_image(
        480,
        520,
        # 188.0,
        # 369.0,
        # 817.0,
        # 718.0,
        image=rectangle_image
    )

    canvas.create_text(
        201.0,
        344.0,
        anchor="nw",
        text="First Name",
        fill="#000000",
        font=("Inter ExtraBold", 17 * -1)
    )

    canvas.create_text(
        376.0,
        344.0,
        anchor="nw",
        text="Last Name",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    canvas.create_text(
        201.0,
        433.0,
        anchor="nw",
        text="Phone Number",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    canvas.create_text(
        557.0,
        433.0,
        anchor="nw",
        text="Birthday (YY-MM-DD)",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    canvas.create_text(
        201.0,
        525.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    radio_buttonMale_Image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    radio_buttonMale = Button(
        image=radio_buttonMale_Image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_imageRadioMale(),
        relief="flat"
    )
    radio_buttonMale.place(
        x=554.0,
        y=375.0,
        width=29.0,
        height=29.0
    )

    radio_buttonFemale_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    radio_buttonFemale = Button(
        image=radio_buttonFemale_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_imageRadioFemale(),
        relief="flat"
    )
    radio_buttonFemale.place(
        x=648.0,
        y=375.0,
        width=29.0,
        height=29.0
    )

    canvas.create_text(
        591.0,
        378.0,
        anchor="nw",
        text="Male",
        fill="#000000",
        font=("Inter Regular", 17 * -1)
    )

    canvas.create_text(
        685.0,
        378.0,
        anchor="nw",
        text="Female",
        fill="#000000",
        font=("Inter Regular", 17 * -1)
    )

    canvas.create_text(
        557.0,
        344.0,
        anchor="nw",
        text="Sex",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    canvas.create_text(
        80.0,
        776.0000610351562,
        anchor="nw",
        text="Have an Existing Account? ",
        fill="#000000",
        font=("Inter Regular", 20 * -1)
    )

    register_button_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    register_button = Button(
        image=register_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.register(
            window, frame, fname, lname, phone_number, birthday, password, gender),
        relief="flat"
    )
    register_button.place(
        x=366.0,
        y=627.0,
        width=217.0,
        height=76.0
    )

    login_button_image = PhotoImage(
        file=relative_to_assets("loginRed.png"))
    login_button = Button(
        image=login_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callLogin(window, frame),
        relief="flat"
    )
    login_button.place(
        x=430.0,
        y=773.0,
        width=161.0,
        height=41.0
    )

    # button_image_5 = PhotoImage(
    #     file=relative_to_assets("button_5.png"))
    # about_button = Button(
    #     image=button_image_5,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: functions.callAbout(window, frame),
    #     relief="flat"
    # )
    # about_button.place(
    #     x=190.0,
    #     y=75.0,
    #     width=90.0,
    #     height=29.0
    # )

    # button_image_6 = PhotoImage(
    #     file=relative_to_assets("button_6.png"))
    # contact_button = Button(
    #     image=button_image_6,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: functions.callContact(window, frame),
    #     relief="flat"
    # )
    # contact_button.place(
    #     x=325.0,
    #     y=75.0,
    #     width=127.0,
    #     height=29.0
    # )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        280.5,
        394.5,
        image=entry_image_1
    )
    fname = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 16 * -1)
    )
    fname.place(
        x=211.0,
        y=369.0,
        width=139.0,
        height=49.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        368.0,
        483.5,
        image=entry_image_2
    )
    phone_number = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 16 * -1)
    )
    phone_number.place(
        x=211.0,
        y=458.0,
        width=314.0,
        height=49.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        368.0,
        575.5,
        image=entry_image_3
    )
    password = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        show="*",
        font=("Inter Regular", 16 * -1)
    )
    password.place(
        x=211.0,
        y=550.0,
        width=314.0,
        height=49.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        455.5,
        394.5,
        image=entry_image_4
    )
    lname = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 16 * -1)
    )
    lname.place(
        x=386.0,
        y=369.0,
        width=139.0,
        height=49.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        649.5,
        483.5,
        image=entry_image_5
    )
    birthday = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 16 * -1)
    )
    birthday.place(
        x=567.0,
        y=458.0,
        width=165.0,
        height=49.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        682.0,
        426.0008850097656,
        image=image_image_1
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        465.0,
        240,
        image=image_image_11
    )

    hoverRegister = PhotoImage(
        file=relative_to_assets("register_RegisterForm.png"))
    hoverLogin = PhotoImage(file=relative_to_assets("loginRedder.png"))
    hoverRadio = PhotoImage(file=relative_to_assets("radioClicked.png"))

    # Function to change image when mouse enters button
    def change_imageRegister(event):
        register_button.config(image=hoverRegister)

    def change_imageLogin(event):
        login_button.config(image=hoverLogin)

    # Function to change image when radiobutton is clicked
    def change_imageRadioMale():
        # functions.disable_radioBtn(radio_buttonMale,radio_buttonFemale)
        global gender
        gender = 'MALE'
        radio_buttonMale.config(image=hoverRadio)
        change_backRadioFemale()

    def change_imageRadioFemale():
        # functions.disable_radioBtn(radio_buttonFemale,radio_buttonMale)
        global gender
        gender = 'FEMALE'
        radio_buttonFemale.config(image=hoverRadio)
        change_backRadioMale()

    # Function to change back to original image when mouse leaves button
    def change_backRegister(event):
        register_button.config(image=register_button_image)

    def change_backLogin(event):
        login_button.config(image=login_button_image)

    def change_backRadioMale():
        radio_buttonMale.config(image=radio_buttonMale_Image)

    def change_backRadioFemale():
        radio_buttonFemale.config(image=radio_buttonMale_Image)

    # Bind the <Enter> event to change_image function
    register_button.bind("<Enter>", change_imageRegister)
    login_button.bind("<Enter>", change_imageLogin)

    # Bind the <Leave> event to change_back function
    register_button.bind("<Leave>", change_backRegister)
    login_button.bind("<Leave>", change_backLogin)

    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg="#DEEAEE")
    start(window, frame=window)
