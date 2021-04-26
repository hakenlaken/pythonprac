import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None, model=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.model = model
        self.createWidgets()

    def nextitem_handler(self):
        """ заглушка обработчика нажатия Next item """
        self.choice.set(self.optionlist[(self.optionlist.index(
            self.choice.get()) + 1) % len(self.optionlist)])

    def createWidgets(self):
        self.E = tk.Entry(self)
        self.E.grid()
        self.L = tk.Label(self)
        self.L.grid()
        self.B = tk.Button(self, text="Copy", command=self.model.copy)
        self.B.grid()


class Model:
    def setup(self, view):
        self.view = view

    def copy(self):
        self.view.L["text"] = self.view.E.get()


if __name__ == "__main__":
    m = Model()
    app = Application(model=m)
    m.setup(app)
    app.master.title('Task 2')
    app.mainloop()
