'''
Tkinter skeleton app
'''
import tkinter as tk
from itertools import product


class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''


class App(Application):
    def create_widgets(self):
        super().create_widgets()
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.C = tk.Canvas()
        self.C.create_oval(10, 10, 200, 100, width=3, outline="pink", fill="forestgreen")
        self.Q.grid()
        self.C.grid()
        self.C.move(1,20,20)
        self.C.bind("<Motion>", lambda e: print(self.C.find_overlapping(e.x, e.y, e.x, e.y)))


app = App(title="Sample application")
app.mainloop()

