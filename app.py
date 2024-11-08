from tkinter import *
import time
from Time import Time

ui = Tk()
ui.title("saat")
ui.geometry('600x300')
ui.configure(bg='black')


def current_time():
    t = Time(time)

    label.config(
        text=t.display())
    label.after(1000, current_time)


if __name__ == "__main__":
    label = Label(ui, text="", font=(None, 62), fg='white', bg='black')
    label.pack(expand=True, fill=BOTH)
    current_time()
    ui.mainloop()
