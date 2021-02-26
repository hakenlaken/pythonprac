import tkinter as tk
import subprocess


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def showdate(self):
        result = subprocess.run(["date"], stdout=subprocess.PIPE, encoding='utf-8')
        self.multvar.set(result.stdout)

    def showdir(self):
        result = subprocess.run(["ls"], stdout=subprocess.PIPE, encoding='utf-8')
        self.multvar.set(result.stdout)

    def showgit(self):
        result = subprocess.run(["git"], stdout=subprocess.PIPE, encoding='utf-8')
        self.multvar.set(result.stdout)

    def createWidgets(self):
        self.multvar = tk.StringVar()
        self.dirButton = tk.Button(self, text='Dir', command=self.showdir)
        self.dateButton = tk.Button(self, text='Date', command=self.showdate)
        self.gitButton = tk.Button(self, text='Git', command=self.showgit)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.multipleLabel = tk.Label(self, textvariable=self.multvar)
        self.dateButton.grid(row=0, column=0)
        self.dirButton.grid(row=0, column=1)
        self.gitButton.grid(row=0, column=2)
        self.quitButton.grid(row=0, column=3)
        self.multipleLabel.grid(columnspan=4)


app = Application()
app.master.title('Task 2')
app.mainloop()

