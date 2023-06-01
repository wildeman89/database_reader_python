from tkinter import Tk


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._winSetup()

    def _winSetup(self):
        self.title("My Program")
        self.geometry("800x640")

    def run(self):
        self.mainloop()
