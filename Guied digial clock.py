import tkinter as ui
import time

clock_window = ui.Tk()


def update_clock():
    hour = time.strftime("%H")
    min = time.strftime("%M")
    second = time.strftime("%S")
    am_or_pm = time.strftime("%p")

    updated_time = hour + ":" + min + ":" + second + " " + am_or_pm

    clock_lbl.config(text=updated_time)
    clock_lbl.after(1000, update_clock)


clock_window.title("Nolo's digital clock")

clock_lbl = ui.Label(clock_window, text="00:00:00")
clock_lbl.pack()

update_clock()

clock_window.mainloop()
