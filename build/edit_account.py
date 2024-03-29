
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import functions 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def start(window, frame, phone):

    new_phone = phone
    global gender
    gender = None

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

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        625.0,
        76.0,
        image=image_image_1
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        642.0,
        230.0,
        image=image_image_8
    )

    # updates phone after updating profile
    def update_profile():
        nonlocal new_phone
        new_phone = functions.update_profile(window, frame, phone, entry_1, entry_5, entry_2, entry_6, entry_4, gender)
       

    save_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    save_button = Button(
        image=save_button_image,
        borderwidth=0,
        highlightthickness=0,
        command= update_profile,
        relief="flat"
    )
    save_button.place(
        x=310.0,
        y=630.0,
        width=639.0,
        height=84.0
    )


    rectangle_image = PhotoImage(                                       # Rounded Rectangle
        file=relative_to_assets("rectangle1.png"))
    rectangle = canvas.create_image(
        628,
        450,
        # 188.0,
        # 369.0,
        # 817.0,
        # 718.0,
        image=rectangle_image
    )

    canvas.create_text(
        352.0,
        312.0,
        anchor="nw",
        text="First Name",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    canvas.create_text(
        527.0,
        312.0,
        anchor="nw",
        text="Last Name",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    canvas.create_text(
        352.0,
        401.0,
        anchor="nw",
        text="Phone Number",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    canvas.create_text(
        708.0,
        401.0,
        anchor="nw",
        text="Birthday",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    canvas.create_text(
        352.0,
        493.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    radio_buttonMale_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    radio_buttonMale = Button(
        image=radio_buttonMale_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_imageRadioMale(),
        relief="flat"
    )
    radio_buttonMale.place(
        x=705.0,
        y=343.0,
        width=29.0,
        height=29.0
    )

    radio_buttonFemale_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    radio_buttonFemale = Button(
        image=radio_buttonFemale_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_imageRadioFemale(),
        relief="flat"
    )
    radio_buttonFemale.place(
        x=799.0,
        y=343.0,
        width=29.0,
        height=29.0
    )

    canvas.create_text(
        742.0,
        346.0,
        anchor="nw",
        text="Male",
        fill="#000000",
        font=("Inter Regular", 17 * -1)
    )

    canvas.create_text(
        836.0,
        346.0,
        anchor="nw",
        text="Female",
        fill="#000000",
        font=("Inter Regular", 17 * -1)
    )

    canvas.create_text(
        708.0,
        312.0,
        anchor="nw",
        text="Sex",
        fill="#000000",
        font=("Inter Bold", 17 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        431.5,
        362.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 16 * -1)
    )
    entry_1.place(
        x=362.0,
        y=337.0,
        width=139.0,
        height=49.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        519.0,
        451.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 16 * -1)
    )
    entry_2.place(
        x=362.0,
        y=426.0,
        width=314.0,
        height=49.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        519.0,
        543.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 16 * -1)
    )
    entry_3.place(
        x=362.0,
        y=518.0,
        width=314.0,
        height=49.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        519.0,
        543.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        show='*',
        font=("Inter Regular", 16 * -1)
    )
    entry_4.place(
        x=362.0,
        y=518.0,
        width=314.0,
        height=49.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        606.5,
        362.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 16 * -1)
    )
    entry_5.place(
        x=537.0,
        y=337.0,
        width=139.0,
        height=49.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        800.5,
        451.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter Regular", 16 * -1)
    )
    entry_6.place(
        x=718.0,
        y=426.0,
        width=165.0,
        height=49.0
    )

    # Insert 
    entry_1.insert(0, user_profile[0][0]) # entry_1 = First Name
    entry_5.insert(0, user_profile[0][1]) # entry_5 = Last Name
    entry_2.insert(0, user_profile[0][3]) # entry_2 = Phone Number
    entry_6.insert(0, user_profile[0][4]) # entry_6 = Birthday
    

    def confirm_delete_account():
        answer = messagebox.askyesno("Confirm Deletion of Account", "Are your sure you want to Delete your Account?")
        if answer == 1:
            delete_account_and_records()
        else:
            return

    def delete_account_and_records():
        functions.delete_account_and_records(window, frame, new_phone),

    delete_button_image = PhotoImage(
        file=relative_to_assets("button_4.png"))
    delete_button = Button(
        image=delete_button_image,
        borderwidth=0,
        highlightthickness=0,
        # command=delete_account_and_records,
        command = confirm_delete_account,
        relief="flat"
    )
    delete_button.place(
        x=939.0,
        y=38.0,
        width=249.0,
        height=78.0
    )

    def callHome(new_phone):
        try:
            new_phone
        except:
            new_phone = phone
            functions.callHome(window, frame, new_phone)
            return
        functions.callHome(window, frame, new_phone)

            


    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    menu_button = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command = lambda: callHome(new_phone),
        relief="flat"
    )
    menu_button.place(
        x=230.0,
        y=56.0,
        width=93.0,
        height=40.0
    )


    def callAbout(new_phone):
        try:
            new_phone
        except:
            new_phone = phone,
            functions.callAbout(window, frame, new_phone)
            return
        functions.callAbout(window, frame, new_phone)




    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    about_button = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command =  lambda: callAbout(new_phone),
        relief="flat"
    )
    about_button.place(
        x=363.0,
        y=59.0,
        width=106.0,
        height=34.0
    )

    def callContact(new_phone):
        try:
            new_phone
        except:
            new_phone = phone,
            functions.callContact(window, frame, new_phone)
            return
        functions.callContact(window, frame, new_phone)


    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    contact_button = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: callContact(new_phone),
        relief="flat"
    )
    contact_button.place(
        x=510.0,
        y=59.0,
        width=131.0,
        height=37.0
    )
    
    hoverSave = PhotoImage(file=relative_to_assets("save.png"))
    hoverRadio = PhotoImage(file=relative_to_assets("radioClicked.png"))
    hoverDelete = PhotoImage(file=relative_to_assets("deleteRed.png"))
    
    # Function to change image when mouse enters button
    def change_imageGetStarted(event):
        save_button.config(image=hoverSave)
    def change_imageDelete(event):
        delete_button.config(image=hoverDelete)
   
    # Function to change image when radiobutton is clicked
    def change_imageRadioMale():
        global gender
        gender = 'MALE'
        radio_buttonMale.config(image=hoverRadio)
        # functions.disable_radioBtn(radio_buttonMale,radio_buttonFemale)
        change_backRadioFemale()
    def change_imageRadioFemale():
        global gender
        gender = 'FEMALE'
        radio_buttonFemale.config(image=hoverRadio)
        # functions.disable_radioBtn(radio_buttonFemale,radio_buttonMale)
        change_backRadioMale()

    # Function to change back to original image when mouse leaves button or radiobutton disabled
    def change_backGetStarted(event):
        save_button.config(image=save_button_image)
    def change_backDelete(event):
        delete_button.config(image=delete_button_image)
    def change_backRadioMale():
        radio_buttonMale.config(image=radio_buttonMale_image)
    def change_backRadioFemale():   
        radio_buttonFemale.config(image=radio_buttonFemale_image)

    # Bind the <Enter> event to change_image function
    save_button.bind("<Enter>", change_imageGetStarted)
    delete_button.bind("<Enter>", change_imageDelete)
    
    # Bind the <Leave> event to change_back function
    save_button.bind("<Leave>", change_backGetStarted)
    delete_button.bind("<Leave>", change_backDelete)

    window.resizable(False, False)
    window.mainloop()
    


if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window, phone='11')
