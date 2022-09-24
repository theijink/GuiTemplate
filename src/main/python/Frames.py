import tkinter as tk
from tkinter import ttk

class Basic(ttk.Frame):
    def __init__(self, root, parent):
        self.root=root
        self.parent=parent
        super().__init__(self.parent, borderwidth=5, relief=tk.RIDGE)
