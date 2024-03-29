

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame10")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def start(window, frame):
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

    rectangle_image = PhotoImage(
        file=relative_to_assets("rectangle.png"))
    rectangle = canvas.create_image(
        506,
        550,
        image=rectangle_image
    )


    login_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    login_button = Button(
        image=login_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.login(window, frame, phone_number_entry, password_entry),
        relief="flat"
    )
    login_button.place(
        x=393.0,
        y=621.0,
        width=217.0,
        height=76.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        502.5,
        467.5,
        image=entry_image_1
    )
    phone_number_entry = Entry(                     # Phone Number Text Field
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 18 * -1),
	    justify = "center"
    )
    phone_number_entry.place(
        x=236.0,
        y=439.0,
        width=533.0,
        height=55.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        501.5,
        572.5,
        image=entry_image_2
    )
    password_entry = Entry(                             # Password Text Field
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        show='*',
        font=("Inter Regular", 18 * -1),
	    justify = "center"
    )
    password_entry.place(
        x=235.0,
        y=544.0,
        width=533.0,
        height=55.0
    )

    register_button_image = PhotoImage(
        file=relative_to_assets("registerRed.png"))
    register_button = Button(
        image=register_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callRegister(window, frame),
        relief="flat"
    )
    register_button.place(
        x=550.0,
        y=773.0,
        width=161.0,
        height=41.0
    )

    canvas.create_text(
        230.0,
        776.0000610351562,
        anchor="nw",
        text="Haven't registered yet? ",
        fill="#000000",
        font=("Inter Regular", 20 * -1)
    )

    canvas.create_text(
        429.0,
        404.0,
        anchor="nw",
        text="Phone Number",
        fill="#000000",
        font=("Inter SemiBold", 20 * -1)
    )


    image_image_2 = PhotoImage(
    file=relative_to_assets("image_welcome_back.png"))
    image_1 = canvas.create_image(
        400.0,
        255.0,
        image=image_image_2
    )
    canvas.create_text(
        447.0,
        508.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter SemiBold", 20 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        704.0,
        430.00048828125,
        image=image_image_1
    )


    hoverRegister = PhotoImage(file=relative_to_assets("registerRedder.png"))
    hoverLogin = PhotoImage(file=relative_to_assets("login_LoginForm.png"))

    # Function to change image when mouse enters button
    def change_imageRegister(event):
        register_button.config(image=hoverRegister)
    def change_imageLogin(event):
        login_button.config(image=hoverLogin)

    # Function to change back to original image when mouse leaves button
    def change_backRegister(event):
        register_button.config(image=register_button_image)
    def change_backLogin(event):
        login_button.config(image=login_button_image)

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
    window.configure(bg = "#DEEAEE")
    start(window, frame=window)
