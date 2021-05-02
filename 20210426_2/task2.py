# -*- coding: utf-8 -*-
import tkinter as tk
from MVC import Model, View, Control


class AppView(View):

    def nextitem_handler(self):
        """text"""
        self.choice.set(self.optionlist[(self.optionlist.index(
            self.choice.get()) + 1) % len(self.optionlist)])

    def createWidgets(self):
        self.Sa = tk.StringVar()
        self.Ea = tk.Entry(self, textvariable=self.Sa)
        self.Sb = tk.StringVar()
        self.Eb = tk.Entry(self, textvariable=self.Sb)
        self.Sc = tk.StringVar()
        self.Ec = tk.Entry(self, textvariable=self.Sc)
        self.La = tk.Label(self, text="coef a:")
        self.Lb = tk.Label(self, text="coef b:")
        self.Lc = tk.Label(self, text="coef c:")
        self.Ltask2 = tk.Label(self, text="Solving a * x^2 + b * x^2 + c = 0")
        self.Ltask2.grid(sticky="NEWS", row=0, columnspan=3)
        self.La.grid(sticky="NEWS", row=1, column=0)
        self.Lb.grid(sticky="NEWS", row=1, column=1)
        self.Lc.grid(sticky="NEWS", row=1, column=2)
        self.Ea.grid(sticky="NEWS", row=2, column=0)
        self.Eb.grid(sticky="NEWS", row=2, column=1)
        self.Ec.grid(sticky="NEWS", row=2, column=2)
        self.Sresult = tk.Label(self)
        self.Bsolve = tk.Button(self, text="Solve")
        self.BQ = tk.Button(self, text="Quit", command=self.master.quit)
        self.Bsolve.grid(sticky="NEWS", row=3, column=0)
        self.Sresult.grid(sticky="NEWS", row=3, column=1)
        self.BQ.grid(sticky="NEWS", row=3, column=2)

    def assingbindings(self):
        self.Bsolve["command"] = self.control.calculate


class AppControl(Control):

    def calculate(self):
        self.model.calculate()

    def setup(self):
        self.model.initialstate()


class AppModel(Model):

    def initialstate(self):
        self.view.Sresult["text"] = "Missing some coefficients"

    def calculate(self):
        try:
            a = float(self.view.Sa.get())
            b = float(self.view.Sb.get())
            c = float(self.view.Sc.get())
            result = self.calculateresult(a, b, c)
        except Exception as E:
            result = f"{E}"
            if result[-2:] == "''":
                result = "Missing some coefficients"
        self.view.Sresult["text"] = result

    def calculateresult(self, a, b, c):
        if not(a) and not(b) and not(c):
            return "∞"
        if not(a) and not(b):
            return "∅"
        if not(a):
            return -c / b
        else:
            D = b ** 2 - 4 * a * c
            if D > 0:
                return ((-b - D ** (1 / 2)) / (2 * a), (-b + D ** (1 / 2)) / (2 * a))
            if D == 0:
                return -b / (2 * a)
            if D < 0:
                return "∅"


if __name__ == "__main__":  # pragma: no cover
    view = AppView(title="task2")
    model = AppModel(view)
    control = AppControl(model)
    model(control)
