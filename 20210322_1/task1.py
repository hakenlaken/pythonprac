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

        self.canvas = tk.Canvas(self, bg='black')
        self.startpress = False
        self.Motion = False
        self.oval = 0
        self.oval_width = 3
        self.oval_outline = "pink"
        self.oval_fill = "forestgreen"

        self.T = tk.Text(self, bg='black')
        self.T.tag_config('SyntaxChecker', foreground='red')
        self.lines = [""]

        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.clearB = tk.Button(self, text="Clear", command=self.Clear)
        self.drawB = tk.Button(self, text="Run", command=self.DrawTextHandler)

        self.helpS = tk.StringVar()
        self.helpS.set("Man Help")
        self.helpL = tk.Label(self, textvariable=self.helpS)

        self.obj_list = ["oval", "rectangle", "line"]

        self.T.bind("<KeyPress>", self.KeyHandler)
        self.T.bind("<Motion>", self.MotionHandler)

        self.T.tag_config("incorrect", foreground="red")
        self.T.tag_config("correct", foreground="green")

        self.T.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="NEWS")
        self.canvas.grid(row=0, column=4, rowspan=4, columnspan=4, sticky="NEWS")
        self.Q.grid(row=4, column=4, sticky="NEWS")
        self.clearB.grid(row=4, column=5, sticky="NEWS")
        self.drawB.grid(row=4, column=6, sticky="NEWS")
        self.helpL.grid(row=4, column=0, columnspan=4, sticky="NEWS")

    def Clear(self):
        for i in self.canvas.find_all():
            self.canvas.delete(i)

    def DrawTextHandler(self):
        self.Clear()
        self.lines = self.T.get("1.0", tk.END).split("\n")
        for i, line in enumerate(self.lines):
            words = line.split(" ")
            if words[0] in self.obj_list:
                try:
                    eval(f"self.canvas.create_{words[0]}({','.join(words[1:])})")
                except Exception:
                    self.T.tag_add('incorrect', str(i + 1) +
                                   '.0 linestart', str(i + 1) + '.0 lineend')
                    self.T.tag_remove('correct', str(i + 1) +
                                      '.0 linestart', str(i + 1) + '.0 lineend')
                else:
                    self.T.tag_add('correct', str(i + 1) +
                                   '.0 linestart', str(i + 1) + '.0 lineend')
                    self.T.tag_remove('incorrect', str(i + 1) +
                                      '.0 linestart', str(i + 1) + '.0 lineend')
            elif line.startswith("#"):
                self.T.tag_add('correct', str(i + 1) +
                               '.0 linestart', str(i + 1) + '.0 lineend')
                self.T.tag_remove('incorrect', str(i + 1) +
                                  '.0 linestart', str(i + 1) + '.0 lineend')
            else:
                self.T.tag_add('incorrect', str(i + 1) +
                               '.0 linestart', str(i + 1) + '.0 lineend')
                self.T.tag_remove('correct', str(i + 1) +
                                  '.0 linestart', str(i + 1) + '.0 lineend')
        pass

    def KeyHandler(self, event):
        self.lines = self.T.get("1.0", tk.END).split("\n")
        for i, line in enumerate(self.lines):
            words = line.split(" ")
            if line.startswith("#") or words[0] in self.obj_list:
                self.T.tag_add('correct', str(i + 1) +
                               '.0 linestart', str(i + 1) + '.0 lineend')
                self.T.tag_remove('incorrect', str(i + 1) +
                                  '.0 linestart', str(i + 1) + '.0 lineend')
            else:
                self.T.tag_add('incorrect', str(i + 1) +
                               '.0 linestart', str(i + 1) + '.0 lineend')
                self.T.tag_remove('correct', str(i + 1) +
                                  '.0 linestart', str(i + 1) + '.0 lineend')

    def MotionHandler(self, event):
        coords = self.T.index(tk.CURRENT).split('.')
        curx, words = int(coords[0]), [""]
        if self.lines[0] != '':
            words = self.lines[curx - 1].split(" ")
        if words[0] in self.obj_list:
            if words[0] == "oval" or words[0] == "rectangle":
                self.helpS.set(words[0] +
                               " start_x start_y end_x end_y outline='color' fill='color'")
            elif words[0] == "line":
                self.helpS.set("line start_x start_y end_x end_y width='width' fill='color'")
        elif words[0].startswith("#"):
            self.helpS.set("# line")
        elif self.lines[0] != '' and self.lines[curx - 1].isspace() is True or words[0] == '':
            self.helpS.set("Empty line")
        else:
            self.helpS.set("Not CCL line")


app = App(title="task1.py")
app.mainloop()
