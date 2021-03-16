import threading


class App(threading.Thread):

    def __init__(self, root):
        threading.Thread.__init__(self)
        self.root = root
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.mainloop()
