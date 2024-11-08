from tkinter import *
import time

ui = Tk()
ui.title("saat")
ui.geometry('600x300')


def CurrentTime():
    h = time.strftime('%I')
    m = time.strftime("%M")
    S = time.strftime("%S")
    am_pm = time.strftime("%p")
    week_day = time.strftime("%A")
    day = time.strftime("%d")
    txt = week_day + " " + day + "th" + "\n" + \
        h + ":" + m + ":" + S + "" + "\n" + am_pm
    label.config(text=txt)
    label.after(1000, CurrentTime)


label = Label(ui, text="", font=(None, 62), fg='blue', bg='skyblue')

label.pack()

CurrentTime()

ui.mainloop()
