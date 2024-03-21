from tkinter import Tk

class Window:
    def __init__(self,title) -> None:
        self.window=Tk()
        self.window.title(title)
        self.window.resizable(width=False,height=False)
        self.window.geometry("400x400")