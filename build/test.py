import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_graph():
    fig, ax = plt.subplots()
    ax.bar(["January", "February"], [7.5, 8.0])
    ax.set_ylabel("Average Sleep Value (hours)")
    ax.set_title("Average Sleep Value Per Month")
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)

window = tk.Tk()
create_graph()
window.mainloop()
