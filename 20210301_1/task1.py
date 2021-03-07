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
        self.quitButton = tk.Button(self, text='Exit', command=self.doexit)
        self.nextitemButton = tk.Button(self, text='Next item', command=self.nextitem_handler)
        self.menuLabel = tk.Label(self, text='<MenuItem>')
        self.nextitemButton.grid()
        self.menuLabel.grid()
        self.quitButton.grid()


app = Application()
app.master.title('Task 1')
app.mainloop()
