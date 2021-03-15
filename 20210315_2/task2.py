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
            for row in range(self.grid_size()[1]):
                self.columnconfigure(column, weight=1)
                self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''
        self.B = tk.Button(self, text="Quit", command=self.master.quit)
        self.B.bind('<Any-KeyPress>', lambda event: print(event))
        self.master.bind('<Any-KeyPress>', lambda event: print("Root", event))
        self.B.grid()
        self.E = tk.Button(self, text="Event",
                           command=lambda: self.event_generate('<KeyPress-Return>'))
        self.E.grid()


class App(Application):
    def create_widgets(self):
        super().create_widgets()


app = App(title="Sample application")
app.mainloop()
