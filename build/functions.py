from tkinter import *

def display(entry_1, entry_2):
    try:
        name = entry_1.get()
        age = entry_2.get()
        display = f'The name is {name} and you are {age}'
        return display
    except Exception as error:
        print(f'Error: {error}')
        return str(error)

