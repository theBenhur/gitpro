from tkinter import Tk,Frame,Label

class Window:
    def __init__(self,title) -> None:
        self.window=Tk()
        self.window.title(title)
        self.window.resizable(width=False,height=False)
        self.window.geometry("400x400")
        self.greeting_frame=Frame()
        Label(master=self.greeting_frame,text="Hola").pack()
        self.greeting_frame.pack()