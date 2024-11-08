import time


class Time:
    def __init__(self, t: time):
        self.hour = time.strftime('%I')
        self.minute = time.strftime("%M")
        self.second = time.strftime("%S")
        self.p = time.strftime("%p")
        self.week_day = time.strftime("%A")
        self.month_day = time.strftime("%d")

    def display(self) -> str:
        return f"{self.week_day} {self.month_day}th\n{self.hour}:{self.minute}:{self.second}{self.p}"
