import pyautogui as pag
from pynput import mouse
from gui import click


def check_on_screen():
    x, y = pag.position()
    if not pag.onScreen(x, y):
        pag.alert("Your mouse is not on the screen, you probaply have 2 Screens, This program can only accsess your "
                  "main screen, you can change your main screen in the Windows settings")
        return False
    return True


def on_click(x, y, button, pressed):
    print("clicked")
    if button == mouse.Button.left and pressed:
        color = pag.pixel(x, y)
        click(x, y, color)


def startListener():
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()
