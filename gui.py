from tkinter import *
import pag_stuff as pags
import main as main
from App import App
from threading import Thread
from Process import *
from Click import Click
from time import sleep

recordClicks = True
clicks = []

pag.click(400, 250)


def click(x, y, color):
    if recordClicks:
        c = Click(x, y, color)
        clicks.append(c)
        c.getGui().grid(in_=root, row=len(clicks), column=2)


def displayProcess(p, i):
    gui = p.getGui()
    gui.grid(in_=root, row=i, column=0)


def run():
    pags.startListener()

def runProsesses():
    main.run_processes()

t = Thread(target=run, daemon=True)
t.start()

t2 = Thread(target=runProsesses, daemon=True)
t2.start()

sleep(0.1)

root = Tk()
root.title("Game Automater")
root.geometry("800x400")
Label(root, width=10).grid(column=1)

p = Process()

displayProcess(p, 0)
displayProcess(p, 1)
displayProcess(p, 2)
displayProcess(p, 3)

f = Frame()
#Button(f, text="Start Recording", command=(lambda : recordClicks=True)

root.mainloop()
