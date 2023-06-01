from tkinter import Tk
from frames.mainframe import MFrame


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._winSetUp()
        self.mainFrame: MFrame = MFrame(self)
        self.mainFrame.pack(fill="both")

    def run(self):
        self.mainloop()

    def _winSetUp(self):
        self.title("DB Reader")
        self.geometry("800x640")
        self["bg"] = "grey"
