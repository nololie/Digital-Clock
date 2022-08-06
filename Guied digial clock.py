from ctypes import windll
import tkinter as ui

clock_window = ui.Tk()

clock_window.title("Nolo's digital clock")

clock_lbl = ui.Label(clock_window, text="00:00:00")
clock_lbl.pack()

clock_window.mainloop()
