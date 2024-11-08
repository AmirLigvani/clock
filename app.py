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
    zone = time.strftime("%Z")

    txt = week_day + "\n" + h + ":" + m + ":" + S + "" + "\n" + am_pm
    txt2 = zone
    label.config(text=txt)
    label.after(1000, CurrentTime)
    label2.config(text=txt2)
    label2.after(1000, CurrentTime)


label = Label(ui, text="", font=(None, 62), fg='blue', bg='skyblue')
label2 = Label(ui, text="", font=(None, 24), bg="skyblue", fg="blue")
label.pack()
label2.pack()
CurrentTime()

ui.mainloop()
