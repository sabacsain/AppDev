import tkinter

root = tkinter.Tk()
root.overrideredirect(True)
root.geometry("600x400")
root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())

# Add other widgets to the root window here

root.mainloop()


