import time
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.showtime()

    def showtime(self):
        self.timeLabel["text"] = time.strftime("%c")

    def createWidgets(self):
        self.timeButton = tk.Button(self, text='Time', command=self.showtime)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.timeLabel = tk.Label(self, text='<time>')
        self.timeButton.grid()
        self.quitButton.grid()
        self.timeLabel.grid()


app = Application()
app.master.title('Sample application')
app.mainloop()
