'''
Tkinter skeleton app
'''
import tkinter as tk
import gettext
import locale

locale.setlocale(locale.LC_ALL, '')

gettext.install("task1", ".", names=("ngettext",))


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
        self.S = tk.StringVar()
        self.count = 0
        self.S.set(ngettext("%d time clicked", "%d times clicked", self.count) % (self.count,))

        self.L = tk.Label(self, textvariable=self.S)
        self.E = tk.Button(self, text=_("Press me"), command=self.validate_button)
        self.E.grid(row=0, columnspan=3)
        self.L.grid(row=1, columnspan=3)

    def validate_button(self):
        '''button validation'''
        # print("Modification at index " + index)
        self.count += 1
        self.S.set(ngettext("%d time clicked", "%d times clicked", self.count) % (self.count,))


class App(Application):
    def create_widgets(self):
        super().create_widgets()


def show_handler(self):
    self.S.set(self.SforE.get())


def main():
    app = App(title="task2.py")
    app.mainloop()


if __name__ == "__main__":
    main()
