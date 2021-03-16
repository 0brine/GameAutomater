from Process import *
import pyautogui as pag

processes = []


def run_processes():
    global processes
    processes.append(Process(400, 250, 400, 250, (75, 219, 106), 10))
    while True:
        for p in processes:
            p.action()
        pag.sleep(10 / 1000)
