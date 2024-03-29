from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import functions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def start():
    window = Tk()
    window.title('Sleep Ease')
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    
    frame = Frame(window)

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
        1007.0,
        413.0,
        image=image_image_1
    )

    register_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    register_button = Button(
        image=register_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callRegister(window, frame),
        relief="flat"
    )
    register_button.place(
        x=392.0,
        y=517.0,
        width=344.0,
        height=95.0
    )

    login_button_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    login_button = Button(
        image=login_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callLogin(window, frame),
        relief="flat"
    )
    login_button.place(
        x=392.0,
        y=645.0,
        width=350.0,
        height=95.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        525.0,
        207.0,
        image=image_image_2
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        565,
        407.0,
        image=image_image_11
    )

    # canvas.create_text(
    #     225.0,
    #     356.0,
    #     anchor="nw",
    #     text="Want to track your sleeping habits?",
    #     fill="#000000",
    #     font= ("Inter Bold", 40 * -1)
    # )

    # canvas.create_text(
    #     435.0,
    #     410.0,
    #     anchor="nw",
    #     text="Register Below!",
    #     fill="#000000",
    #     font=("Inter Bold", 36 * -1)
    # )

    hoverRegister = PhotoImage(file=relative_to_assets("registerMain.png"))
    hoverLogin = PhotoImage(file=relative_to_assets("loginMain.png"))

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
    start()