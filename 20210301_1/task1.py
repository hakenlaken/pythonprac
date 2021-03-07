import tkinter as tk
import subprocess


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def doexit(self):
        """ заглушка обработчика нажатия Exit """
        pass

    def nextitem_handler(self):
        """ заглушка обработчика нажатия Next item """

    def createWidgets(self):
        self.choice = tk.StringVar()
        self.optionlist = ('One', 'Two', 'Three')
        self.choice.set(self.optionlist[0])
        self.quitButton = tk.Button(self, text='Exit', command=self.doexit)
        self.nextitemButton = tk.Button(self, text='Next item', command=self.nextitem_handler)
        self.dropMenu = tk.OptionMenu(self, self.choice, *self.optionlist)
        self.menuLabel = tk.Label(self, textvariable=self.choice)
        self.menuLabel.grid()
        self.nextitemButton.grid()
        self.dropMenu.grid()
        self.quitButton.grid()


app = Application()
app.master.title('Task 1')
app.mainloop()
