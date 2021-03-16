from tkinter import *
import pyautogui as pag


class Process:
    def __init__(self, clickX = 0, clickY = 0, checkX = -1, checkY = -1, checkColor = "#0099ff", actionInterval = 1000, active = True, name = "Action", action = None):
        self.clickX = clickX
        self.clickY = clickY
        self.checkX = clickX if checkX == -1 else checkX
        self.checkY = clickY if checkY == -1 else checkY
        self.checkColor = checkColor
        self.actionInterval = actionInterval
        self.name = name
        self.active = active
        self.action = self.defaultAction if action is None else action

    def defaultAction(self):
        color = pag.pixel(self.checkX, self.checkY)
        if color == self.checkColor:
            pag.click(self.clickX, self.clickY)
            print("pag clicked")

    def getGui(self):
        root = Frame()
        
        Label(root, text="Click ").grid(row=0, column=0)
        Button(root, text=str(self.clickX) + "," + str(self.clickY), command=self.getGui).grid(row=0, column=1)
        Label(root, text=" every ").grid(row=0, column=2)
        e = Entry(root)
        e.grid(row=0, column=3)
        e.insert(0, str(self.actionInterval))
        Label(root, text="ms when Pixel ").grid(row=0, column=4)
        Button(root, text=str(self.checkX) + "," + str(self.checkY), command=self.getGui).grid(row=0, column=5)
        Label(root, text=" has colour ").grid(row=0, column=6)
        Button(root, width=2, bg=self.checkColor, command=self.getGui).grid(row=0, column=7)
        Label(root, text="    Name: ").grid(row=0, column=8)
        e = Entry(root)
        e.grid(row=0, column=9)
        e.insert(0, str(self.name))

        return root
