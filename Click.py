from tkinter import *
from datetime import datetime


class Click:
    def __init__(self, x, y, color, time=-1):
        if time == -1:
            time = datetime.now()
        self.x = x
        self.y = y
        self.color = color
        self.time = time

    def getGui(self):
        root = Frame()

        Label(root, width=10, text=str(self.x) + "," + str(self.y)).grid(row=0, column=0)
        Label(root, width=7,  text=str("#%02x%02x%02x" % self.color), borderwidth=1, bg=("#%02x%02x%02x" % self.color)).grid(row=0, column=1)
        Label(root, width=10, text=self.time.strftime("%H:%M:%S")).grid(row=0, column=2)

        return root
