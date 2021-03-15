'''
Tkinter skeleton app
'''
import tkinter as tk
from itertools import product

flag = True


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


class App(Application):
    def create_widgets(self):
        alpha = self.register(self.alpha)
        self.S = tk.StringVar()
        self.E = tk.Entry(self, textvariable=self.S,
                          validate='all', validatecommand=(alpha, '%P'))
        self.E.grid(columnspan=2)
        self.L = tk.Label(self, text="Lower letters only")
        self.L.grid(row=1, column=0)
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.Q.grid(row=1, column=1)

    def alpha(self, P):
        # print(f"{why}: '{txt}'")
        if str.isdigit(P) or P == "":
            return True
        else:
            return False


app = App(title="Sample application")
app.mainloop()
