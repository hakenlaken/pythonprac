'''
Tkinter skeleton app
'''
import tkinter as tk
import re
# from itertools import product


class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.pattern = re.compile(r"[-+]?(?:(?:\d*\.\d+)|(?:\d+\.?))?")
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
        self.S = tk.StringVar()
        self.S.set("")
        vcmd = (self.register(self.validate_username), "%i", "%P")
        self.E = tk.Entry(self, validate="key",
                          validatecommand=vcmd,
                          invalidcommand=self.print_error, textvariable=self.S)
        self.E.grid(row=0, columnspan=2)
        self.L = tk.Label(self, text="float numbers")
        self.L.grid(row=1, column=0)
        self.Q = tk.Button(self, text="Quit", command=self.quit_handler)
        self.Q.grid(row=1, column=1)

    def validate_username(self, index, username):
        '''entry validation'''
        # print("Modification at index " + index)
        return self.pattern.fullmatch(username) is not None

    def print_error(self):
        '''error validation'''
        # print("Invalid username character")

    def quit_handler(self):
        answer = self.S.get()
        if answer in ["", "-", "+"]:
            print(0)
        else:
            print(eval(answer))
        self.quit()


app = App(title="task1.py")
app.mainloop()
