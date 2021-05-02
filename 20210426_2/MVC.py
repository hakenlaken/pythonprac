import tkinter as tk


class View(tk.Frame):

    def __init__(self, master=None, title="task 2", control=None, **kwargs):
        self.control = control
        super().__init__(master, ** kwargs)
        if not master:  # pragma: no cover
            self.master.title(title)
            self.master.columnconfigure(0, weight=1)
            self.master.rowconfigure(0, weight=1)
            self.grid(sticky="NEWS")
        self.createWidgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def createWidgets(self):
        '''Create all the widgets.'''

    def assingbindings(self):
        """text"""

    def __call__(self, control=None):
        self.control = control
        self.assingbindings()
        self.mainloop()
        del self.control


class Model:

    def __init__(self, view):
        self.view = view

    def __call__(self, control=None):
        if control:  # pragma: no cover
            control.setup()
        self.view(control)


class Control:

    def __init__(self, model):
        self.model = model

    def setup(self):
        """TEXT"""
