from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import functions
import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame8")


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
    # canvas.create_text(
    #     112.0,
    #     250.0,
    #     anchor="nw",
    #     text="Enter date range:",
    #     fill="#000000",
    #     font=("Inter Bold", 36 * -1, 'bold')
    # )

    generate_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    generate_button = Button(
        image=generate_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.callWeeklyGraph(window, frame, month, year, phone),
        relief="flat"
    )
    generate_button.place(
        x=433.0,
        y=522.0,
        width=413.0,
        height=78.0
    )

    # canvas.create_text(
    #     491.0,
    #     412.0,
    #     anchor="nw",
    #     text="MONTH",
    #     fill="#000000",
    #     font=("Inter Bold", 24 * -1, 'bold')
    # )

    # canvas.create_text(
    #     704.0,
    #     412.0,
    #     anchor="nw",
    #     text="YEAR",
    #     fill="#000000",
    #     font=("Inter Bold", 24 * -1, 'bold')
    # )

    # canvas.create_rectangle(
    #     872.0,
    #     190.0,
    #     1153.0,
    #     267.0,
    #     fill="#D9D9D9",
    #     outline="")

    # canvas.create_text(
    #     872.0,
    #     206.0,
    #     anchor="nw",
    #     text="WEEKLY",
    #     fill="#000000",
    #     font=("Inter SemiBold", 36 * -1)
    # )

    image_image_3 = PhotoImage(
        file=relative_to_assets("week.png"))
    image_3 = canvas.create_image(
        965.0,
        250.0,
        image=image_image_3
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
        command=lambda: functions.callAbout(window, frame,phone),
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

   
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        531.5,
        479.5,
        image=entry_image_1
    )
    # entry_1 = Entry(
    #     bd=0,
    #     bg="#FFFFFF",
    #     fg="#000716",
    #     highlightthickness=0
    # )
    # entry_1.place(
    #     x=446.0,
    #     y=448.0,
    #     width=171.0,
    #     height=61.0
    # )

    # button_image_6 = PhotoImage(
    #     file=relative_to_assets("button_6.png"))
    # button_6 = Button(
    #     image=button_image_6,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_6 clicked"),
    #     relief="flat"
    # )
    # button_6.place(
    #     x=592.0,
    #     y=467.0,
    #     width=31.300262451171875,
    #     height=26.0
    # )

    canvas.create_text(
        476.0,
        465.0,
        anchor="nw",
        text="January",
        fill="#665F5F",
        font=("Inter ExtraLight", 25 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        747.5,
        479.5,
        image=entry_image_2
    )
    # entry_2 = Entry(
    #     bd=0,
    #     bg="#FFFFFF",
    #     fg="#000716",
    #     highlightthickness=0
    # )
    # entry_2.place(
    #     x=662.0,
    #     y=448.0,
    #     width=171.0,
    #     height=61.0
    # )

    # button_image_7 = PhotoImage(
    #     file=relative_to_assets("button_7.png"))
    # button_7 = Button(
    #     image=button_image_7,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_7 clicked"),
    #     relief="flat"
    # )
    # button_7.place(
    #     x=808.0,
    #     y=467.0,
    #     width=31.30023193359375,
    #     height=26.0
    # )

    # canvas.create_text(
    #     715.0,
    #     465.0,
    #     anchor="nw",
    #     text="2022",
    #     fill="#665F5F",
    #     font=("Inter ExtraLight", 25 * -1)
    # )


    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        440.0,
        340.0,
        image=image_image_7
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        140.0,
        81.0,
        image=image_image_2
    )

    
    #function to get value of combo box
    def cbx_month_click(event):
        global month
        month = cbx_month.get()
        print(month)

    def cbx_year_click(event):
        global year
        year = cbx_year.get()
        print(year)


    cbx_month_options = ["01", "02", "03","04","05","06","07","08","09","10","11","12"]
    cbx_month  = ttk.Combobox(values=cbx_month_options)
    cbx_month.current(cbx_month_options.index(datetime.datetime.today().strftime('%m')))
    cbx_month.bind("<<ComboboxSelected>>", cbx_month_click)
    cbx_month.place(
        x=440.0,
        y=452.0,
        width=184,
        height=56,
        )
    cbx_month.config(
        font=("Inter ExtraLight", 25 * -1),
        justify="center",
        state="readonly"
        )

    cbx_year_options = [str(i) for i in range(2010,datetime.datetime.today().year + 1)]
    cbx_year  = ttk.Combobox(values=cbx_year_options)
    cbx_year.current(cbx_year_options.index(str(datetime.datetime.today().year)))
    cbx_year.bind("<<ComboboxSelected>>", cbx_year_click)
    cbx_year.place(
        x=658.0,
        y=452.0,
        width=182,
        height=56,
        )
    cbx_year.config(
        font=("Inter ExtraLight", 25 * -1),
        justify="center",
        state="readonly"
        )

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "white", background= "#DEEAEE")

    # in case the user doesn't click the comboboxes
    cbx_month_click("<<ComboboxSelected>>")
    cbx_year_click("<<ComboboxSelected>>")


    hoverGenerate = PhotoImage(file=relative_to_assets("generate.png"))

    # Function to change image when mouse enters button
    def change_imageGetStarted(event):
        generate_button.config(image=hoverGenerate)

    # Function to change back to original image when mouse leaves button
    def change_backGetStarted(event):
        generate_button.config(image=generate_button_image)

    # Bind the <Enter> event to change_image function
    generate_button.bind("<Enter>", change_imageGetStarted)

    # Bind the <Leave> event to change_back function
    generate_button.bind("<Leave>", change_backGetStarted)



    window.resizable(False, False)
    window.mainloop()



if __name__ == '__main__':
    window = Tk()
    window.geometry("1244x838")
    window.configure(bg = "#DEEAEE")
    start(window, frame=window, phone='11')