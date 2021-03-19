'''
Tkinter skeleton app
'''
import tkinter as tk
from itertools import product
import re


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
        self.choice = tk.StringVar()
        self.S = tk.StringVar()
        self.S.set("Default")

        self.SforE = tk.StringVar()
        self.SforE.set("")
        self.pattern = re.compile(r"^\w{0,10}$")
        vcmd = (self.register(self.validate_word), "%i", "%P")
        self.E = tk.Entry(self, validate="key",
                          validatecommand=vcmd,
                          invalidcommand=self.print_error, textvariable=self.SforE)
        self.E.grid(row=0, columnspan=3)

        self.optionlist = ('One', 'Two', 'Three')
        self.choice.set(self.optionlist[0])
        self.OM = tk.OptionMenu(self, self.choice, *self.optionlist)
        self.QB = tk.Button(self, text="Quit", command=self.master.quit)
        # self.master.bind('<Any-KeyPress>', lambda event: print("Root", event))
        self.OM.grid(row=1, column=0, sticky="W")
        self.L = tk.Label(self, textvariable=self.S)
        self.L.bind('<Enter>', lambda event: self.S.set("Hi Mouse"))
        self.L.bind('<Leave>', lambda event: self.S.set("Bye Mouse"))
        self.L.grid(row=0, column=3, columnspan=2)
        self.QB.grid(row=1, column=4)
        self.IB = tk.Button(self, text="Insert",
                            command=lambda: self.E.insert(tk.END, self.choice.get()))
        self.IB.grid(row=1, column=2, sticky="E")
        self.SB = tk.Button(self, text="Show", command=lambda: self.S.set(self.SforE.get()))
        self.SB.grid(row=1, column=3)

    def validate_word(self, index, username):
        '''entry validation'''
        # print("Modification at index " + index)
        return self.pattern.fullmatch(username) is not None

    def print_error(self):
        '''error validation'''
        # print("Invalid username character")


class App(Application):
    def create_widgets(self):
        super().create_widgets()


app = App(title="task2.py")
app.mainloop()
