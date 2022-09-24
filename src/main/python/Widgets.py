import tkinter as tk
from tkinter import ttk

class LabelEntryFrame(ttk.Frame):
    def __init__(self, root, parent):
        self.root=root
        self.parent=parent
        super().__init__(parent, borderwidth=2, relief=tk.RIDGE)
        self.labval=tk.StringVar()
        self.entvar=tk.StringVar()
        self.label=tk.Label(self, textvariable=self.labval)
        self.entry=tk.Entry(self, textvariable=self.entvar)
        self.label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

class Graph2DFrame(ttk.Frame):        
    def __init__(self, root, parent):
        self.root=root
        self.parent=parent
        super().__init__(parent, borderwidth=2, relief=tk.RIDGE)