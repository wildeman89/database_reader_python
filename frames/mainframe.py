from tkinter import Frame, Label


class MFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Label(self, text="Hello World!").grid(row=0, column=0)
