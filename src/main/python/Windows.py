import tkinter as tk
from tkinter import ttk

class Basic(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.updateloop(infinite=False))
        self.updateloop()

    def updateloop(self, infinite=True):
        while infinite:
            self.update()

class Preferences(tk.Tk):  
    def __init__(self):
        super().__init__()